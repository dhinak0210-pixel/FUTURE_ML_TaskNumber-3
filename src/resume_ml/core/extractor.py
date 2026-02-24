import re
from typing import List, Set

class SkillExtractor:
    """Extracts technical and soft skills from text."""
    
    def __init__(self):
        # In a real scenario, we'd use a spaCy NER model or a large skill taxonomy.
        self.skill_db = {
            "python", "java", "javascript", "aws", "docker", "kubernetes", "sql", 
            "tableau", "power bi", "machine learning", "deep learning", "nlp",
            "communication", "leadership", "project management", "agile"
        }
        
    def extract_skills(self, text: str) -> List[str]:
        """Extract skills from text by matching against a database."""
        text = text.lower()
        # Simple word tokenization
        words = re.findall(r'\b\w+(?:\s\w+)*\b', text)
        
        extracted = []
        for skill in self.skill_db:
            if re.search(rf'\b{re.escape(skill)}\b', text):
                extracted.append(skill.title())
                
        return sorted(list(set(extracted)))
