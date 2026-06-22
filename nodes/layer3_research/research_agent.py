# nodes/layer3_research/research_agent.py
from schemas.state import ResearchState
from utils.logger import get_logger

logger = get_logger(__name__)


class ResearchAgentNode:
    """Orchestrate additional research if needed."""

    async def run(self, state: ResearchState) -> dict:
        """Check if more research is needed."""
        identified_gaps = state.get("identified_gaps", [])
        
        needs_more_research = len(identified_gaps) > 0
        
        return {
            "needs_more_research": needs_more_research,
            "current_stage": "research_evaluated",
        }