"""
nodes/layer1_context/brand_voice_analyzer.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState, BrandVoiceProfile
from services.website_crawler import WebsiteCrawler
from services.gemini_service import GeminiService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class BrandVoiceAnalyzerNode:
    """Extract brand voice from website."""
    
    def __init__(self):
        self.crawler = WebsiteCrawler()
        self.gemini = GeminiService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Extract brand voice profile."""
        try:
            website_url = state["website_url"]
            
            html = await self.crawler.fetch_website(website_url)
            if not html:
                raise ValueError(f"Failed to fetch {website_url}")
            
            voice_data = await self.gemini.analyze_brand_voice(html)
            
            brand_voice: BrandVoiceProfile = {
                "brand_personality": "authoritative",
                "values": ["transparency", "innovation"],
                "communication_style": "direct",
                "target_audience_description": "professionals",
                # ... more fields
            }
            
            return {
                "brand_voice_profile": brand_voice,
                "current_stage": "brand_voice_analyzed",
            }
        except Exception as e:
            self.logger.error(f"Brand voice analysis failed: {e}")
            raise
 
 