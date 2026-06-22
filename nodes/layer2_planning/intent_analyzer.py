"""
LAYER 2: RESEARCH PLANNING NODES
 
nodes/layer2_planning/intent_analyzer.py
"""
 
from typing import Dict, Any
from schemas.state import ResearchState, IntentProfile
from services.gemini_service import GeminiService
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class IntentAnalyzerNode:
    """Analyze user intent for keyword."""
    
    def __init__(self):
        self.gemini = GeminiService()
        self.logger = logger
    
    async def run(self, state: ResearchState) -> Dict[str, Any]:
        """Analyze keyword intent."""
        try:
            keyword = state["keyword"]
            
            intent_profile: IntentProfile = {
                "keyword": keyword,
                "search_intent": "informational",
                "intent_confidence": 0.85,
                "user_journey_stage": "awareness",
                "pain_points": [],
                "motivations": [],
                "information_needs": [],
            }
            
            return {
                "intent_profile": intent_profile,
                "current_stage": "intent_analyzed",
            }
        except Exception as e:
            self.logger.error(f"Intent analysis failed: {e}")
            raise
 
 