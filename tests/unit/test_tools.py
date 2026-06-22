# tests/unit/test_tools.py
import pytest
from tools.extract_content import ContentExtractor


def test_extract_text_simple_html():
    """Test text extraction from simple HTML."""
    html = "<p>Hello World</p>"
    text = ContentExtractor.extract_text(html)
    assert "Hello" in text
    assert "World" in text


def test_extract_metadata():
    """Test metadata extraction."""
    html = """
    <html>
    <head>
        <title>Test Page</title>
        <meta name="description" content="Test description">
    </head>
    </html>
    """
    metadata = ContentExtractor.extract_metadata(html)
    assert metadata.get("title") == "Test Page"
    assert metadata.get("description") == "Test description"


def test_html_to_markdown_empty():
    """Test markdown conversion of empty HTML."""
    html = ""
    markdown = ContentExtractor.html_to_markdown(html)
    assert markdown == ""