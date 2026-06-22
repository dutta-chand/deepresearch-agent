# utils/validators.py
from typing import Tuple
import re


def validate_url(url: str) -> Tuple[bool, str]:
    """Validate URL format."""
    pattern = r"^https?://"
    if re.match(pattern, url):
        return True, "Valid URL"
    return False, "Invalid URL format"


def validate_pincode(pincode: str) -> Tuple[bool, str]:
    """Validate pincode format."""
    pincode = pincode.strip()
    if re.match(r"^\d{5,6}$", pincode):
        return True, "Valid pincode"
    return False, "Invalid pincode format"


def validate_keyword(keyword: str) -> Tuple[bool, str]:
    """Validate keyword."""
    keyword = keyword.strip()
    if len(keyword) > 2 and len(keyword) < 100:
        return True, "Valid keyword"
    return False, "Keyword too short or too long"