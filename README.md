# Disk-signature-Recovery
Signature-based file recovery toolkit in Python. Scans raw disks or images for known file signatures (JPG, PNG, PDF, LOG) and reconstructs recoverable files without relying on filesystem metadata. Lightweight, forensic-friendly, and dependency-free.

# Signature-recovery

Signature-based file recovery toolkit in Python.

## Supported Formats
- JPG
- PNG
- PDF
- LOG (timestamp-based)

## Usage
Open the desired carver script (e.g., `jpg_recover.py`) in VS Code and run it.  
Update the `source` (disk image or device path) and `output_dir` variables as needed inside the script before execution.

## Notes
- Python ≥ 3.8  
- No external dependencies  
- Runs in read-only mode on the source  
