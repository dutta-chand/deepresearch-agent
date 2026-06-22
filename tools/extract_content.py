# tools/extract_content.py
from markdownify import markdownify as md
from bs4 import BeautifulSoup
from typing import Tuple, Optional


class ContentExtractor:
    """Extract and parse webpage content."""

    @staticmethod
    def html_to_markdown(html: str, max_length: Optional[int] = None) -> str:
        """Convert HTML to markdown."""
        try:
            markdown = md(html, heading_style="atx")
            
            # Clean up whitespace
            lines = markdown.split("\n")
            clean_lines = [line.rstrip() for line in lines]
            markdown = "\n".join(clean_lines)
            
            # Remove excessive blank lines
            while "\n\n\n" in markdown:
                markdown = markdown.replace("\n\n\n", "\n\n")
            
            if max_length and len(markdown) > max_length:
                markdown = markdown[:max_length] + "\n... [truncated]"
            
            return markdown.strip()
        except Exception:
            return ""

    @staticmethod
    def extract_text(html: str) -> str:
        """Extract plain text from HTML."""
        try:
            soup = BeautifulSoup(html, "html.parser")
            for script in soup(["script", "style"]):
                script.decompose()
            return soup.get_text(separator=" ", strip=True)
        except Exception:
            return ""

    @staticmethod
    def extract_metadata(html: str) -> dict:
        """Extract metadata from HTML."""
        try:
            soup = BeautifulSoup(html, "html.parser")
            metadata = {}
            
            title_tag = soup.find("title")
            if title_tag:
                metadata["title"] = title_tag.get_text(strip=True)
            
            desc_tag = soup.find("meta", attrs={"name": "description"})
            if desc_tag:
                metadata["description"] = desc_tag.get("content", "")
            
            author_tag = soup.find("meta", attrs={"name": "author"})
            if author_tag:
                metadata["author"] = author_tag.get("content", "")
            
            return metadata
        except Exception:
            return {}