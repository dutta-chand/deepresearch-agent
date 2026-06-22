"""
services/fact_checking.py
 
Claim verification service.
"""
 
from typing import Dict, Any, List
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class FactCheckingService:
    """Verify claims against sources."""
    
    async def verify_claims(self,
                           claims: List[str],
                           sources: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Verify multiple claims."""
        results = []
        for claim in claims:
            result = await self.verify_single_claim(claim, sources)
            results.append(result)
        
        return {
            "verified_count": sum(1 for r in results if r["status"] == "verified"),
            "unverified_count": sum(1 for r in results if r["status"] == "unverified"),
            "contradicted_count": sum(1 for r in results if r["status"] == "contradicted"),
            "details": results,
        }
    
    async def verify_single_claim(self,
                                  claim: str,
                                  sources: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Verify a single claim."""
        # Simple keyword matching (in production, use embeddings)
        claim_words = set(claim.lower().split())
        
        matches = 0
        for source in sources:
            content = source.get("content", "").lower()
            matches += sum(1 for word in claim_words if word in content)
        
        confidence = matches / len(claim_words) if claim_words else 0
        
        status = "verified" if confidence > 0.6 else "unverified"
        
        return {
            "claim": claim,
            "status": status,
            "confidence": confidence,
            "matches_found": matches,
        }
 
 