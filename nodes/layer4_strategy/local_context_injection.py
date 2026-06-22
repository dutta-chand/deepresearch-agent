# nodes/layer4_strategy/local_context_injection.py
from schemas.state import ResearchState
from utils.logger import get_logger

logger = get_logger(__name__)


class LocalContextInjectionNode:
    """Inject local context from pincode into strategy."""

    async def run(self, state: ResearchState) -> dict:
        """Integrate local context."""
        location_profile = state.get("location_profile", {})
        article_outline = state.get("article_outline", {})
        
        # Add local context to outline if needed
        if location_profile and article_outline:
            sections = article_outline.get("sections", [])
            for section in sections:
                if "local_context_integration" not in section:
                    section["local_context_integration"] = True
        
        return {
            "article_outline": article_outline,
            "current_stage": "local_context_injected",
        }