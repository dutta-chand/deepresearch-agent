"""
services/gemini_service.py

Groq API integration for all LLM tasks.
"""

from typing import Dict, Any
from groq import Groq

from app.config import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class GeminiService:
    """LLM service for content generation, analysis, and refinement."""

    def __init__(self):
        self.client = Groq(
            api_key=settings.groq_api_key
        )
        self.temperature = settings.groq_temperature

    def _generate(self, prompt: str) -> str:
        """Send prompt to Groq and return response text."""

        response = self.client.chat.completions.create(
            model=settings.groq_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=settings.groq_temperature,
            max_tokens=settings.groq_max_tokens
        )

        return response.choices[0].message.content

    async def analyze_style(self, html_content: str) -> Dict[str, Any]:
        prompt = f"""
Analyze this website HTML and extract a detailed style profile.

Return JSON with:
tone, vocabulary_level, sentence_length_avg,
paragraph_length_avg, heading_hierarchy,
use_bullets, use_lists, structure_pattern,
cta_style, color_palette, formatting_emphasis,
content_rhythm.

HTML:
{html_content[:5000]}
"""

        return {"analysis": self._generate(prompt)}

    async def analyze_brand_voice(self, html_content: str) -> Dict[str, Any]:
        prompt = f"""
Analyze the brand voice and communication style from this website.

Extract:
brand_personality,
values,
key_messaging,
target_audience,
communication_style,
authority_signals,
differentiators.

HTML:
{html_content[:5000]}
"""

        return {"analysis": self._generate(prompt)}

    async def plan_research(
        self,
        keyword: str,
        location_context: str,
        trends: str
    ) -> Dict[str, Any]:

        prompt = f"""
Create a research plan for the keyword: {keyword}

Location Context:
{location_context}

Trends:
{trends}

Return JSON with:
- focus_areas
- primary_angle
- secondary_angles
- source_requirements
- local_context_integration
- evidence_requirements
"""

        return {"plan": self._generate(prompt)}

    async def generate_search_queries(
        self,
        keyword: str,
        research_plan: str
    ) -> Dict[str, Any]:

        prompt = f"""
Based on this keyword and research plan,
generate 8-12 specific search queries.

Keyword:
{keyword}

Research Plan:
{research_plan}

Return as JSON list of query strings.
"""

        return {"queries": self._generate(prompt)}

    async def extract_seo_keywords(
        self,
        keyword: str
    ) -> Dict[str, Any]:

        prompt = f"""
Expand the keyword: {keyword}

Return JSON with:
- keyword_variations
- long_tail_keywords
- semantic_keywords
- lsi_keywords
- question_keywords
"""

        return {"keywords": self._generate(prompt)}

    async def create_article_outline(
        self,
        keyword: str,
        style_profile: str,
        seo_plan: str
    ) -> Dict[str, Any]:

        prompt = f"""
Create an article outline for: {keyword}

Style to match:
{style_profile}

SEO Strategy:
{seo_plan}

Return JSON outline with sections,
subheadings, and word distribution.
"""

        return {"outline": self._generate(prompt)}

    async def draft_article(
        self,
        keyword: str,
        outline: str,
        evidence: str,
        style_profile: str,
        brand_voice: str,
        location_context: str
    ) -> Dict[str, Any]:

        prompt = f"""
Write an SEO-optimized article about: {keyword}

STRUCTURE:
{outline}

EVIDENCE:
{evidence}

STYLE PROFILE:
{style_profile}

BRAND VOICE:
{brand_voice}

LOCAL CONTEXT:
{location_context}

REQUIREMENTS:
- Original phrasing
- Natural keyword integration
- 1500-2000 words
- Markdown format
- Include section headings
"""

        return {"article": self._generate(prompt)}

    async def fact_check_claim(
        self,
        claim: str,
        sources: str
    ) -> Dict[str, Any]:

        prompt = f"""
Verify this claim against the provided sources.

CLAIM:
{claim}

SOURCES:
{sources}

Return JSON with:
- verification_status
- confidence
- evidence_count
- opposing_evidence_found
"""

        return {"verification": self._generate(prompt)}

    async def refine_article(
        self,
        article: str,
        feedback: str,
        style_profile: str
    ) -> Dict[str, Any]:

        prompt = f"""
Refine this article based on feedback.

ARTICLE:
{article}

FEEDBACK:
{feedback}

STYLE TO MAINTAIN:
{style_profile}

Return the refined article in markdown.
"""

        return {"refined": self._generate(prompt)}

    async def calculate_seo_score(
        self,
        article: str,
        keywords: str
    ) -> Dict[str, Any]:

        prompt = f"""
Evaluate the SEO quality of this article.

ARTICLE:
{article}

TARGET KEYWORDS:
{keywords}

Return JSON with:
- keyword_density
- heading_structure_score
- readability_score
- internal_linking_potential
- content_length_score
"""

        return {"seo_metrics": self._generate(prompt)}