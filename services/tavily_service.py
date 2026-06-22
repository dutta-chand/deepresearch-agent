"""
services/tavily_service.py
 
Tavily API integration for web search.
"""
 
from typing import List, Dict, Any
from tavily import TavilyClient
from app.config import settings
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class TavilyService:
    """Web search service using Tavily API."""
    
    def __init__(self):
        self.client = TavilyClient(api_key=settings.tavily_api_key)
    
    async def search(self,
                    query: str,
                    max_results: int = 10,
                    search_depth: str = "advanced") -> List[Dict[str, Any]]:
        """Execute web search."""
        try:
            response = self.client.search(
                query=query,
                max_results=max_results,
                search_depth=search_depth
            )
            return response.get("results", [])
        except Exception as e:
            logger.error(f"Tavily search failed: {e}")
            return []
    
    async def fetch_source_metadata(self, url: str) -> Dict[str, Any]:
        """Get metadata for a source URL."""
        return {"url": url, "metadata": "extracted"}