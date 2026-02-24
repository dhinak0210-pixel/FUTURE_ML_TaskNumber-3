from typing import List, Dict, Any
from resume_ml.core.matcher import JobMatcher

class CandidateRanker:
    """Ranks multiple candidates based on their match scores."""
    
    def __init__(self):
        self.matcher = JobMatcher()
        
    def rank_candidates(self, candidates: List[Dict[str, str]], jd_text: str) -> List[Dict[str, Any]]:
        """
        Rank a list of candidates.
        Each candidate should have 'id', 'name', and 'text'.
        """
        ranked_results = []
        
        for candidate in candidates:
            analysis = self.matcher.calculate_score(candidate['text'], jd_text)
            ranked_results.append({
                "candidate_id": candidate.get('id'),
                "name": candidate.get('name'),
                "score": analysis["overall_match_score"],
                "matched_keywords": analysis["matched_keywords"]
            })
            
        # Sort by score descending
        return sorted(ranked_results, key=lambda x: x['score'], reverse=True)
