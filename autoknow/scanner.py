# autoknow/scanner.py
import os

def scan_codebase(directory: str) -> list:
    """Scan a directory and return code files."""
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith((".py", ".js", ".go", ".rs", ".java", ".ts")):
                files.append(os.path.join(root, filename))
    return files