def refinement_prompt(article: str, feedback: str, style_profile: str) -> str:
    """Polish article based on feedback."""
    return f"""
Refine and improve this article based on feedback.
 
ARTICLE:
{article}
 
FEEDBACK/ISSUES TO FIX:
{feedback}
 
MAINTAIN THIS STYLE:
{style_profile}
 
REFINEMENT REQUIREMENTS:
1. Fix all flagged issues
2. Improve clarity where needed
3. Strengthen weak claims with better evidence
4. Improve flow and transitions
5. Maintain original style and voice
6. Keep all formatting (markdown)
7. Don't remove facts, only strengthen them
8. Add elaboration where articles feel thin
 
Return the refined article in markdown format.
"""
 
 
