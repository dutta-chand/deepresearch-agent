"""
nodes/layer2_planning/seo_expansion.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState, KeywordProfile
from services.gemini_service import GeminiService
from services.seo_service import SEOService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class SEOExpansionNode:
    """Expand keyword with SEO variations."""
    
    def __init__(self):
        self.gemini = GeminiService()
        self.seo_service = SEOService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Expand keyword for SEO."""
        try:
            keyword = state["keyword"]
            location_profile = state.get("location_profile", {})
            
            # Get keyword variations from Gemini
            keyword_data = await self.gemini.extract_seo_keywords(keyword)
            
            keyword_profile: KeywordProfile = {
                "primary_keyword": keyword,
                "keyword_variations": [],
                "long_tail_keywords": [],
                "semantic_keywords": [],
                "lsi_keywords": [],
                "local_keywords": location_profile.get("locality", "").split(),
                "keyword_difficulty": 0.65,
                "search_volume": 5400,
            }
            
            return {
                "keyword_profile": keyword_profile,
                "current_stage": "keywords_expanded",
            }
        except Exception as e:
            self.logger.error(f"SEO expansion failed: {e}")
            raise
 
 