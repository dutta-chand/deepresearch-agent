"""
nodes/layer2_planning/research_planner.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState, ResearchPlan
from services.gemini_service import GeminiService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class ResearchPlannerNode:
    """Create research strategy."""
    
    def __init__(self):
        self.gemini = GeminiService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Plan research strategy."""
        try:
            keyword = state["keyword"]
            location_profile = state.get("location_profile", {})
            trend_profile = state.get("trend_profile", {})
            
            location_context = f"{location_profile.get('city')} area"
            trends = str(trend_profile.get("location_trends", []))
            
            plan_data = await self.gemini.plan_research(
                keyword, location_context, trends
            )
            
            research_plan: ResearchPlan = {
                "focus_areas": [],
                "primary_angle": "comprehensive guide",
                "secondary_angles": [],
                "depth_strategy": "expert-level",
                "source_requirements": {
                    "news": 3,
                    "blog": 2,
                    "official": 2,
                },
                "local_context_integration": "natural incorporation",
                "evidence_requirements": [],
            }
            
            return {
                "research_plan": research_plan,
                "current_stage": "research_planned",
            }
        except Exception as e:
            self.logger.error(f"Research planning failed: {e}")
            raise
 
 