# schemas/types.py
from typing import TypedDict, Optional, List, Dict, Any


class SearchResult(TypedDict, total=False):
    """Search result from Tavily."""
    url: str
    title: str
    snippet: str
    content: str
    score: float


class Source(TypedDict, total=False):
    """Citation source."""
    url: str
    title: str
    source_type: str
    domain: str
    domain_authority: float
    relevance_score: float
    access_date: str


class Evidence(TypedDict, total=False):
    """Extracted fact with source."""
    claim: str
    source_url: str
    evidence_type: str
    confidence: float
    verification_status: str


class ArticleMetadata(TypedDict, total=False):
    """Article metadata."""
    word_count: int
    reading_time_minutes: int
    keyword_density: float
    seo_score: float
    confidence_score: float
    generated_at: str