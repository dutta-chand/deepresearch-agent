"""
nodes/layer3_research/evidence_synthesizer.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState, EvidenceCollection, Evidence
from services.gemini_service import GeminiService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class EvidenceSynthesizerNode:
    """Synthesize evidence from extracted content."""
    
    def __init__(self):
        self.gemini = GeminiService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Synthesize evidence."""
        try:
            raw_content = state.get("raw_content", [])
            raw_sources = state.get("raw_sources", [])
            
            evidence_items: list[Evidence] = []
            
            for content in raw_content[:3]:
                evidence: Evidence = {
                    "claim": "Key finding from source",
                    "source_url": content.get("url", ""),
                    "evidence_type": "statistic",
                    "confidence": 0.85,
                    "verification_status": "unverified",
                }
                evidence_items.append(evidence)
            
            evidence_collection: EvidenceCollection = {
                "total_sources": len(raw_sources),
                "primary_sources": raw_sources[:3],
                "secondary_sources": raw_sources[3:],
                "evidence_items": evidence_items,
                "coverage_areas": {},
                "high_quality_evidence": evidence_items,
            }
            
            return {
                "evidence_collection": evidence_collection,
                "current_stage": "evidence_synthesized",
            }
        except Exception as e:
            self.logger.error(f"Evidence synthesis failed: {e}")
            raise
 
 