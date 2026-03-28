import subprocess
import os
import re
import glob
import argparse
import shutil
from datetime import datetime

def print_separator(char="=", length=80):
    print(char * length)

def print_header(text):
    print_separator("=")
    print(f"🎯 {text.center(76)}")
    print_separator("=")

def print_section(text):
    print_separator("-", 60)
    print(f"📂 {text}")
    print_separator("-", 60)

def sanitize_filename(filename):
    return filename.replace(" ", "_").replace("–", "-")

def fallback_print_to_pdf(pptx_path, pdf_path):
    print(f"🖨️ Falling back to AppleScript export for: {pptx_path}")
    pptx_path = os.path.abspath(pptx_path)
    pdf_path = os.path.abspath(pdf_path)
    applescript = f'''
    tell application "Microsoft PowerPoint"
      activate
      open POSIX file "{pptx_path}"
      delay 2
      save active presentation in POSIX file "{pdf_path}" as save as PDF
      close active presentation saving no
    end tell
    '''
    try:
        result = subprocess.run(
            ["osascript", "-e", applescript],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            print(f"✅ AppleScript export successful: {pdf_path}")
            return True
        print(f"❌ AppleScript error: {result.stderr.strip()}")
    except Exception as e:
        print(f"❌ Fallback failed: {e}")
    return False

def safe_convert(pptx, cwd, force):
    pdf_name = os.path.splitext(pptx)[0] + ".pdf"
    pdf_path = os.path.join(cwd, pdf_name)
    if os.path.exists(pdf_path) and not force:
        print(f"⏭️  Skipping conversion; PDF exists: {pdf_name}")
        return
    if os.path.exists(pdf_path) and force:
        print(f"🔄 Overwriting existing PDF: {pdf_name}")
    try:
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", pptx],
            cwd=cwd, check=True, timeout=45
        )
    except subprocess.CalledProcessError:
        print(f"❌ LibreOffice failed for {pptx}, trying fallback…")
        fallback_print_to_pdf(os.path.join(cwd, pptx), pdf_path)
    except subprocess.TimeoutExpired:
        print(f"⏱️ Timeout converting {pptx}, trying fallback…")
        fallback_print_to_pdf(os.path.join(cwd, pptx), pdf_path)

# ← Only new helper added
def compress_if_needed(pdf_path, max_size_mb=40):
    """Compress PDF in-place if it exceeds max_size_mb."""
    size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    if size_mb <= max_size_mb:
        return
    tmp = pdf_path + ".tmp.pdf"
    print(f"📦 Compressing {os.path.basename(pdf_path)} ({size_mb:.1f}MB)…")
    try:
        subprocess.run([
            "gs", "-sDEVICE=pdfwrite", "-dPDFSETTINGS=/screen",
            "-dNOPAUSE", "-dBATCH", "-dQUIET",
            f"-sOutputFile={tmp}", pdf_path
        ], check=True)
        shutil.move(tmp, pdf_path)
        new_size = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"✅ Compressed to {new_size:.1f}MB")
    except subprocess.CalledProcessError as e:
        print(f"❌ Compression failed: {e}")
        if os.path.exists(tmp):
            os.remove(tmp)

def merge_pdfs(pdf_list, output_path, force):
    if os.path.exists(output_path):
        if not force:
            print(f"⏭️  Skipping merge; exists: {os.path.basename(output_path)}")
            return
        print(f"🔄 Overwriting existing {os.path.basename(output_path)}")
    subprocess.run(["pdfunite", *pdf_list, output_path], check=True)
    print(f"✅ Created {os.path.basename(output_path)}")
    # ← Single call to compress if over 40MB
    compress_if_needed(output_path)



def process_unit(base, unit, force):
    """Process a unit by calling merge_pptx.py on both sub-patterns and sub-dirs."""
    unit_dir = os.path.join(base, unit)
    print_header(f"UNIT {unit}")

    for sub in ["Lecture-Slides", "Readings"]:
        # Build the *pattern* prefix (not including slash) for merge_pptx.py
        pattern = os.path.join(unit_dir, f"{unit}-{sub}")

        # Always call merge_pptx.py in pattern mode (it handles both dir & pattern)
        cmd = ["python", "merge_pptx.py", pattern]
        if force:   cmd.append("-f")

        try:                                        subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:  print(f"❌ Failed to process {unit}-{sub}: {e}")
        except FileNotFoundError:                   print("❌ merge_pptx.py not found")


    # Process the main unit directory
    cmd = ["python", "merge_pptx.py", unit_dir]
    if force: cmd.append("-f")
    
    try:                                        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:  print(f"❌ Failed to process unit {unit}: {e}")
    except FileNotFoundError:                   print("❌ merge_pptx.py not found in current directory")


def main():
    parser = argparse.ArgumentParser(description="Process all IDAI700 units")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Overwrite existing PDFs and merges")
    args = parser.parse_args()
    base = "/Users/pitergarcia/DataScience/Semester4/IDAI700"
    print_header("IDAI700 BATCH START")
    print(f"🕐 {datetime.now():%Y-%m-%d %H:%M:%S}")
    if args.force:  print("🔄 FORCE MODE ACTIVE")

    print()
    for i in range(1, 10):
        process_unit(base, f"IDAI700-Unit_{i}", args.force)
        print()

    print_separator("=")
    print(f"🏁 ALL DONE — {datetime.now():%Y-%m-%d %H:%M:%S}")
    print_separator("=")

if __name__ == "__main__":
    main()
