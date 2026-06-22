# nodes/layer5_writing/refinement.py
from schemas.state import ResearchState
from services.gemini_service import GeminiService
from prompts.refinement import humanization_refinement_prompt, fact_check_refinement_prompt
from utils.logger import get_logger

logger = get_logger(__name__)


class RefinementNode:
    """Refine and humanize article based on feedback."""

    def __init__(self):
        self.gemini = GeminiService()

    async def run(self, state: ResearchState) -> dict:
        """
        Refine article through humanization and fact-check corrections.
        
        This node:
        1. Applies humanization to improve readability and naturalness
        2. Fixes any fact-check issues
        3. Maintains all critical elements (facts, SEO, structure, citations)
        4. Returns refined article for final formatting
        """
        
        try:
            draft_article = state.get("draft_article", "")
            if not draft_article:
                logger.warning("No draft article to refine")
                return {
                    "draft_article": draft_article,
                    "current_stage": "article_refined",
                }
            
            keyword = state.get("keyword", "")
            style_profile = state.get("style_profile", {})
            brand_voice_profile = state.get("brand_voice_profile", {})
            seo_plan = state.get("seo_plan", {})
            fact_check_results = state.get("fact_check_results", {})
            
            # Step 1: Apply humanization refinement
            logger.info("Applying humanization refinement to article")
            
            humanization_prompt = humanization_refinement_prompt(
                draft_article=draft_article,
                keyword=keyword,
                style_profile=style_profile,
                brand_voice=brand_voice_profile,
                seo_plan=seo_plan,
            )
            
            humanized_response = await self.gemini.refine_article(
                article=draft_article,
                feedback=humanization_prompt,
                style=str(style_profile),
            )
            
            refined_article = humanized_response.get("refined", draft_article)
            logger.debug(f"Humanization complete. New length: {len(refined_article)} chars")
            
            # Step 2: Apply fact-check corrections if needed
            has_flagged_claims = bool(fact_check_results.get("claims_needing_revision", []))
            
            if has_flagged_claims:
                logger.info("Applying fact-check corrections")
                
                fact_check_prompt = fact_check_refinement_prompt(
                    article=refined_article,
                    fact_check_results=fact_check_results,
                )
                
                fact_check_response = await self.gemini.refine_article(
                    article=refined_article,
                    feedback=fact_check_prompt,
                    style=str(style_profile),
                )
                
                refined_article = fact_check_response.get("refined", refined_article)
                logger.debug(f"Fact-check corrections applied. New length: {len(refined_article)} chars")
            
            # Step 3: Validate refinement
            refinement_validation = await self._validate_refinement(
                original=draft_article,
                refined=refined_article,
                state=state,
            )
            
            if not refinement_validation.get("valid", True):
                logger.warning("Refinement validation failed, using humanized version with caution")
                refinement_notes = refinement_validation.get("issues", [])
            else:
                refinement_notes = ["Refinement validation passed"]
            
            logger.info("Article refinement complete")
            
            return {
                "draft_article": refined_article,
                "refinement_notes": refinement_notes,
                "current_stage": "article_refined",
            }
        
        except Exception as e:
            logger.error(f"Refinement node error: {e}", exc_info=True)
            return {
                "draft_article": state.get("draft_article", ""),
                "refinement_notes": [f"Refinement error: {str(e)}"],
                "current_stage": "article_refined",
            }

    async def _validate_refinement(
        self,
        original: str,
        refined: str,
        state: ResearchState,
    ) -> dict:
        """
        Validate that refinement preserved critical elements.
        
        Checks:
        1. All citations still present
        2. Heading structure intact
        3. Word count within acceptable range
        4. Primary keyword still present
        5. All source URLs intact
        """
        
        issues = []
        
        # Check word count (allow -10% to +10%)
        original_words = len(original.split())
        refined_words = len(refined.split())
        word_count_change = abs(refined_words - original_words) / original_words if original_words > 0 else 0
        
        if word_count_change > 0.10:
            issues.append(f"Word count changed by {word_count_change*100:.1f}% (original: {original_words}, refined: {refined_words})")
        
        # Check heading preservation
        original_headings = original.count("##")
        refined_headings = refined.count("##")
        
        if original_headings != refined_headings:
            issues.append(f"Heading count mismatch (original: {original_headings}, refined: {refined_headings})")
        
        # Check primary keyword presence
        keyword = state.get("keyword", "").lower()
        if keyword and keyword not in refined.lower():
            issues.append(f"Primary keyword '{keyword}' missing from refined article")
        
        # Check citation preservation
        sources = state.get("sources", [])
        for source in sources:
            url = source.get("url", "")
            if url and url not in refined:
                issues.append(f"Citation link missing: {url}")
        
        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "word_count_original": original_words,
            "word_count_refined": refined_words,
        }
