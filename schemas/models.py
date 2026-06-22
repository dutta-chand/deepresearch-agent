##layer1 

from typing import TypedDict, List, Dict, Any, Optional


class StyleProfile(TypedDict, total=False):
    tone: str
    vocabulary_level: str
    sentence_length_avg: float
    paragraph_length_avg: int
    heading_style: str
    structure_pattern: List[str]
    cta_style: str
    content_rhythm: str
    example_usage: bool
    story_telling: bool
    data_driven: bool


class BrandVoiceProfile(TypedDict, total=False):
    brand_personality: str
    values: List[str]
    key_messaging: List[str]
    communication_style: str
    authority_signals: List[str]
    differentiators: List[str]


class LocationProfile(TypedDict, total=False):
    pincode: str
    country: str
    state: str
    city: str
    locality: str
    district: str
    major_industries: List[str]
    area_type: str


class TrendProfile(TypedDict, total=False):
    location_trends: List[str]
    seasonal_trends: List[str]
    news_headlines: List[str]
    emerging_interests: List[str]


##layer2

class IntentProfile(TypedDict, total=False):
    keyword: str
    search_intent: str
    intent_confidence: float
    user_journey_stage: str
    pain_points: List[str]


class KeywordProfile(TypedDict, total=False):
    primary_keyword: str
    keyword_variations: List[str]
    long_tail_keywords: List[str]
    semantic_keywords: List[str]
    local_keywords: List[str]
    trending_keywords: List[str]


class ResearchPlan(TypedDict, total=False):
    focus_areas: List[str]
    primary_angle: str
    secondary_angles: List[str]
    evidence_requirements: List[str]
    citation_style: str

##layer3

class Source(TypedDict, total=False):
    url: str
    title: str
    source_type: str
    domain: str
    relevance_score: float
    publication_date: Optional[str]


class Evidence(TypedDict, total=False):
    claim: str
    source_url: str
    evidence_type: str
    confidence: float
    verification_status: str


class EvidenceCollection(TypedDict, total=False):
    total_sources: int
    primary_sources: List[Source]
    evidence_items: List[Evidence]


class KnowledgeBase(TypedDict, total=False):
    entities: List[Dict[str, Any]]
    relationships: List[Dict[str, Any]]
    key_concepts: List[str]
    statistics: Dict[str, Any]

##layer4

class SEOPlan(TypedDict, total=False):
    primary_keyword: str
    keyword_density_targets: Dict[str, float]
    local_seo_signals: List[str]


class ArticleOutline(TypedDict, total=False):
    title: str
    meta_description: str
    sections: List[Dict[str, Any]]


class WritingInstructions(TypedDict, total=False):
    tone_description: str
    voice_guidelines: List[str]
    local_context_instructions: str
    required_elements: List[str]

##layer5

class ArticleMetadata(TypedDict, total=False):
    word_count: int
    estimated_seo_score: float
    style_adherence_score: float
    fact_check_score: float


class FinalArticle(TypedDict, total=False):
    title: str
    slug: str
    meta_description: str
    content: str
    metadata: ArticleMetadata
    generated_at: str
    ready_to_publish: bool

    