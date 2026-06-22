"""
services/seo_service.py
 
SEO analysis and optimization service.
"""
 
from typing import Dict, Any, List
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class SEOService:
    """SEO analysis and metrics."""
    
    def calculate_keyword_density(self, text: str, keyword: str) -> float:
        """Calculate keyword density percentage."""
        words = text.lower().split()
        keyword_count = sum(1 for w in words if keyword.lower() in w)
        return (keyword_count / len(words) * 100) if words else 0
    
    def analyze_readability(self, text: str) -> Dict[str, Any]:
        """Analyze content readability."""
        sentences = text.split('.')
        words = text.split()
        
        return {
            "word_count": len(words),
            "sentence_count": len(sentences),
            "avg_words_per_sentence": len(words) / len(sentences) if sentences else 0,
            "reading_time_minutes": len(words) // 200,
        }
    
    def generate_meta_description(self, title: str, content: str) -> str:
        """Generate SEO meta description."""
        # First 155 characters of content
        return content[:155].strip() + "..."
    
    async def calculate_seo_score(self,
                                 article: str,
                                 keywords: List[str]) -> Dict[str, Any]:
        """Calculate overall SEO score."""
        scores = {
            "keyword_optimization": self._score_keyword_optimization(article, keywords),
            "readability": self._score_readability(article),
            "structure": self._score_structure(article),
            "length": self._score_length(article),
        }
        
        overall_score = sum(scores.values()) / len(scores)
        
        return {
            "overall_score": overall_score,
            "component_scores": scores,
            "recommendations": self._get_recommendations(scores),
        }
    
    def _score_keyword_optimization(self, article: str, keywords: List[str]) -> float:
        """Score keyword usage."""
        article_lower = article.lower()
        found_count = sum(1 for kw in keywords if kw.lower() in article_lower)
        return min(1.0, found_count / len(keywords)) if keywords else 0.5
    
    def _score_readability(self, article: str) -> float:
        """Score readability metrics."""
        readability = self.analyze_readability(article)
        word_count = readability["word_count"]
        
        if 800 <= word_count <= 3000:
            return 1.0
        elif word_count < 800:
            return 0.5
        else:
            return 0.7
    
    def _score_structure(self, article: str) -> float:
        """Score article structure."""
        heading_count = article.count('#')
        return min(1.0, heading_count / 5)
    
    def _score_length(self, article: str) -> float:
        """Score content length."""
        word_count = len(article.split())
        if word_count >= 1500:
            return 1.0
        elif word_count >= 800:
            return 0.8
        else:
            return 0.5
    
    def _get_recommendations(self, scores: Dict[str, float]) -> List[str]:
        """Generate SEO recommendations."""
        recommendations = []
        if scores["keyword_optimization"] < 0.8:
            recommendations.append("Improve keyword density")
        if scores["readability"] < 0.8:
            recommendations.append("Improve readability")
        if scores["structure"] < 0.8:
            recommendations.append("Add more headings")
        if scores["length"] < 0.8:
            recommendations.append("Increase content length")
        return recommendations
 
 
__all__ = [
    "GeminiService",
    "TavilyService",
    "WebsiteCrawlerS",
    "TrendDiscoveryService",
    "FactCheckingService",
    "SEOService",
]
 