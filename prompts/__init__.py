# prompts/__init__.py
from prompts.style_analysis import style_analysis_prompt
from prompts.brand_voice import brand_voice_prompt
from prompts.research_planning import research_plan_prompt
from prompts.seo_strategy import seo_strategy_prompt
from prompts.article_architecture import article_outline_prompt
from prompts.draft_writing import draft_writer_prompt
from prompts.fact_checking import fact_check_prompt
from prompts.refinement import humanization_refinement_prompt
from prompts.style_audit import style_audit_prompt

__all__ = [
    "style_analysis_prompt",
    "brand_voice_prompt",
    "research_plan_prompt",
    "seo_strategy_prompt",
    "article_outline_prompt",
    "draft_writer_prompt",
    "fact_check_prompt",
    "refinement_prompt",
    "style_audit_prompt",
]
