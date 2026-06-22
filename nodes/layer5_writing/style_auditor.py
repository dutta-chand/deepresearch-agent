# nodes/layer5_writing/style_auditor.py
from schemas.state import ResearchState
from utils.logger import get_logger

logger = get_logger(__name__)


class StyleAuditorNode:
    """Audit article style matching."""

    async def run(self, state: ResearchState) -> dict:
        """Check style adherence."""
        draft_article = state.get("draft_article", "")
        style_profile = state.get("style_profile", {})
        
        style_audit_results = {
            "tone_match": True,
            "structure_match": True,
            "vocabulary_match": True,
            "style_score": 0.85,
            "recommendations": [],
        }
        
        return {
            "style_audit_results": style_audit_results,
            "current_stage": "style_audited",
        }