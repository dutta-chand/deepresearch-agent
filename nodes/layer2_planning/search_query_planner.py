"""
nodes/layer2_planning/search_query_planner.py
"""
 
from typing import Dict, Any, List
from schemas.state import ResearchState
from services.gemini_service import GeminiService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class SearchQueryPlannerNode:
    """Generate specific search queries."""
    
    def __init__(self):
        self.gemini = GeminiService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Generate search queries."""
        try:
            keyword = state["keyword"]
            research_plan = state.get("research_plan", {})
            keyword_profile = state.get("keyword_profile", {})
            
            queries_data = await self.gemini.generate_search_queries(
                keyword, str(research_plan)
            )
            
            search_queries: List[str] = [
                keyword,
                f"{keyword} guide",
                f"{keyword} 2024",
                f"how to {keyword}",
                f"{keyword} benefits",
            ]
            
            return {
                "search_queries": search_queries,
                "current_stage": "search_queries_planned",
            }
        except Exception as e:
            self.logger.error(f"Search query planning failed: {e}")
            raise
 
 