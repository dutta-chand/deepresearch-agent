"""
LAYER 5: WRITING & VALIDATION NODES
 
nodes/layer5_writing/draft_writer.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState
from services.gemini_service import GeminiService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class DraftWriterNode:
    """Generate article draft."""
    
    def __init__(self):
        self.gemini = GeminiService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Write article draft."""
        try:
            keyword = state["keyword"]
            outline = state.get("article_outline", {})
            evidence = state.get("evidence_collection", {})
            style_profile = state.get("style_profile", {})
            brand_voice = state.get("brand_voice_profile", {})
            location_profile = state.get("location_profile", {})
            
            draft_article = await self.gemini.draft_article(
                keyword,
                str(outline),
                str(evidence),
                str(style_profile),
                str(brand_voice),
                str(location_profile.get("city", ""))
            )
            
            return {
                "draft_article": draft_article.get("article", ""),
                "current_stage": "article_drafted",
            }
        except Exception as e:
            self.logger.error(f"Article drafting failed: {e}")
            raise
 
 