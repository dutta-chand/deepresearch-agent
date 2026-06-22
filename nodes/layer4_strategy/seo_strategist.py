"""
LAYER 4: CONTENT STRATEGY NODES
 
nodes/layer4_strategy/seo_strategist.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState, SEOPlan
from services.seo_service import SEOService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class SEOStrategistNode:
    """Create SEO optimization plan."""
    
    def __init__(self):
        self.seo_service = SEOService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Create SEO plan."""
        try:
            keyword = state["keyword"]
            keyword_profile = state.get("keyword_profile", {})
            location_profile = state.get("location_profile", {})
            
            seo_plan: SEOPlan = {
                "primary_keyword": keyword,
                "keyword_placement_strategy": {
                    "title": True,
                    "meta_description": True,
                    "h1": True,
                    "h2": True,
                },
                "keyword_density_targets": {
                    "primary": 1.5,
                    "secondary": 0.5,
                },
                "internal_linking_plan": [],
                "external_linking_plan": [],
                "schema_markup": ["Article", "NewsArticle"],
                "local_seo_signals": [
                    f"Include {location_profile.get('city', 'location')} references"
                ],
            }
            
            return {
                "seo_plan": seo_plan,
                "current_stage": "seo_planned",
            }
        except Exception as e:
            self.logger.error(f"SEO strategy failed: {e}")
            raise
 