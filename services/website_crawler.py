import httpx
from bs4 import BeautifulSoup
from typing import Optional, Dict, Any
from utils.logger import get_logger
 
logger = get_logger(__name__)

class WebsiteCrawler:
    """Fetch and parse website content."""
    
    def __init__(self, timeout: float = 30.0):
        self.timeout = timeout
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
    
    async def fetch_website(self, url: str) -> Optional[str]:
        """Fetch website HTML."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=self.headers)
                return response.text
        except Exception as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return None
    
    def extract_text(self, html: str) -> str:
        """Extract text from HTML."""
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()
    
    def extract_structure(self, html: str) -> Dict[str, Any]:
        """Extract page structure."""
        soup = BeautifulSoup(html, 'html.parser')
        return {
            "headings": [h.text for h in soup.find_all(['h1', 'h2', 'h3'])],
            "paragraphs": len(soup.find_all('p')),
            "links": len(soup.find_all('a')),
            "images": len(soup.find_all('img')),
        }
 
 
