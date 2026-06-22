# prompts/style_audit.py
def style_audit_prompt(article: str, style_profile: str) -> str:
    """Prompt for style audit."""
    return f"""
Audit this article for style consistency.

ARTICLE:
{article[:2000]}

STYLE PROFILE TO MATCH:
{style_profile}

Evaluate:
1. Tone consistency
2. Structure adherence
3. Vocabulary level match
4. Formatting consistency

Return JSON with scores and recommendations.
"""