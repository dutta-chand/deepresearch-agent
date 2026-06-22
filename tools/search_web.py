# tools/search_web.py
from services.tavily_service import TavilyService
from typing import List, Dict, Any


class WebSearcher:
    """Web search using Tavily."""

    def __init__(self):
        self.tavily = TavilyService()

    async def search(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Search the web."""
        results = await self.tavily.search(query, max_results=max_results)
        return results

    async def search_batch(self, queries: List[str]) -> List[Dict[str, Any]]:
        """Search multiple queries."""
        all_results = []
        for query in queries:
            results = await self.search(query)
            all_results.extend(results)
        return all_results