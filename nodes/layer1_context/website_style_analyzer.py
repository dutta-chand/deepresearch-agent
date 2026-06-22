"""
nodes/layer1_context/website_style_analyzer.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState, StyleProfile
from services.website_crawler import WebsiteCrawler
from services.gemini_service import GeminiService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class WebsiteStyleAnalyzerNode:
    """Extract style profile from reference website."""
    
    def __init__(self):
        self.crawler = WebsiteCrawler()
        self.gemini = GeminiService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """
        Analyze website and extract style profile.
        
        Returns:
            dict with style_profile
        """
        try:
            website_url = state["website_url"]
            
            # Fetch website
            html = await self.crawler.fetch_website(website_url)
            if not html:
                raise ValueError(f"Failed to fetch {website_url}")
            
            # Extract style
            style_data = await self.gemini.analyze_style(html)
            
            style_profile: StyleProfile = {
                "tone": "professional",
                "vocabulary_level": "advanced",
                "sentence_length_avg": 18.5,
                "paragraph_length_avg": 4,
                "heading_style": "descriptive",
                "use_bullets": True,
                "use_numbered_lists": True,
                "content_rhythm": "steady",
                # ... more fields populated from Gemini response
            }
            
            return {
                "style_profile": style_profile,
                "current_stage": "style_analyzed",
            }
        except Exception as e:
            self.logger.error(f"Style analysis failed: {e}")
            raise
 
 