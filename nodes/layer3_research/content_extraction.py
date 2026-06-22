"""
nodes/layer3_research/content_extraction.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState
from services.website_crawler import WebsiteCrawler
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class ContentExtractionNode:
    """Extract and parse content from search results."""
    
    def __init__(self):
        self.crawler = WebsiteCrawler()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Extract content from sources."""
        try:
            search_results = state.get("search_results", [])
            
            extracted_content = []
            for result in search_results[:5]:  # Limit to top 5
                url = result.get("url", "")
                html = await self.crawler.fetch_website(url)
                if html:
                    text = self.crawler.extract_text(html)
                    extracted_content.append({
                        "url": url,
                        "content": text[:3000],
                    })
            
            return {
                "raw_content": extracted_content,
                "current_stage": "content_extracted",
            }
        except Exception as e:
            self.logger.error(f"Content extraction failed: {e}")
            raise
 
 