def article_outline_prompt(keyword: str, style_profile: str, seo_plan: str) -> str:
    """Create article structure and outline."""
    return f"""
Create a detailed article outline.
 
Keyword: {keyword}
Style to Match: {style_profile}
SEO Strategy: {seo_plan}
 
Return JSON outline:
{{
  "title": "SEO-optimized title",
  "meta_description": "compelling meta description (155 chars max)",
  "slug": "url-slug",
  "sections": [
    {{
      "heading": "H1/H2 heading",
      "subheadings": ["H3 subheading 1", "H3 subheading 2"],
      "word_count_target": <number>,
      "purpose": "section purpose",
      "content_points": ["point1", "point2"],
      "include_evidence": true/false,
      "include_cta": true/false
    }}
  ],
  "word_count_distribution": {{"intro": 150, "body": 1300, "conclusion": 100}},
  "keyword_placement_points": ["H1", "first paragraph", "H2", "last paragraph"],
  "estimated_sections": 6,
  "estimated_total_words": 1500
}}
"""