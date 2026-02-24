import pytest
from resume_ml.core.matcher import JobMatcher

def test_calculate_score():
    matcher = JobMatcher()
    resume_text = "Experienced Python developer with AWS knowledge."
    jd_text = "Looking for a Python developer who knows AWS."
    
    result = matcher.calculate_score(resume_text, jd_text)
    
    assert "overall_match_score" in result
    assert result["overall_match_score"] > 0
    assert "python" in [k.lower() for k in result["matched_keywords"]]
    assert "aws" in [k.lower() for k in result["matched_keywords"]]

def test_calculate_score_no_match():
    matcher = JobMatcher()
    resume_text = "Chef with experience in Italian cuisine."
    jd_text = "Software engineer for cloud infrastructure."
    
    result = matcher.calculate_score(resume_text, jd_text)
    
    assert result["overall_match_score"] < 0.2  # Should be low
