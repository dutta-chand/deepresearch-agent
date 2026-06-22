# tools/style_extractor.py
from bs4 import BeautifulSoup
from typing import Dict, Any


class StyleExtractor:
    """Extract style information from HTML."""

    @staticmethod
    def extract_headings(html: str) -> Dict[str, Any]:
        """Extract heading hierarchy."""
        soup = BeautifulSoup(html, "html.parser")
        headings = {
            "h1": len(soup.find_all("h1")),
            "h2": len(soup.find_all("h2")),
            "h3": len(soup.find_all("h3")),
        }
        return headings

    @staticmethod
    def extract_formatting(html: str) -> Dict[str, Any]:
        """Extract formatting usage."""
        soup = BeautifulSoup(html, "html.parser")
        return {
            "bold": len(soup.find_all("b")) + len(soup.find_all("strong")),
            "italic": len(soup.find_all("i")) + len(soup.find_all("em")),
            "lists": len(soup.find_all("ul")) + len(soup.find_all("ol")),
            "blockquotes": len(soup.find_all("blockquote")),
        }

    @staticmethod
    def extract_structure(html: str) -> Dict[str, Any]:
        """Extract page structure."""
        soup = BeautifulSoup(html, "html.parser")
        paragraphs = soup.find_all("p")
        
        paragraph_lengths = [len(p.text.split()) for p in paragraphs]
        avg_paragraph_length = (
            sum(paragraph_lengths) / len(paragraph_lengths)
            if paragraph_lengths
            else 0
        )
        
        return {
            "paragraph_count": len(paragraphs),
            "avg_paragraph_length": avg_paragraph_length,
            "total_sections": len(soup.find_all(["section", "article", "div"])),
        }