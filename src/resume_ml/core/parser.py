import pdfplumber
import docx
from typing import Optional
from pathlib import Path

class ResumeParser:
    """Handles text extraction from various resume formats."""
    
    def extract_text(self, file_path: str) -> Optional[str]:
        """Extract text from PDF, DOCX, or TXT files."""
        path = Path(file_path)
        if not path.exists():
            return None
            
        suffix = path.suffix.lower()
        
        try:
            if suffix == ".pdf":
                return self._from_pdf(file_path)
            elif suffix == ".docx":
                return self._from_docx(file_path)
            elif suffix == ".txt":
                return path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error extracting text from {file_path}: {e}")
            return None
            
        return None

    def _from_pdf(self, path: str) -> str:
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    def _from_docx(self, path: str) -> str:
        doc = docx.Document(path)
        return "\n".join([para.text for para in doc.paragraphs])
