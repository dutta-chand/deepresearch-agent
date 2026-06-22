"""
nodes/layer4_strategy/article_architect.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState, ArticleOutline
from services.gemini_service import GeminiService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class ArticleArchitectNode:
    """Design article structure and outline."""
    
    def __init__(self):
        self.gemini = GeminiService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Create article outline."""
        try:
            keyword = state["keyword"]
            style_profile = state.get("style_profile", {})
            seo_plan = state.get("seo_plan", {})
            
            outline_data = await self.gemini.create_article_outline(
                keyword, str(style_profile), str(seo_plan)
            )
            
            article_outline: ArticleOutline = {
                "title": f"Complete Guide to {keyword}",
                "meta_description": f"Learn everything about {keyword}",
                "sections": [
                    {"heading": "Introduction", "subheadings": []},
                    {"heading": "What is " + keyword, "subheadings": []},
                    {"heading": "Benefits", "subheadings": []},
                    {"heading": "How to", "subheadings": []},
                    {"heading": "Conclusion", "subheadings": []},
                ],
                "word_count_distribution": {
                    "introduction": 150,
                    "main_content": 1200,
                    "conclusion": 100,
                },
                "cta_placement": [4],  # Section index
            }
            
            return {
                "article_outline": article_outline,
                "current_stage": "article_architected",
            }
        except Exception as e:
            self.logger.error(f"Article architecture failed: {e}")
            raise
 
 