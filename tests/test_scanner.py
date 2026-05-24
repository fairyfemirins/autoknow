# tests/test_scanner.py
from autoknow.scanner import scan_codebase
import os

def test_scan_codebase(tmp_path):
    # Create test files
    (tmp_path / "test.py").write_text("def hello(): pass")
    (tmp_path / "test.js").write_text("function hello() {}")
    
    files = scan_codebase(str(tmp_path))
    assert len(files) == 2
    assert str(tmp_path / "test.py") in files
    assert str(tmp_path / "test.js") in files