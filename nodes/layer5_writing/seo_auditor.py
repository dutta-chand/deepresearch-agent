# nodes/layer5_writing/seo_auditor.py
from schemas.state import ResearchState
from services.seo_service import SEOService
from utils.logger import get_logger

logger = get_logger(__name__)


class SEOAuditorNode:
    """Audit article for SEO optimization."""

    def __init__(self):
        self.seo_service = SEOService()

    async def run(self, state: ResearchState) -> dict:
        """Audit article SEO."""
        draft_article = state.get("draft_article", "")
        keyword_profile = state.get("keyword_profile", {})
        
        keywords = keyword_profile.get("keyword_variations", [])
        
        seo_audit_results = await self.seo_service.calculate_seo_score(
            draft_article,
            keywords
        )
        
        return {
            "seo_audit_results": seo_audit_results,
            "current_stage": "seo_audited",
        }