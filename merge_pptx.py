import subprocess
import os
import re
import sys
import glob
import argparse
import shutil
from datetime import datetime


import atexit


def cleanup():
    # Kill any lingering processes
    os.system("pkill -f soffice 2>/dev/null")
    os.system("pkill -f 'Microsoft PowerPoint' 2>/dev/null")
    
    # Remove any .tmp.pdf files
    os.system(f"find '{base_dir}' -name '*.tmp' -delete 2>/dev/null")
    os.system(f"find '{base_dir}' -name '*.tmp.pdf' -delete 2>/dev/null")

def print_separator(char="=", length=80):
    print(char * length)

def print_header(text):
    print_separator("=")
    print(f"🎯 {text.center(76)}")
    print_separator("=")

def print_section(text):
    print("\n")
    print_separator("-", 60)
    print(f"📂 {text}")
    print_separator("-", 60)

def sanitize_filename(filename):
    return filename.replace(" ", "_").replace("–", "-")

def fallback_print_to_pdf(pptx_path, pdf_path):
    applescript = f'''
tell application "Microsoft PowerPoint"
  activate
  open POSIX file "{os.path.abspath(pptx_path)}"
  delay 2
  save active presentation in POSIX file "{os.path.abspath(pdf_path)}" as save as PDF
  close active presentation saving no
end tell
'''
    subprocess.run(["osascript", "-e", applescript], check=False)

def safe_convert(pptx, cwd, force):
    pdf     = os.path.splitext(pptx)[0] + ".pdf"
    pdf_path= os.path.join(cwd, pdf)
    if os.path.exists(pdf_path) and not force: return
    if os.path.exists(pdf_path) and force:
        print(f"🔄 Overwriting PDF: {pdf}")
    try:
        # Increased timeout and added capture_output for debugging
        result = subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", pptx],
            cwd=cwd, check=True, timeout=120, capture_output=True
        )
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, result.args)
    except subprocess.TimeoutExpired:
        print(f"⚠️ soffice timed out for {pptx} - falling back")
        fallback_print_to_pdf(os.path.join(cwd, pptx), pdf_path)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ soffice failed for {pptx} with error: {e.stderr.decode()}")
        fallback_print_to_pdf(os.path.join(cwd, pptx), pdf_path)
    except Exception as e:
        print(f"⚠️ Unexpected error for {pptx}: {str(e)} - falling back")
        fallback_print_to_pdf(os.path.join(cwd, pptx), pdf_path)

def compress_if_needed(pdf_path, max_mb=40):
    size_mb = os.path.getsize(pdf_path) / (1024*1024)
    
    if size_mb <= max_mb:return
    tmp = pdf_path + ".tmp.pdf"
    # Added -dCompatibilityLevel to potentially fix recursive dict issues
    print(f"📦 Compressing {os.path.basename(pdf_path)} ({size_mb:.1f}MB)…")
    subprocess.run(["gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", "-dPDFSETTINGS=/screen", "-dNOPAUSE", "-dBATCH", "-dQUIET", f"-sOutputFile={tmp}", pdf_path], check=True)
    
    shutil.move(tmp, pdf_path.replace(".pdf", "-compressed.pdf"))
    print(f"✅ Compressed to {(os.path.getsize(pdf_path)/(1024*1024)):.1f}MB")

def merge_pdfs(sources, out, force):
    if os.path.exists(out) and not force:
        print(f"⏭️ Skipping merge; exists {os.path.basename(out)}\n")
        return
    
    # Switched to gs for merging to better handle potential PDF issues
    if os.path.exists(out) and force: print(f"🔄 Overwriting {os.path.basename(out)}")
    gs_args = ["gs", "-dBATCH", "-dNOPAUSE", "-q", "-sDEVICE=pdfwrite", "-dPDFSETTINGS=/prepress", f"-sOutputFile={out}"] + sources
    
    print(f"✅ Created {os.path.basename(out)}\n")
    subprocess.run(gs_args, check=True)
    compress_if_needed(out)



def handle_lectures(base, name, sub, force, sufix=".pptx"):
    """Process a subfolder (Lecture-Slides, Readings, etc.). 
    Converts PPTX to PDF, collects PDFs, merges if >1, 
    and updates all_pdfs set with absolute paths.
    """
    # Check if we're in subdirectory mode (sub is not None) and the directory exists
    if sub is not None and os.path.isdir(base):
        print_section(f"{sub} — {name}")
        # Convert all PPTX files found in the subdirectory
        for pptx in sorted(os.listdir(base)):
            if pptx.lower().endswith(sufix):
                print(f"➡️ Converting: {pptx}")
                safe_convert(pptx, base, force)
    else:
        # Pattern mode: find PPTX files matching the pattern in current directory
        pptx_files = sorted(glob.glob(f"{sufix}"))
        print(pptx_files)
        if pptx_files:
            print("📦 Converting matched .pptx files…")
            # Convert each matched PPTX file
            for full in pptx_files:
                fname = os.path.basename(full)
                print(f"➡️ Converting: {fname}")
                safe_convert(fname, base, force)
     
    # Collect and merge the resulting PDFs from this processing
    return collect_and_merge_subpdfs(base, name, sub, force, sufix="-Lecture-Slides")   

def handle_readings(base, name, sub, force, sufix="-Readings"):
    """Process a subfolder (Lecture-Slides, Readings, etc.). 
    Converts PPTX to PDF, collects PDFs, merges if >1, 
    and updates all_pdfs set with absolute paths.
    """
    # Readings don't need conversion, just collect and merge existing PDFs
    return collect_and_merge_subpdfs(base, name, sub, force, sufix="-Readings")

def collect_and_merge_subpdfs(base, name, sub, force, sufix):
    """
    Find PDFs in `subdir` (excluding the sub-merged target), optionally merge them,
    and update `all_pdfs` (a set of ABSOLUTE paths) with what will be used downstream.
    Returns: list[str] of absolute paths actually used (either the merged file or the singles).
    """
    
    merging_files = []
    has_lectures_or_readings = re.search(r'readings|lecture-slides', base.lower())
    if sufix not in name and not has_lectures_or_readings: dir_path = base+"/"+name+sufix
    elif has_lectures_or_readings: dir_path = base
    else: dir_path = base+"/"+name
    print("\nCURRENT DIR:\t", dir_path)

    if os.path.exists(dir_path):
        # Exclude any previously merged files to avoid recursion
        merging_files   = [os.path.join(dir_path, p) for p in os.listdir(dir_path) if p.lower().endswith(".pdf") and not p.lower().endswith("merged.pdf")and os.path.basename(p) != f"{name}.pdf"]
        # print("Sub Found PDFs:", merging_files)   
    else:
        # Pattern mode: find PDFs matching the name pattern in the base directory
        pdf_files       = sorted(glob.glob(os.path.join(base, f"{name}*.pdf")))
        # Filter out the merged output file and final unit PDF to avoid circular references
        merging_files   = [p for p in pdf_files if p.lower().endswith(".pdf") and  not p.lower().endswith(f"-merged.pdf") and os.path.basename(p) != f"{name}.pdf"]
        # print("Base Found PDFs:", merging_files)  
        

    # Only merge if we have multiple PDFs
    out = os.path.join(base, f"{name}-Merged.pdf")                       
    if re.search(sufix, name) and len(merging_files) > 1:   merge_pdfs(merging_files, out, force)
    elif len(merging_files) > 1:                            print(f"\t\t⚠️ Sufix NOT a Match for {sufix if has_lectures_or_readings else name} matching PDFs found — skipping merge.")
    else:                                                   print("\t\t⚠️ Less than two matching PDFs found — skipping merge.")
    
    # Return the list of files that will be used in the final cohesive merge
    return [] if has_lectures_or_readings else merging_files

def convert_and_merge(path, force):
    # Initialize variables for both directory and pattern modes
    base   = ""
    isdir  = False
    all_pdfs = set()  # Track all PDF files to be included in final merge
    folder = os.path.abspath(path)
    name   = os.path.basename(folder)
    
    if os.path.isdir(path):
        # Set up for processing lecture slides (PPTX files)
        sufix   = ".pptx"
        base    = path
        isdir   = True
    else:
        # Pattern mode: processing files matching a pattern (not a directory)
        sub     = False  # No subdirectory processing in pattern mode
        prefix  = path.rstrip("/")
        sufix   = f"{prefix}*.pptx"  # Pattern to match PPTX files
        base    = os.path.dirname(os.path.abspath(prefix))
        name    = os.path.basename(prefix)
        
    print(f"PATH {path} \t\t PATTERN: {name}")
    # Set the final output path for the cohesive merge
    out = os.path.join(base, f"{name}.pdf")
    
    # Process readings (collect/merge existing PDFs)
    all_pdfs.update(handle_readings(base, name, sub=isdir, force=force))
    # Process lectures (convert PPTX to PDF, then collect/merge PDFs)
    all_pdfs.update(handle_lectures(base, name, sub=isdir, force=force, sufix=sufix))
    
    # Final cohesive merge of all collected PDFs into single unit file
    print_section(f"Cohesive — {name}")
    # print("PDF Files Found", all_pdfs)
    # Only merge if we have multiple PDFs to combine
    if len(all_pdfs) > 1 and not re.search(r'readings|lecture-slides', name.lower()):   merge_pdfs([item for item in all_pdfs], out, force)



def merge_all_units(base, force):
    print_header("FINAL UNITS MERGE")
    src=[]
    for i in range(1,10):
        p=os.path.join(base,f"IDAI700-Unit_{i}",f"IDAI700-Unit_{i}.pdf")
        if os.path.isfile(p):
            src.append(p)
    if len(src)>1:
        merge_pdfs(src, os.path.join(base,"units-merged.pdf"), force)


atexit.register(cleanup)
base_dir = ""
def main():
    try:
        p=argparse.ArgumentParser(description="IDAI700 tool")
        p.add_argument("path", nargs="?", help="Folder or pattern")
        p.add_argument("-f","--force",action="store_true",help="Overwrite")
        p.add_argument("--merge-all-units",action="store_true")
        a=p.parse_args()
        base="/Users/pitergarcia/DataScience/Semester4/IDAI700"
        
        global base_dir
        base_dir = a.path
        if a.merge_all_units:   merge_all_units(base,a.force)
        elif a.path:            convert_and_merge(a.path,a.force)
        else:                   print("Specify folder/pattern or --merge-all-units")

    finally:                    cleanup()

if __name__=="__main__":
    main()
