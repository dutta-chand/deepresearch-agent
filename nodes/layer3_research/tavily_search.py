"""
LAYER 3: DEEP RESEARCH NODES
 
nodes/layer3_research/tavily_search.py
"""
 
from typing import Dict, Any, List
from schemas.state import ResearchState, Source
from services.tavily_service import TavilyService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class TavilySearchNode:
    """Execute web searches using Tavily."""
    
    def __init__(self):
        self.tavily = TavilyService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Execute searches for all queries."""
        try:
            search_queries = state.get("search_queries", [])
            
            all_results = []
            for query in search_queries:
                results = await self.tavily.search(query, max_results=10)
                all_results.extend(results)
            
            # Convert to Source objects
            sources: List[Source] = [
                {
                    "url": r.get("url", ""),
                    "title": r.get("title", ""),
                    "source_type": "web",
                    "domain": r.get("url", "").split("/")[2] if r.get("url") else "",
                    "domain_authority": 65.0,
                    "relevance_score": r.get("score", 0.8),
                    "language": "en",
                }
                for r in all_results
            ]
            
            return {
                "search_results": all_results,
                "raw_sources": sources,
                "current_stage": "search_completed",
            }
        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            raise
 
 