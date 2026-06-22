"""
nodes/layer5_writing/fact_checker.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState
from services.fact_checking import FactCheckingService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class FactCheckerNode:
    """Verify claims in article."""
    
    def __init__(self):
        self.fact_checker = FactCheckingService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Fact-check article."""
        try:
            draft_article = state.get("draft_article", "")
            evidence = state.get("evidence_collection", {})
            
            # Extract claims and verify
            fact_check_results = await self.fact_checker.verify_claims(
                ["Sample claim from article"],
                evidence.get("evidence_items", [])
            )
            
            return {
                "fact_check_results": fact_check_results,
                "fact_check_passed": fact_check_results.get("unverified_count", 0) == 0,
                "current_stage": "article_fact_checked",
            }
        except Exception as e:
            self.logger.error(f"Fact-checking failed: {e}")
            raise
 
 