def writing_instructions_prompt(style_profile: str,
                                brand_voice: str,
                                keyword: str,
                                location: str) -> str:
    """Create detailed writing instructions."""
    return f"""
Create detailed instructions for article writing.
 
Style to Match: {style_profile}
Brand Voice: {brand_voice}
Keyword: {keyword}
Location: {location}
 
Return JSON instructions:
{{
  "tone_description": "specific tone guidelines",
  "vocabulary_guidelines": "word choice guidelines",
  "sentence_structure": "typical sentence patterns",
  "paragraph_style": "short/medium/long typical paragraphs",
  "heading_requirements": "how to structure headings",
  "formatting_preferences": ["bullets", "lists", "emphasis"],
  "cta_requirements": ["CTA 1", "CTA 2"],
  "local_context_integration": "how to weave in location naturally",
  "keyword_integration": "keyword usage guidelines",
  "prohibited_content": ["don't include this"],
  "required_elements": ["element1", "element2"],
  "brand_alignment_checklist": ["check1", "check2"],
  "target_reading_level": "grade 10/college/professional",
  "authenticity_requirement": "write original content, don't copy sources"
}}
"""
 
 
# ============================================================================
# LAYER 5: WRITING & VALIDATION PROMPTS
# ============================================================================
 
def draft_writer_prompt(keyword: str,
                       outline: str,
                       evidence: str,
                       style_profile: str,
                       brand_voice: str,
                       location: str,
                       instructions: str) -> str:
    """Generate article draft."""
    return f"""
Write a comprehensive, original article about: {keyword}
 
OUTLINE TO FOLLOW:
{outline}
 
EVIDENCE TO INCORPORATE (naturally, don't copy):
{evidence}
 
WRITING STYLE (write like this):
{style_profile}
 
BRAND VOICE (match this personality):
{brand_voice}
 
LOCAL CONTEXT TO WEAVE IN:
Location: {location}
- Integrate naturally and organically
- Don't force local references
- Make connections meaningful
 
DETAILED WRITING INSTRUCTIONS:
{instructions}
 
REQUIREMENTS:
1. Original writing - paraphrase evidence, don't copy
2. 1500-2000 words
3. Markdown format with proper heading hierarchy
4. Natural keyword integration
5. Engaging and informative
6. Professional tone
7. Include section headings as specified in outline
8. At least 2-3 paragraphs per major section
9. Clear transitions between sections
10. Compelling conclusion with CTA
 
START WRITING:
"""
 