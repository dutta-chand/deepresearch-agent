def pincode_analysis_prompt(pincode: str, city: str) -> str:
    """Analyze local context for pincode."""
    return f"""
Provide detailed local context analysis for:
- Pincode: {pincode}
- City/Area: {city}
 
Return JSON with demographic and contextual information:
{{
  "population": <estimated number>,
  "area_type": "urban/suburban/rural",
  "climate": "tropical/temperate/arid/etc",
  "language_primary": "language",
  "language_secondary": ["languages"],
  "economic_status": "low/lower-middle/middle/upper-middle/high",
  "literacy_rate": <percentage>,
  "internet_penetration": <percentage>,
  "major_industries": ["industry1", "industry2"],
  "local_attractions": ["attraction1", "attraction2"],
  "transportation": ["type1", "type2"],
  "housing_type": "apartments/houses/mixed",
  "local_government": "municipal_corporation/municipality",
  "nearby_major_cities": ["city1", "city2"]
}}
"""
 
 
def trend_discovery_prompt(pincode: str, keyword: str) -> str:
    """Discover local trends."""
    return f"""
Identify trending topics and interests for:
- Pincode: {pincode}
- Keyword: {keyword}
 
Return JSON with local trends:
{{
  "local_trending_now": ["trend1", "trend2", "trend3"],
  "seasonal_trends": ["seasonal_trend1", "seasonal_trend2"],
  "category_related_trends": ["related_trend1", "related_trend2"],
  "viral_topics_in_area": ["viral1", "viral2"],
  "local_news_highlights": ["news1", "news2"],
  "emerging_interests": ["emerging1", "emerging2"],
  "cultural_events": ["event1", "event2"],
  "social_signals": ["signal1", "signal2"]
}}
"""
def intent_analysis_prompt(keyword: str) -> str:
    """Analyze search intent for keyword."""
    return f"""
Analyze search intent for the keyword: "{keyword}"
 
Return JSON:
{{
  "search_intent": "informational/transactional/navigational/local",
  "intent_confidence": <0-1>,
  "user_journey_stage": "awareness/consideration/decision",
  "pain_points": ["pain1", "pain2"],
  "motivations": ["motivation1", "motivation2"],
  "information_needs": ["need1", "need2"],
  "decision_criteria": ["criteria1", "criteria2"],
  "common_questions": ["question1", "question2"]
}}
"""

def seo_keyword_expansion_prompt(keyword: str, location: str) -> str:
    """Expand keyword with SEO variations."""
    return f"""
Expand the keyword "{keyword}" with SEO variations for location: {location}
 
Return JSON with expanded keyword list:
{{
  "keyword_variations": ["variation1", "variation2"],
  "long_tail_keywords": ["long_tail1", "long_tail2"],
  "semantic_keywords": ["semantic1", "semantic2"],
  "lsi_keywords": ["lsi1", "lsi2"],
  "question_keywords": ["question1", "question2"],
  "local_keywords": ["local1", "local2"],
  "related_searches": ["related1", "related2"],
  "trending_variations": ["trending1", "trending2"]
}}
 
Focus on keywords that would appeal to users in {location}.
"""
 
 
def research_plan_prompt(keyword: str, location_context: str, trends: str) -> str:
    """Create comprehensive research strategy."""
    return f"""
Create a detailed research plan for:
Keyword: {keyword}
Location: {location_context}
Local Trends: {trends}
 
Return JSON research plan:
{{
  "focus_areas": ["area1", "area2", "area3"],
  "primary_angle": "main approach/narrative",
  "secondary_angles": ["angle1", "angle2"],
  "depth_strategy": "beginner/intermediate/expert",
  "source_requirements": {{"academic": 2, "news": 3, "blog": 2, "official": 2}},
  "expected_research_depth": "shallow/moderate/deep",
  "local_context_integration": "how to weave in local angle",
  "brand_alignment": "how to match brand voice",
  "seo_integration": "how to incorporate SEO naturally",
  "evidence_types_needed": ["statistic", "case study", "expert quote"],
  "estimated_content_sections": 7,
  "estimated_word_count": 2000
}}
"""
 
 
def search_query_generation_prompt(keyword: str, research_plan: str) -> str:
    """Generate specific search queries."""
    return f"""
Based on this keyword and research plan, generate targeted search queries.
 
Keyword: {keyword}
Research Plan: {research_plan}
 
Return a JSON list of 10-15 specific, diverse search queries:
{{
  "search_queries": [
    "query1",
    "query2",
    "query3",
    ... (10-15 total)
  ]
}}
 
Queries should cover:
- Broad topic overview
- Specific subtopics
- How-to angles
- News/recent developments
- Expert perspectives
- Local angles
- Problem-solving
- Comparison/alternative
"""
 
 
# ============================================================================
# LAYER 3: DEEP RESEARCH PROMPTS
# ============================================================================
 
def evidence_extraction_prompt(content: str, keyword: str) -> str:
    """Extract facts and evidence from content."""
    return f"""
Extract key facts, statistics, and evidence from this content.
 
Keyword: {keyword}
Content:
{content[:2000]}
 
Return JSON with extracted evidence:
{{
  "evidence_items": [
    {{
      "claim": "specific fact/statistic",
      "evidence_type": "statistic/quote/example/case-study",
      "source_credibility_markers": ["marker1", "marker2"],
      "context": "context in which claim appears"
    }}
  ],
  "key_concepts": ["concept1", "concept2"],
  "definitions": {{"term": "definition"}},
  "statistics": {{"stat_name": value}},
  "controversies": ["controversial_point"],
  "gaps": ["missing_information"]
}}
 
Focus on facts that directly support the keyword topic.
"""
 
 
def knowledge_synthesis_prompt(evidence_items: str, keyword: str) -> str:
    """Synthesize evidence into structured knowledge."""
    return f"""
Synthesize the following evidence into structured knowledge.
 
Keyword: {keyword}
Evidence:
{evidence_items[:2000]}
 
Return JSON knowledge structure:
{{
  "entities": [
    {{"name": "entity", "type": "person/concept/product", "importance": "high/medium/low"}}
  ],
  "relationships": [
    {{"from": "entity1", "to": "entity2", "relation": "type of relationship"}}
  ],
  "key_concepts": ["concept1", "concept2"],
  "concept_hierarchy": {{"parent_concept": ["sub1", "sub2"]}},
  "definitions": {{"term": "definition"}},
  "examples": {{"concept": ["example1", "example2"]}},
  "statistics": {{"stat_name": "stat_value"}},
  "controversies": [
    {{"issue": "description", "perspectives": ["perspective1", "perspective2"]}}
  ]
}}
"""
