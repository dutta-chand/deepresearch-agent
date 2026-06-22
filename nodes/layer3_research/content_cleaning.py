# nodes/layer3_research/content_cleaning.py
from schemas.state import ResearchState
from utils.logger import get_logger

logger = get_logger(__name__)


class ContentCleaningNode:
    """Clean and deduplicate research content."""

    async def run(self, state: ResearchState) -> dict:
        """Clean content from research phase."""
        raw_content = state.get("raw_content", [])
        
        # Deduplicate based on URL
        seen_urls = set()
        cleaned_content = []
        
        for item in raw_content:
            url = item.get("url", "")
            if url not in seen_urls:
                seen_urls.add(url)
                cleaned_content.append(item)
        
        return {
            "raw_content": cleaned_content,
            "current_stage": "content_cleaned",
        }