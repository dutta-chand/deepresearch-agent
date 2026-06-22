"""
nodes/layer1_context/trend_discovery.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState, TrendProfile
from services.trend_discovery import TrendDiscoveryService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class TrendDiscoveryNode:
    """Discover local trends for pincode area."""
    
    def __init__(self):
        self.trend_service = TrendDiscoveryService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Discover trends for location and keyword."""
        try:
            pincode = state["pincode"]
            keyword = state["keyword"]
            
            # Discover trends
            trends_data = await self.trend_service.discover_trends(pincode)
            
            trend_profile: TrendProfile = {
                "location_trends": trends_data.get("trends", []),
                "seasonal_trends": [],
                "category_trends": {
                    keyword: ["trend1", "trend2"]
                },
                "search_volume_signals": {},
                # ... more fields
            }
            
            return {
                "trend_profile": trend_profile,
                "current_stage": "trends_discovered",
            }
        except Exception as e:
            self.logger.error(f"Trend discovery failed: {e}")
            raise
 
 