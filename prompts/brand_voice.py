def brand_voice_prompt(html_content: str) -> str:
    """Extract brand voice and personality."""
    return f"""
Analyze the brand voice and communication style from this website.
 
Website Content:
{html_content[:3000]}
 
Return JSON with:
{{
  "brand_personality": "authoritative/friendly/innovative/professional",
  "values": ["value1", "value2", "value3"],
  "key_messaging": ["message1", "message2"],
  "target_audience": "description of ideal reader",
  "communication_style": "direct/narrative/educational/conversational",
  "authority_signals": ["credentials", "expertise", "social proof"],
  "differentiators": ["unique selling point 1", "unique selling point 2"],
  "brand_guarantees": ["guarantee 1", "guarantee 2"],
  "company_culture_signals": ["evidence of culture"],
  "ethics_and_stance": "description of brand's ethical position"
}}
 
Focus on the actual messaging, not company name. What makes this brand's voice unique?
"""


 