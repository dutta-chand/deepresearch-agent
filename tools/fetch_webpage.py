# tools/fetch_webpage.py
import httpx
from typing import Optional


class WebpageFetcher:
    """Fetch webpages with error handling."""

    def __init__(self, timeout: float = 30.0):
        self.timeout = timeout
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    async def fetch(self, url: str) -> Optional[str]:
        """Fetch webpage HTML."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=self.headers)
                response.raise_for_status()
                return response.text
        except Exception:
            return None

    async def fetch_multiple(self, urls: list) -> dict:
        """Fetch multiple URLs."""
        results = {}
        for url in urls:
            results[url] = await self.fetch(url)
        return results