"""
schemas/state.py

Complete LangGraph state definitions using TypedDict.
This is the master state flowing through all nodes.

All data transformations flow through this single immutable dictionary.
"""

from typing import TypedDict, Optional, List, Dict, Any
from dataclasses import dataclass
from datetime import datetime


# ============================================================================
# LAYER 1: CONTEXT INTELLIGENCE OUTPUTS
# ============================================================================

class StyleProfile(TypedDict, total=False):
    """Website writing style profile."""
    tone: str                          # e.g., "professional", "casual", "technical"
    vocabulary_level: str              # "simple", "intermediate", "advanced"
    sentence_length_avg: float         # Average words per sentence
    paragraph_length_avg: int          # Average sentences per paragraph
    heading_hierarchy: Dict[str, Any]  # H1, H2, H3 patterns
    heading_style: str                 # "descriptive", "question", "how-to"
    use_bullets: bool
    use_numbered_lists: bool
    use_blockquotes: bool
    use_images: bool
    use_code_blocks: bool
    use_tables: bool
    color_palette: List[str]
    structure_pattern: List[str]       # Typical section order
    average_sections: int
    cta_style: str                     # Call-to-action pattern
    cta_frequency: int                 # CTAs per article
    opening_style: str
    closing_style: str
    content_rhythm: str                # "fast-paced", "steady", "slow"
    emojis_used: bool
    formatting_emphasis: str           # "bold", "italic", "code", "all"
    link_density: float                # Links per 100 words
    example_usage: bool
    story_telling: bool
    data_driven: bool


class BrandVoiceProfile(TypedDict, total=False):
    """Website brand voice characteristics."""
    brand_personality: str             # "friendly", "authoritative", "innovative"
    values: List[str]
    key_messaging: List[str]
    target_audience_description: str
    communication_style: str
    brand_guarantees: List[str]
    ethical_stance: str
    company_culture: str
    authority_signals: List[str]       # Trust builders used
    differentiators: List[str]
    brand_story_elements: List[str]


class LocationProfile(TypedDict, total=False):
    """Geographic and demographic context for pincode."""
    pincode: str
    country: str
    state: str
    city: str
    locality: str
    district: str
    population: int
    area_type: str                     # "urban", "suburban", "rural"
    climate: str
    language_primary: str
    language_secondary: List[str]
    economic_status: str               # "low", "middle", "high"
    literacy_rate: float
    internet_penetration: float
    major_industries: List[str]
    local_attractions: List[str]
    local_events: List[str]
    nearby_cities: List[str]
    transportation: List[str]
    local_government: str
    housing_type: str
    business_density: str


class TrendProfile(TypedDict, total=False):
    """Local and global trends relevant to pincode."""
    location_trends: List[str]         # Local trending topics
    seasonal_trends: List[str]         # Time-based trends
    category_trends: Dict[str, List[str]]  # By topic
    search_volume_signals: Dict[str, int]
    news_headlines: List[str]
    viral_topics: List[str]
    influencer_interests: List[str]
    cultural_events: List[str]
    economic_signals: List[str]
    social_signals: List[str]
    emerging_interests: List[str]


# ============================================================================
# LAYER 2: RESEARCH PLANNING OUTPUTS
# ============================================================================

class IntentProfile(TypedDict, total=False):
    """User intent analysis for the keyword."""
    keyword: str
    search_intent: str                 # "informational", "transactional", "navigational"
    intent_confidence: float
    user_journey_stage: str             # "awareness", "consideration", "decision"
    pain_points: List[str]
    motivations: List[str]
    desired_outcomes: List[str]
    information_needs: List[str]
    decision_criteria: List[str]


class KeywordProfile(TypedDict, total=False):
    """Expanded keyword and SEO terms."""
    primary_keyword: str
    keyword_variations: List[str]
    long_tail_keywords: List[str]
    semantic_keywords: List[str]
    lsi_keywords: List[str]
    related_searches: List[str]
    question_keywords: List[str]
    local_keywords: List[str]          # Keywords relevant to pincode
    trending_keywords: List[str]       # Trending locally
    keyword_difficulty: float
    search_volume: int
    cpc: float
    competition_level: str
    intent_alignment: Dict[str, float]


class ResearchPlan(TypedDict, total=False):
    """Overall research strategy."""
    focus_areas: List[str]
    primary_angle: str
    secondary_angles: List[str]
    depth_strategy: str
    source_requirements: Dict[str, int]  # {"academic": 2, "news": 3, etc.}
    research_duration_estimate: int
    quality_thresholds: Dict[str, float]
    local_context_integration: str
    brand_alignment_strategy: str
    seo_strategy_integration: str
    evidence_requirements: List[str]
    citation_style: str


# ============================================================================
# LAYER 3: DEEP RESEARCH OUTPUTS
# ============================================================================

class Source(TypedDict, total=False):
    """Individual source metadata."""
    url: str
    title: str
    source_type: str                  # "news", "blog", "academic", "official", "forum"
    domain: str
    domain_authority: float            # 0-100
    relevance_score: float             # 0-1
    freshness: str                     # "current", "recent", "archived"
    author: str
    publication_date: Optional[str]
    access_date: str
    language: str
    content_length: int                # characters
    credibility_indicators: List[str]


class Evidence(TypedDict, total=False):
    """Extracted factual claim with source."""
    claim: str
    source_url: str
    evidence_type: str                # "statistic", "quote", "example", "case-study"
    confidence: float                  # 0-1
    verification_status: str           # "verified", "unverified", "contradicted"
    supporting_evidence: List[str]
    opposing_evidence: List[str]
    context: str
    citation_format: str


class EvidenceCollection(TypedDict, total=False):
    """Aggregated evidence for article."""
    total_sources: int
    primary_sources: List[Source]
    secondary_sources: List[Source]
    evidence_items: List[Evidence]
    coverage_areas: Dict[str, int]    # topic → count
    confidence_scores: Dict[str, float]
    contradictions: List[Dict[str, Any]]
    high_quality_evidence: List[Evidence]
    local_evidence: List[Evidence]


class KnowledgeBase(TypedDict, total=False):
    """Structured knowledge graph."""
    entities: List[Dict[str, Any]]     # {name, type, importance}
    relationships: List[Dict[str, Any]]  # {from, to, relation_type}
    key_concepts: List[str]
    hierarchies: Dict[str, List[str]]  # concept → sub-concepts
    definitions: Dict[str, str]
    examples: Dict[str, List[str]]
    statistics: Dict[str, Any]
    trends: List[Dict[str, Any]]
    controversies: List[Dict[str, Any]]


# ============================================================================
# LAYER 4: CONTENT STRATEGY OUTPUTS
# ============================================================================

class SEOPlan(TypedDict, total=False):
    """SEO optimization strategy."""
    primary_keyword: str
    keyword_placement_strategy: Dict[str, Any]
    keyword_density_targets: Dict[str, float]
    on_page_elements: Dict[str, str]  # title, meta, h1, etc.
    internal_linking_plan: List[Dict[str, str]]
    external_linking_plan: List[Dict[str, str]]
    schema_markup: List[str]           # structured data types
    readability_targets: Dict[str, Any]
    content_freshness_signals: List[str]
    multimedia_strategy: Dict[str, Any]
    mobile_optimization_notes: List[str]
    page_speed_considerations: List[str]
    local_seo_signals: List[str]       # for pincode


class ArticleOutline(TypedDict, total=False):
    """Article structure plan."""
    title: str
    meta_description: str
    sections: List[Dict[str, Any]]     # {heading, subheadings, content_points}
    word_count_distribution: Dict[str, int]
    keyword_distribution: Dict[str, List[int]]
    cta_placement: List[int]           # section indexes
    section_purposes: Dict[str, str]
    tone_by_section: Dict[str, str]
    local_context_integration_points: List[int]
    evidence_requirements_by_section: Dict[str, List[str]]
    style_requirements: Dict[str, Any]


class WritingInstructions(TypedDict, total=False):
    """Detailed instructions for draft writer."""
    tone_description: str
    style_requirements: Dict[str, Any]
    voice_guidelines: List[str]
    structure_requirements: Dict[str, Any]
    keyword_instructions: Dict[str, Any]
    evidence_instructions: Dict[str, Any]
    local_context_instructions: str
    brand_alignment_checklist: List[str]
    prohibited_content: List[str]
    required_elements: List[str]
    target_reading_level: str
    formatting_requirements: Dict[str, Any]


# ============================================================================
# LAYER 5: FINAL OUTPUT
# ============================================================================

class ArticleMetadata(TypedDict, total=False):
    """Article performance metrics."""
    word_count: int
    reading_time_minutes: int
    flesch_kincaid_grade: float
    keyword_density: float
    unique_keywords_used: int
    sentences_count: int
    paragraphs_count: int
    headings_count: int
    internal_links: int
    external_links: int
    images_count: int
    estimated_seo_score: float
    local_relevance_score: float
    style_adherence_score: float
    fact_check_score: float
    sources_cited: int
    generation_time_seconds: float


class FinalArticle(TypedDict, total=False):
    """Complete finalized article."""
    title: str
    slug: str
    meta_description: str
    canonical_url: str
    content: str                       # Full markdown
    sections: List[Dict[str, Any]]
    html_content: Optional[str]
    metadata: ArticleMetadata
    sources_cited: List[Source]
    evidence_used: List[Evidence]
    optimization_notes: Dict[str, Any]
    fact_check_report: Dict[str, Any]
    refinement_log: List[Dict[str, Any]]
    generated_at: str
    confidence_score: float
    ready_to_publish: bool


# ============================================================================
# MASTER RESEARCH STATE (TypedDict)
# ============================================================================

class ResearchState(TypedDict, total=False):
    """
    Master state flowing through entire LangGraph.
    
    This is the single source of truth for all node transformations.
    Each node reads inputs and returns dict with fields to update.
    LangGraph merges updates back into this state.
    """
    
    # ========================================================================
    # INPUT LAYER
    # ========================================================================
    
    keyword: str                       # Primary research topic
    website_url: str                   # Reference website for style
    pincode: str                       # Geographic location code
    user_context: Optional[Dict[str, Any]]
    
    # ========================================================================
    # LAYER 1: CONTEXT INTELLIGENCE
    # ========================================================================
    
    style_profile: Optional[StyleProfile]
    brand_voice_profile: Optional[BrandVoiceProfile]
    location_profile: Optional[LocationProfile]
    trend_profile: Optional[TrendProfile]
    
    # ========================================================================
    # LAYER 2: RESEARCH PLANNING
    # ========================================================================
    
    intent_profile: Optional[IntentProfile]
    keyword_profile: Optional[KeywordProfile]
    research_plan: Optional[ResearchPlan]
    search_queries: List[str]          # Generated search queries
    
    # ========================================================================
    # LAYER 3: DEEP RESEARCH
    # ========================================================================
    
    search_results: List[Dict[str, Any]]
    raw_sources: List[Source]
    sources: List[Source]              # Ranked and filtered
    raw_content: List[Dict[str, Any]]
    evidence_collection: Optional[EvidenceCollection]
    knowledge_base: Optional[KnowledgeBase]
    
    # ========================================================================
    # LAYER 4: CONTENT STRATEGY
    # ========================================================================
    
    seo_plan: Optional[SEOPlan]
    article_outline: Optional[ArticleOutline]
    writing_instructions: Optional[WritingInstructions]
    content_strategy: Optional[Dict[str, Any]]
    
    # ========================================================================
    # LAYER 5: WRITING & VALIDATION
    # ========================================================================
    
    draft_article: Optional[str]
    draft_metadata: Optional[Dict[str, Any]]
    fact_check_results: Optional[Dict[str, Any]]
    fact_check_passed: bool
    seo_audit_results: Optional[Dict[str, Any]]
    style_audit_results: Optional[Dict[str, Any]]
    refinement_notes: List[str]
    final_article: Optional[FinalArticle]
    
    # ========================================================================
    # CONTROL & METADATA
    # ========================================================================
    
    current_stage: str
    iteration_count: int
    max_iterations: int
    messages: List[Dict[str, Any]]
    errors: List[str]
    warnings: List[str]
    execution_log: List[Dict[str, Any]]
    start_time: str
    end_time: Optional[str]
    total_duration_seconds: Optional[float]


# ============================================================================
# ADDITIONAL TYPE DEFINITIONS
# ============================================================================

@dataclass
class NodeInput:
    """Standard input for all nodes."""
    state: ResearchState
    context: Optional[Dict[str, Any]] = None


@dataclass
class NodeOutput:
    """Standard output from all nodes."""
    updates: Dict[str, Any]
    errors: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None


__all__ = [
    "ResearchState",
    "StyleProfile",
    "BrandVoiceProfile",
    "LocationProfile",
    "TrendProfile",
    "IntentProfile",
    "KeywordProfile",
    "ResearchPlan",
    "Source",
    "Evidence",
    "EvidenceCollection",
    "KnowledgeBase",
    "SEOPlan",
    "ArticleOutline",
    "WritingInstructions",
    "FinalArticle",
    "ArticleMetadata",
    "NodeInput",
    "NodeOutput",
]