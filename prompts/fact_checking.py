def fact_check_prompt(article: str, evidence: str) -> str:
    """Verify claims in article."""
    return f"""
Fact-check this article against provided evidence.
 
ARTICLE:
{article[:2000]}
 
EVIDENCE PROVIDED:
{evidence[:2000]}
 
For each major claim in the article:
1. Identify the claim
2. Check if it's supported by the evidence
3. Identify any contradictions
4. Rate confidence (0-1)
 
Return JSON:
{{
  "claims_verified": [
    {{
      "claim": "the claim",
      "status": "verified/unverified/contradicted",
      "confidence": 0.85,
      "supporting_evidence": "from sources",
      "contradicting_evidence": "if any"
    }}
  ],
  "overall_verification_score": 0.90,
  "claims_needing_revision": ["claim1", "claim2"],
  "recommendations": ["recommendation1"]
}}
"""
 
 