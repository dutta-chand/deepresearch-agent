# prompts/refinement.py
def humanization_refinement_prompt(
    draft_article: str,
    keyword: str,
    style_profile: dict,
    brand_voice: dict,
    seo_plan: dict,
) -> str:
    """
    Prompt for humanizing and refining article while preserving all critical elements.
    Focus on making the article feel written by a skilled human content creator.
    """
    
    style_tone = style_profile.get("tone", "professional")
    style_rhythm = style_profile.get("content_rhythm", "steady")
    vocab_level = style_profile.get("vocabulary_level", "intermediate")
    brand_personality = brand_voice.get("brand_personality", "professional")
    primary_keyword = seo_plan.get("primary_keyword", keyword)
    
    return f"""You are an expert content refinement specialist tasked with humanizing an AI-generated article while preserving ALL critical elements.

ARTICLE TO REFINE:
{draft_article}

CONSTRAINTS (DO NOT VIOLATE):
1. Preserve every factual claim exactly as written
2. Preserve all source citations and URLs
3. Preserve all heading hierarchy and structure
4. Preserve all markdown formatting
5. Preserve SEO keyword placement strategy
6. Preserve word count range (1500-2000 words)
7. Preserve all numerical data and statistics
8. Preserve local pincode context references
9. Preserve metadata and schema markup references
10. Preserve opening and closing calls-to-action

TARGET STYLE:
- Tone: {style_tone}
- Rhythm: {style_rhythm}
- Vocabulary Level: {vocab_level}
- Brand Personality: {brand_personality}
- Primary Keyword: {primary_keyword}

HUMANIZATION OBJECTIVES:
1. Sentence Variation
   - Mix short (5-8 word) sentences with longer (15-20 word) sentences
   - Create rhythm through alternating sentence lengths
   - Use 1-2 short punchy sentences per paragraph
   - Avoid monotonous medium-length sentences

2. Narrative Flow
   - Replace robotic transitions with natural connectors
   - Use "But", "So", "Because" instead of "Furthermore", "Additionally", "Moreover"
   - Create cause-and-effect relationships naturally
   - Build momentum toward conclusions organically

3. Readability Enhancement
   - Convert passive voice to active voice where possible (without losing nuance)
   - Eliminate redundant explanations
   - Break up dense paragraphs into scannable chunks
   - Use white space effectively

4. Conversational Quality
   - Include rhetorical questions occasionally
   - Use "you" language where appropriate
   - Add relevant analogies or examples (must be factually accurate)
   - Show personality while maintaining professionalism

5. EEAT Signal Enhancement
   - Strengthen expertise signals through confident language
   - Add experience-based phrasing ("In practice...", "We've found...")
   - Increase authoritativeness through data-backed claims
   - Build trustworthiness by acknowledging nuance and complexity

6. AI Detection Reduction
   PHRASES TO ELIMINATE:
   - "In today's rapidly evolving landscape"
   - "It is important to note"
   - "In conclusion"
   - "Delve into"
   - "Unlock the potential"
   - "Leverage"
   - "Harness"
   - "In the modern world"
   - "As we navigate..."
   - "It is worth noting"
   - "At the end of the day"
   - "All things considered"
   - "In this digital age"
   - "The bottom line is"
   - "To summarize"
   
   REPLACE WITH:
   - "Today's" or "Right now"
   - "Importantly" or just state the fact
   - "That's it" or "Here's what matters" or start new section
   - "Explore" or "Understand"
   - "Maximize" or "Improve"
   - "Use" or "Apply"
   - "Use" or "Take advantage of"
   - "Today" or specific timeframe
   - "As we..." with specific action
   - "Worth knowing" or just state directly
   - "Ultimately" or remove entirely
   - "Basically" or be specific
   - "Now" or specific context
   - "Here's what works" or specific insight
   - "Recap" or specific summary

7. Keyword Preservation
   - Primary keyword appears naturally 1-2 times per 300 words
   - Never keyword stuff
   - Maintain semantic variations of primary keyword
   - Keep keyword placement in: title, first paragraph, H2 headings, conclusion
   - Avoid artificial keyword insertion

8. Professional Authority
   - Maintain confident, knowledgeable tone
   - Keep technical accuracy
   - Preserve expert perspective
   - Support claims with evidence
   - Acknowledge limitations honestly

EXECUTION STEPS:
1. Read the article once for overall structure
2. Identify and mark all facts, citations, and SEO keywords
3. Rewrite each paragraph with improved sentence variety
4. Replace robotic phrases with natural alternatives
5. Enhance narrative connections between sections
6. Add conversational elements without compromising expertise
7. Verify all facts remain unchanged
8. Verify all citations remain intact
9. Verify all keywords are naturally integrated
10. Ensure heading hierarchy is preserved

OUTPUT REQUIREMENTS:
- Return ONLY the refined article in markdown format
- Maintain ALL original formatting (bold, italics, lists, blockquotes)
- Include ALL original citations and source references
- Keep heading hierarchy exactly as original
- Preserve word count within 5% of original
- Make no mention of changes or refinements in the output

START REFINING NOW:
"""


def fact_check_refinement_prompt(article: str, fact_check_results: dict) -> str:
    """
    Prompt for refining article based on fact-check feedback.
    """
    
    flagged_claims = fact_check_results.get("claims_needing_revision", [])
    
    if not flagged_claims:
        return ""
    
    flagged_text = "\n".join([f"- {claim}" for claim in flagged_claims])
    
    return f"""You are a fact-checking specialist. Revise the following article to address flagged claims.

ARTICLE:
{article}

FLAGGED CLAIMS NEEDING REVISION:
{flagged_text}

REQUIREMENTS:
1. Fix only the flagged claims
2. Do NOT change any other content
3. Do NOT alter heading structure
4. Do NOT remove citations
5. Do NOT change formatting
6. Do NOT modify word count significantly
7. Strengthen claims with evidence where possible
8. Maintain SEO keyword placement
9. Keep professional tone

Return the revised article with only the necessary changes.
"""
