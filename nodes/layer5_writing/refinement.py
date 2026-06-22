"""
nodes/layer5_writing/refinement.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState
from services.gemini_service import GeminiService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class RefinementNode:
    """Polish article based on fact-check feedback."""
    
    def __init__(self):
        self.gemini = GeminiService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Refine article."""
        try:
            draft_article = state.get("draft_article", "")
            fact_check_results = state.get("fact_check_results", {})
            style_profile = state.get("style_profile", {})
            
            refined_article = await self.gemini.refine_article(
                draft_article,
                str(fact_check_results),
                str(style_profile)
            )
            
            return {
                "draft_article": refined_article.get("refined", draft_article),
                "current_stage": "article_refined",
            }
        except Exception as e:
            self.logger.error(f"Refinement failed: {e}")
            raise
 
 