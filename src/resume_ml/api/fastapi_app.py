from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import List
import os
import shutil
import uuid
from pathlib import Path

from resume_ml.core.parser import ResumeParser
from resume_ml.core.matcher import JobMatcher

app = FastAPI(title="Resume ML System API")

parser = ResumeParser()
matcher = JobMatcher()

TEMP_DIR = Path("data/temp")
TEMP_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Welcome to Resume ML System API", "version": "2.0.0"}

@app.post("/analyze")
async def analyze_resume(
    jd_text: str = Form(...),
    file: UploadFile = File(...)
):
    """
    Analyze a resume file against a job description.
    """
    # Create a unique temp file
    temp_file_path = TEMP_DIR / f"{uuid.uuid4()}_{file.filename}"
    
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # 1. Parse
        resume_text = parser.extract_text(str(temp_file_path))
        if not resume_text:
            raise HTTPException(status_code=400, detail="Could not extract text from the provided file.")
            
        # 2. Match
        analysis_result = matcher.calculate_score(resume_text, jd_text)
        
        return {
            "filename": file.filename,
            "analysis": analysis_result
        }
        
    finally:
        # Cleanup
        if temp_file_path.exists():
            temp_file_path.unlink()

@app.post("/analyze-text")
async def analyze_text(
    resume_text: str = Form(...),
    jd_text: str = Form(...)
):
    """
    Analyze raw resume text against a job description.
    """
    analysis_result = matcher.calculate_score(resume_text, jd_text)
    return {"analysis": analysis_result}
