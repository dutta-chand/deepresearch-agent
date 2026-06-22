# tools/source_ranker.py
from typing import List, Dict, Any


class SourceRanker:
    """Rank sources by relevance and credibility."""

    @staticmethod
    def rank_by_relevance(
        sources: List[Dict[str, Any]], 
        query: str
    ) -> List[Dict[str, Any]]:
        """Rank sources by relevance to query."""
        query_words = set(query.lower().split())
        
        for source in sources:
            content = source.get("content", "").lower()
            matches = sum(1 for word in query_words if word in content)
            relevance = matches / len(query_words) if query_words else 0
            source["relevance_score"] = relevance
        
        return sorted(sources, key=lambda x: x.get("relevance_score", 0), reverse=True)

    @staticmethod
    def rank_by_domain_authority(sources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Rank sources by domain authority."""
        authority_scores = {
            "wikipedia.org": 95,
            "github.com": 90,
            "medium.com": 75,
            "dev.to": 70,
        }
        
        for source in sources:
            domain = source.get("domain", "")
            authority = authority_scores.get(domain, 50)
            source["domain_authority"] = authority
        
        return sorted(sources, key=lambda x: x.get("domain_authority", 0), reverse=True)

    @staticmethod
    def combine_rankings(sources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Combine multiple ranking factors."""
        for source in sources:
            relevance = source.get("relevance_score", 0)
            authority = source.get("domain_authority", 50) / 100
            combined = (relevance * 0.6) + (authority * 0.4)
            source["combined_score"] = combined
        
        return sorted(sources, key=lambda x: x.get("combined_score", 0), reverse=True)