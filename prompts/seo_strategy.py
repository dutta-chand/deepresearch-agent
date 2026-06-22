def seo_strategy_prompt(keyword: str, keywords_expanded: str) -> str:
    """Create SEO optimization strategy."""
    return f"""
Create a detailed SEO strategy.
 
Primary Keyword: {keyword}
Expanded Keywords: {keywords_expanded}
 
Return JSON SEO plan:
{{
  "on_page_optimization": {{
    "title": "optimized title (60 chars)",
    "meta_description": "optimized description (155 chars)",
    "h1": "H1 tag with primary keyword",
    "h2_strategy": "placement of secondary keywords",
    "keyword_density_targets": {{"primary": 1.5, "secondary": 0.5}},
    "first_100_words": "include primary keyword naturally"
  }},
  "internal_linking": ["link1", "link2"],
  "external_links": ["authoritative_link1", "authoritative_link2"],
  "schema_markup": ["Article", "NewsArticle", "BreadcrumbList"],
  "image_strategy": "alt text with keywords",
  "readability_targets": {{"flesch_score": 60, "avg_sentence_length": 15}},
  "freshness_signals": ["recent data", "current trends"],
  "local_seo_elements": ["local_keyword_1", "local_keyword_2"]
}}
"""
def seo_audit_prompt(article: str, keywords: str) -> str:
    """Audit article for SEO."""
    return f"""
Audit this article for SEO quality.
 
ARTICLE:
{article[:2000]}
 
TARGET KEYWORDS:
{keywords}
 
Analyze and return JSON:
{{
  "keyword_density": {{"primary": 1.5, "status": "optimal/low/high"}},
  "heading_structure_score": 0.85,
  "keyword_in_h1": true,
  "keyword_in_h2": true,
  "first_paragraph_keyword": true,
  "meta_tag_ready": true,
  "readability_score": 0.80,
  "word_count_status": "adequate/low/high",
  "internal_linking_potential": 3,
  "content_freshness": "high/medium/low",
  "recommendations": [
    "recommendation1",
    "recommendation2"
  ],
  "overall_seo_score": 0.82
}}
"""
 
 
__all__ = [
    "style_analysis_prompt",
    "brand_voice_prompt",
    "pincode_analysis_prompt",
    "trend_discovery_prompt",
    "intent_analysis_prompt",
    "seo_keyword_expansion_prompt",
    "research_plan_prompt",
    "search_query_generation_prompt",
    "evidence_extraction_prompt",
    "knowledge_synthesis_prompt",
    "article_outline_prompt",
    "seo_strategy_prompt",
    "writing_instructions_prompt",
    "draft_writer_prompt",
    "fact_check_prompt",
    "refinement_prompt",
    "seo_audit_prompt",
]
 