def style_analysis_prompt(html_content: str) -> str:
    """Analyze website style and tone."""
    return f"""
Analyze this website's writing style and tone. Extract a detailed style profile.
 
HTML Content:
{html_content[:3000]}
 
Analyze and return JSON with:
{{
  "tone": "professional/casual/friendly/formal",
  "vocabulary_level": "simple/intermediate/advanced/technical",
  "sentence_length_avg": <number>,
  "paragraph_length_avg": <number>,
  "heading_style": "descriptive/question/how-to/command",
  "use_bullets": true/false,
  "use_numbered_lists": true/false,
  "use_blockquotes": true/false,
  "use_code_blocks": true/false,
  "use_tables": true/false,
  "structure_pattern": ["Introduction", "Main Points", "Conclusion"],
  "cta_style": "direct/soft/question-based",
  "cta_frequency_per_article": <number>,
  "opening_style": "story/question/statistic/hook",
  "closing_style": "summary/cta/thought-provoking",
  "content_rhythm": "fast-paced/steady/slow",
  "formatting_emphasis": "bold/italic/code/combinations",
  "link_density_per_100_words": <number>,
  "uses_storytelling": true/false,
  "uses_examples": true/false,
  "data_driven": true/false
}}
 
Be precise and specific based on the HTML structure and content.
"""
 