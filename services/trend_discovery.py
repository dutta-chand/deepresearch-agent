"""
services/trend_discovery.py
 
Local trend analysis service.
"""
 
from typing import List, Dict, Any
from services.tavily_service import TavilyService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class TrendDiscoveryService:
    """Discover local trends for pincode area."""
    
    def __init__(self):
        self.tavily = TavilyService()
    
    async def discover_trends(self, pincode: str) -> Dict[str, Any]:
        """Find trends relevant to pincode area."""
        # Search for pincode-specific trends
        queries = [
            f"{pincode} trending topics",
            f"{pincode} news today",
            f"what's popular in {pincode}",
        ]
        
        trends = []
        for query in queries:
            results = await self.tavily.search(query, max_results=3)
            trends.extend([r.get("title") for r in results])
        
        return {
            "pincode": pincode,
            "trends": trends,
            "trend_count": len(trends),
        }
 
 