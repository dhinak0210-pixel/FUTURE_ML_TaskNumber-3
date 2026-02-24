import re
from typing import List, Dict, Any

class JobMatcher:
    """Matches resumes against job descriptions using semantic alignment."""
    
    def __init__(self):
        # In a real scenario, we would load a sentence-transformer model here.
        pass
        
    def calculate_score(self, resume_text: str, jd_text: str) -> Dict[str, Any]:
        """
        Calculate a match score between 0 and 1.
        Designated as a placeholder for full BERT/LLM matching.
        """
        resume_words = set(re.findall(r'\w+', resume_text.lower()))
        jd_words = set(re.findall(r'\w+', jd_text.lower()))
        
        # Simple Jaccard similarity as a baseline
        intersection = resume_words.intersection(jd_words)
        union = resume_words.union(jd_words)
        
        score = len(intersection) / len(union) if union else 0.0
        
        # Identify matching keywords
        common_keywords = list(intersection)
        
        return {
            "overall_match_score": round(score, 4),
            "matched_keywords": common_keywords[:20],  # Top 20 for brief display
            "engine": "KeywordBaselineV1"
        }
