# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
import asyncio
from main import SEOContentEngine

app = FastAPI(title="SEO Content Engine")


class ResearchRequest(BaseModel):
    """Research request model."""
    keyword: str
    website_url: str
    pincode: str


class ResearchResponse(BaseModel):
    """Research response model."""
    success: bool
    final_article: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    sources: Optional[list] = None
    error: Optional[str] = None


@app.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest) -> ResearchResponse:
    """Generate article via research pipeline."""
    try:
        engine = SEOContentEngine()
        result = await engine.generate_article(
            keyword=request.keyword,
            website_url=request.website_url,
            pincode=request.pincode,
        )
        return ResearchResponse(**result)
    except Exception as e:
        return ResearchResponse(success=False, error=str(e))


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}