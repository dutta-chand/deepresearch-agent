"""
nodes/layer5_writing/final_formatter.py
"""
 
from typing import Dict, Any
from datetime import datetime
from schemas.state import ResearchState, FinalArticle, ArticleMetadata
from services.seo_service import SEOService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class FinalFormatterNode:
    """Format final article with metadata and citations."""
    
    def __init__(self):
        self.seo_service = SEOService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Format final article."""
        try:
            draft_article = state.get("draft_article", "")
            keyword = state["keyword"]
            sources = state.get("raw_sources", [])
            evidence = state.get("evidence_collection", {})
            
            # Calculate metadata
            readability = self.seo_service.analyze_readability(draft_article)
            seo_metrics = await self.seo_service.calculate_seo_score(
                draft_article,
                [keyword]
            )
            
            metadata: ArticleMetadata = {
                "word_count": readability.get("word_count", 0),
                "reading_time_minutes": readability.get("reading_time_minutes", 0),
                "keyword_density": self.seo_service.calculate_keyword_density(
                    draft_article, keyword
                ),
                "sources_cited": len(sources),
                "estimated_seo_score": seo_metrics.get("overall_score", 0.7),
                "generated_at": datetime.now().isoformat(),
            }
            
            final_article: FinalArticle = {
                "title": f"Guide to {keyword}",
                "content": draft_article,
                "metadata": metadata,
                "sources_cited": sources[:5],
                "evidence_used": evidence.get("high_quality_evidence", []),
                "confidence_score": 0.85,
                "ready_to_publish": True,
            }
            
            return {
                "final_article": final_article,
                "current_stage": "article_formatted",
            }
        except Exception as e:
            self.logger.error(f"Formatting failed: {e}")
            raise
 
 
__all__ = [
    "InputNormalizerNode",
    "WebsiteStyleAnalyzerNode",
    "BrandVoiceAnalyzerNode",
    "PincodeAnalyzerNode",
    "TrendDiscoveryNode",
    "IntentAnalyzerNode",
    "SEOExpansionNode",
    "ResearchPlannerNode",
    "SearchQueryPlannerNode",
    "TavilySearchNode",
    "ContentExtractionNode",
    "EvidenceSynthesizerNode",
    "SEOStrategistNode",
    "ArticleArchitectNode",
    "DraftWriterNode",
    "FactCheckerNode",
    "RefinementNode",
    "FinalFormatterNode",
]
 