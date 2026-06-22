# graphs/edges.py
from typing import Literal
from schemas.state import ResearchState


def router_fact_check(state: ResearchState) -> Literal["refine", "format"]:
    """Route based on fact-check results."""
    fact_check_passed = state.get("fact_check_passed", False)
    return "format" if fact_check_passed else "refine"


def router_needs_more_research(state: ResearchState) -> Literal["search", "analyze"]:
    """Route based on research gaps."""
    needs_research = state.get("needs_more_research", False)
    return "search" if needs_research else "analyze"


def router_research_complete(state: ResearchState) -> Literal["draft", "search"]:
    """Route based on research completion."""
    research_complete = state.get("research_complete", False)
    return "draft" if research_complete else "search"