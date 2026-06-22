# nodes/layer4_strategy/style_alignment.py
from schemas.state import ResearchState
from utils.logger import get_logger

logger = get_logger(__name__)


class StyleAlignmentNode:
    """Generate writing instructions aligned with website style."""

    async def run(self, state: ResearchState) -> dict:
        """Create style-aligned writing instructions."""
        style_profile = state.get("style_profile", {})
        brand_voice_profile = state.get("brand_voice_profile", {})
        
        writing_instructions = {
            "tone_description": style_profile.get("tone", "professional"),
            "vocabulary_guidelines": f"Level: {style_profile.get('vocabulary_level', 'intermediate')}",
            "sentence_structure": "varies",
            "paragraph_style": style_profile.get("paragraph_style", "medium"),
            "heading_requirements": "match style profile",
            "formatting_preferences": [],
            "cta_requirements": [],
            "brand_alignment_checklist": [],
            "prohibited_content": [],
            "required_elements": [],
        }
        
        return {
            "writing_instructions": writing_instructions,
            "current_stage": "style_aligned",
        }