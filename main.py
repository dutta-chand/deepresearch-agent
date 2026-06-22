"""
main.py

SEO Content Engine - Main Entry Point

Usage:
    python main.py \
        --keyword "blockchain explained" \
        --website "https://example.com" \
        --pincode "94043"
"""

import asyncio
import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

from schemas.state import ResearchState
from graphs.graph_builder import create_graph
from app.config import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class SEOContentEngine:
    """Main orchestrator for the content generation pipeline."""
    
    def __init__(self):
        self.graph = create_graph()
        self.logger = logger
    
    async def generate_article(self,
                              keyword: str,
                              website_url: str,
                              pincode: str) -> Dict[str, Any]:
        """
        Generate a complete article.
        
        Args:
            keyword: Research topic
            website_url: Reference website for style
            pincode: Geographic location
        
        Returns:
            dict with final_article and metadata
        """
        
        try:
            # Initialize state
            initial_state: ResearchState = {
                "keyword": keyword,
                "website_url": website_url,
                "pincode": pincode,
                "current_stage": "initialized",
                "iteration_count": 0,
                "search_queries": [],
                "search_results": [],
                "raw_content": [],
                "raw_sources": [],
                "sources": [],
                "messages": [],
                "errors": [],
                "warnings": [],
                "execution_log": [],
                "start_time": datetime.now().isoformat(),
                "refinement_notes": [],
            }
            
            self.logger.info(f"Starting content generation for: {keyword}")
            self.logger.info(f"Reference website: {website_url}")
            self.logger.info(f"Pincode: {pincode}")
            
            # Execute graph
            result = await self.graph.ainvoke(
                initial_state,
                config={"recursion_limit": settings.recursion_limit}
            )

            print("\n=== RESULT KEYS ===")
            print(result.keys())

            print("\n=== ARTICLE CANDIDATES ===")
            for k, v in result.items():
                if isinstance(v, str) and len(v) > 100:
                    print(f"{k}: {len(v)} chars")
            
            # Extract generated article from graph state
            article_content = result.get("draft_article", "")

            final_article = {
                    "title": keyword,
                    "content": article_content,
                    "metadata": {
                        "word_count": len(article_content.split()),
                        "reading_time_minutes": max(1, len(article_content.split()) // 200),
                        "estimated_seo_score": "N/A"
                    }
            }
            
            print(f"\nArticle length: {len(article_content)}")
            print(article_content[:300])

            # Add end time
            end_time = datetime.now().isoformat()
            
            self.logger.info(f"Content generation complete")
            self.logger.info(f"Article word count: {final_article.get('metadata', {}).get('word_count', 0)}")
            self.logger.info(f"Fact-check passed: {result.get('fact_check_passed', False)}")
            
            return {
                "success": True,
                "final_article": final_article,
                "sources": result.get("sources", []),
                "metadata": {
                    "keyword": keyword,
                    "website": website_url,
                    "pincode": pincode,
                    "start_time": result.get("start_time"),
                    "end_time": end_time,
                    "total_duration_seconds": (
                        datetime.fromisoformat(end_time) -
                        datetime.fromisoformat(result.get("start_time", end_time))
                    ).total_seconds(),
                    "current_stage": result.get("current_stage", "complete"),
                    "iteration_count": result.get("iteration_count", 0),
                },
            }
        
        except Exception as e:
            self.logger.error(f"Content generation failed: {e}", exc_info=True)
            return {
                "success": False,
                "error": str(e),
            }
    
    async def stream_generation(self,
                               keyword: str,
                               website_url: str,
                               pincode: str,
                               callback=None):
        """
        Stream generation with callbacks for each stage.
        
        Args:
            keyword: Research topic
            website_url: Reference website
            pincode: Geographic location
            callback: Function called after each node (stage, state)
        """
        
        initial_state: ResearchState = {
            "keyword": keyword,
            "website_url": website_url,
            "pincode": pincode,
            "current_stage": "initialized",
            "iteration_count": 0,
            "search_queries": [],
            "search_results": [],
            "raw_content": [],
            "raw_sources": [],
            "sources": [],
            "messages": [],
            "errors": [],
            "warnings": [],
            "execution_log": [],
            "start_time": datetime.now().isoformat(),
            "refinement_notes": [],
        }
        
        # Stream graph execution
        async for step in self.graph.stream(
            initial_state,
            config={"recursion_limit": settings.recursion_limit}
        ):
            if callback:
                await callback(step)
            
            yield step


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="SEO Content Engine")
    parser.add_argument("--keyword", required=True, help="Research topic/keyword")
    parser.add_argument("--website", required=True, help="Reference website URL")
    parser.add_argument("--pincode", required=True, help="Geographic location code")
    parser.add_argument("--output", default="outputs", help="Output directory")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    # Create engine
    engine = SEOContentEngine()
    
    # Generate article
    result = asyncio.run(
        engine.generate_article(
            keyword=args.keyword,
            website_url=args.website,
            pincode=args.pincode,
        )
    )
    
    if not result["success"]:
        print(f"Error: {result['error']}")
        return 1
    
    # Save output
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if args.json:
        # Save as JSON
        output_file = output_dir / f"{args.keyword.replace(' ', '_')}.json"
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"Saved JSON to: {output_file}")
    else:
        # Save as Markdown
        article = result["final_article"]
        markdown_content = article.get("content", "")
        
        output_file = output_dir / f"{args.keyword.replace(' ', '_')}.md"
        with open(output_file, 'w') as f:
            f.write(f"# {article.get('title', args.keyword)}\n\n")
            f.write(markdown_content)
        
        print(f"✓ Article generated successfully")
        print(f"  Title: {article.get('title', 'N/A')}")
        print(f"  Word count: {article.get('metadata', {}).get('word_count', 'N/A')}")
        print(f"  Reading time: {article.get('metadata', {}).get('reading_time_minutes', 'N/A')} min")
        print(f"  SEO Score: {float(article.get('metadata', {}).get('estimated_seo_score', 0)):.2f}/1.0" if str(article.get('metadata', {}).get('estimated_seo_score', '')).replace('.', '', 1).isdigit() else f"  SEO Score: {article.get('metadata', {}).get('estimated_seo_score', 'N/A')}")
        print(f"  Saved to: {output_file}")
    
    return 0


if __name__ == "__main__":
    exit(main())


# ============================================================================
# PROGRAMMATIC USAGE EXAMPLE
# ============================================================================

"""
from main import SEOContentEngine
import asyncio

async def main():
    engine = SEOContentEngine()
    result = await engine.generate_article(
        keyword="machine learning for beginners",
        website_url="https://medium.com",
        pincode="94043"
    )
    
    if result["success"]:
        print(result["final_article"]["content"])
    else:
        print(f"Error: {result['error']}")

asyncio.run(main())
"""

__all__ = ["SEOContentEngine", "main"]