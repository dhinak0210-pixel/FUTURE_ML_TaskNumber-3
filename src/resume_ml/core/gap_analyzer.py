from typing import List, Dict, Set
from resume_ml.core.extractor import SkillExtractor

class SkillGapAnalyzer:
    """Identifies skills present in JD but missing in Resume."""
    
    def __init__(self):
        self.extractor = SkillExtractor()
        
    def analyze_gaps(self, resume_text: str, jd_text: str) -> Dict[str, List[str]]:
        """Compare skills and return matched and missing ones."""
        resume_skills = set(self.extractor.extract_skills(resume_text))
        jd_skills = set(self.extractor.extract_skills(jd_text))
        
        matched = jd_skills.intersection(resume_skills)
        missing = jd_skills.difference(resume_skills)
        
        return {
            "matched_skills": sorted(list(matched)),
            "missing_skills": sorted(list(missing))
        }
