import pytest
import os
from pathlib import Path
from resume_ml.core.parser import ResumeParser

def test_extract_text_txt(tmp_path):
    parser = ResumeParser()
    test_file = tmp_path / "test_resume.txt"
    content = "Hello, this is a test resume content."
    test_file.write_text(content, encoding="utf-8")
    
    extracted = parser.extract_text(str(test_file))
    assert extracted == content

def test_extract_text_nonexistent():
    parser = ResumeParser()
    assert parser.extract_text("nonexistent_file.pdf") is None
