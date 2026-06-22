# graphs/state_graph.py
from langgraph.graph import StateGraph
from schemas.state import ResearchState


def create_state_graph() -> StateGraph:
    """Create the base state graph."""
    return StateGraph(ResearchState)