"""
LAYER 1: CONTEXT INTELLIGENCE NODES
 
nodes/layer1_context/input_normalizer.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState
from utils.validators import validate_pincode, validate_url
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class InputNormalizerNode:
    """Validate and normalize user inputs."""
    
    def __init__(self):
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """
        Normalize inputs.
        
        Args:
            state: ResearchState
            
        Returns:
            dict with validated inputs
        """
        try:
            keyword = state.get("keyword", "").strip()
            website_url = state.get("website_url", "").strip()
            pincode = state.get("pincode", "").strip()
            
            if not keyword:
                raise ValueError("Keyword is required")
            if not website_url:
                raise ValueError("Website URL is required")
            if not pincode:
                raise ValueError("Pincode is required")
            
            # Validate formats
            validate_url(website_url)
            validate_pincode(pincode)
            
            return {
                "keyword": keyword,
                "website_url": website_url,
                "pincode": pincode,
                "current_stage": "input_normalized",
            }
        except Exception as e:
            self.logger.error(f"Input validation failed: {e}")
            raise
 