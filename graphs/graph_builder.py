"""
graphs/graph_builder.py
 
Complete LangGraph StateGraph construction.
Assembles all 18 nodes with proper edges, routing, and refinement loops.
"""
 
from typing import Literal
from langgraph.graph import StateGraph, END
from schemas.state import ResearchState
 
# Import all nodes
from nodes.layer1_context.input_normalizer import InputNormalizerNode
from nodes.layer1_context.website_style_analyzer import WebsiteStyleAnalyzerNode
from nodes.layer1_context.brand_voice_analyzer import BrandVoiceAnalyzerNode
from nodes.layer1_context.pincode_analyzer import PincodeAnalyzerNode
from nodes.layer1_context.trend_discovery import TrendDiscoveryNode
from nodes.layer2_planning.intent_analyzer import IntentAnalyzerNode
from nodes.layer2_planning.seo_expansion import SEOExpansionNode
from nodes.layer2_planning.research_planner import ResearchPlannerNode
from nodes.layer2_planning.search_query_planner import SearchQueryPlannerNode
from nodes.layer3_research.tavily_search import TavilySearchNode
from nodes.layer3_research.content_extraction import ContentExtractionNode
from nodes.layer3_research.evidence_synthesizer import EvidenceSynthesizerNode
from nodes.layer4_strategy.seo_strategist import SEOStrategistNode
from nodes.layer4_strategy.article_architect import ArticleArchitectNode
from nodes.layer5_writing.draft_writer import DraftWriterNode
from nodes.layer5_writing.fact_checker import FactCheckerNode
from nodes.layer5_writing.refinement import RefinementNode
from nodes.layer5_writing.final_formatter import FinalFormatterNode
 
from utils.logger import get_logger
 
logger = get_logger(__name__)
 
 
class GraphBuilder:
    """Builds the complete LangGraph state machine."""
    
    def __init__(self):
        self.graph = StateGraph(ResearchState)
        self._initialize_nodes()
        self._add_edges()
        self._add_conditional_edges()
    
    def _initialize_nodes(self):
        """Register all nodes with the graph."""
        
        # Layer 1: Context Intelligence
        self.graph.add_node("input_normalizer", self._node_input_normalizer)
        self.graph.add_node("website_style_analyzer", self._node_website_style_analyzer)
        self.graph.add_node("brand_voice_analyzer", self._node_brand_voice_analyzer)
        self.graph.add_node("pincode_analyzer", self._node_pincode_analyzer)
        self.graph.add_node("trend_discovery", self._node_trend_discovery)
        
        # Layer 2: Research Planning
        self.graph.add_node("intent_analyzer", self._node_intent_analyzer)
        self.graph.add_node("seo_expansion", self._node_seo_expansion)
        self.graph.add_node("research_planner", self._node_research_planner)
        self.graph.add_node("search_query_planner", self._node_search_query_planner)
        
        # Layer 3: Deep Research
        self.graph.add_node("tavily_search", self._node_tavily_search)
        self.graph.add_node("content_extraction", self._node_content_extraction)
        self.graph.add_node("evidence_synthesizer", self._node_evidence_synthesizer)
        
        # Layer 4: Content Strategy
        self.graph.add_node("seo_strategist", self._node_seo_strategist)
        self.graph.add_node("article_architect", self._node_article_architect)
        
        # Layer 5: Writing & Validation
        self.graph.add_node("draft_writer", self._node_draft_writer)
        self.graph.add_node("fact_checker", self._node_fact_checker)
        self.graph.add_node("refinement", self._node_refinement)
        self.graph.add_node("final_formatter", self._node_final_formatter)
        
        logger.info("All 18 nodes registered")
    
    def _add_edges(self):
        """Add linear edges between nodes."""
        
        # Set entry point
        self.graph.set_entry_point("input_normalizer")
        
        # Layer 1 → Layer 2 pipeline
        self.graph.add_edge("input_normalizer", "website_style_analyzer")
        self.graph.add_edge("website_style_analyzer", "brand_voice_analyzer")
        self.graph.add_edge("brand_voice_analyzer", "pincode_analyzer")
        self.graph.add_edge("pincode_analyzer", "trend_discovery")
        
        # Layer 2 planning
        self.graph.add_edge("trend_discovery", "intent_analyzer")
        self.graph.add_edge("intent_analyzer", "seo_expansion")
        self.graph.add_edge("seo_expansion", "research_planner")
        self.graph.add_edge("research_planner", "search_query_planner")
        
        # Layer 3 research
        self.graph.add_edge("search_query_planner", "tavily_search")
        self.graph.add_edge("tavily_search", "content_extraction")
        self.graph.add_edge("content_extraction", "evidence_synthesizer")
        
        # Layer 4 strategy
        self.graph.add_edge("evidence_synthesizer", "seo_strategist")
        self.graph.add_edge("seo_strategist", "article_architect")
        
        # Layer 5 writing
        self.graph.add_edge("article_architect", "draft_writer")
        self.graph.add_edge("draft_writer", "fact_checker")
        
        logger.info("Linear edges added")
    
    def _add_conditional_edges(self):
        """Add conditional routing for refinement loops."""
        
        # Fact-check routing: if not passed, go to refinement; else go to final_formatter
        self.graph.add_conditional_edges(
            "fact_checker",
            self._router_fact_check,
            {
                "refine": "refinement",
                "format": "final_formatter",
            }
        )
        
        # Refinement leads to final formatter
        self.graph.add_edge("refinement", "final_formatter")
        
        # Final formatter is end state
        self.graph.add_edge("final_formatter", END)
        
        logger.info("Conditional edges added")
    
    def _router_fact_check(self, state: ResearchState) -> Literal["refine", "format"]:
        """Route based on fact-check results."""
        fact_check_passed = state.get("fact_check_passed", False)
        if fact_check_passed:
            logger.info("Fact-check passed, proceeding to formatting")
            return "format"
        else:
            logger.info("Fact-check failed, proceeding to refinement")
            return "refine"
    
    def compile(self):
        """Compile the graph for execution."""
        compiled_graph = self.graph.compile(
            checkpointer=None,  # Add memory if needed: MemorySaver()
            interrupt_before=["fact_checker"],  # Interrupt points
            interrupt_after=["draft_writer"],
        )
        logger.info("Graph compiled successfully")
        return compiled_graph
    
    # =========================================================================
    # NODE IMPLEMENTATIONS
    # =========================================================================
    
    async def _node_input_normalizer(self, state: ResearchState) -> dict:
        """Execute InputNormalizerNode."""
        node = InputNormalizerNode()
        return await node.run(state)
    
    async def _node_website_style_analyzer(self, state: ResearchState) -> dict:
        """Execute WebsiteStyleAnalyzerNode."""
        node = WebsiteStyleAnalyzerNode()
        return await node.run(state)
    
    async def _node_brand_voice_analyzer(self, state: ResearchState) -> dict:
        """Execute BrandVoiceAnalyzerNode."""
        node = BrandVoiceAnalyzerNode()
        return await node.run(state)
    
    async def _node_pincode_analyzer(self, state: ResearchState) -> dict:
        """Execute PincodeAnalyzerNode."""
        node = PincodeAnalyzerNode()
        return await node.run(state)
    
    async def _node_trend_discovery(self, state: ResearchState) -> dict:
        """Execute TrendDiscoveryNode."""
        node = TrendDiscoveryNode()
        return await node.run(state)
    
    async def _node_intent_analyzer(self, state: ResearchState) -> dict:
        """Execute IntentAnalyzerNode."""
        node = IntentAnalyzerNode()
        return await node.run(state)
    
    async def _node_seo_expansion(self, state: ResearchState) -> dict:
        """Execute SEOExpansionNode."""
        node = SEOExpansionNode()
        return await node.run(state)
    
    async def _node_research_planner(self, state: ResearchState) -> dict:
        """Execute ResearchPlannerNode."""
        node = ResearchPlannerNode()
        return await node.run(state)
    
    async def _node_search_query_planner(self, state: ResearchState) -> dict:
        """Execute SearchQueryPlannerNode."""
        node = SearchQueryPlannerNode()
        return await node.run(state)
    
    async def _node_tavily_search(self, state: ResearchState) -> dict:
        """Execute TavilySearchNode."""
        node = TavilySearchNode()
        return await node.run(state)
    
    async def _node_content_extraction(self, state: ResearchState) -> dict:
        """Execute ContentExtractionNode."""
        node = ContentExtractionNode()
        return await node.run(state)
    
    async def _node_evidence_synthesizer(self, state: ResearchState) -> dict:
        """Execute EvidenceSynthesizerNode."""
        node = EvidenceSynthesizerNode()
        return await node.run(state)
    
    async def _node_seo_strategist(self, state: ResearchState) -> dict:
        """Execute SEOStrategistNode."""
        node = SEOStrategistNode()
        return await node.run(state)
    
    async def _node_article_architect(self, state: ResearchState) -> dict:
        """Execute ArticleArchitectNode."""
        node = ArticleArchitectNode()
        return await node.run(state)
    
    async def _node_draft_writer(self, state: ResearchState) -> dict:
        """Execute DraftWriterNode."""
        node = DraftWriterNode()
        return await node.run(state)
    
    async def _node_fact_checker(self, state: ResearchState) -> dict:
        """Execute FactCheckerNode."""
        node = FactCheckerNode()
        return await node.run(state)
    
    async def _node_refinement(self, state: ResearchState) -> dict:
        """Execute RefinementNode."""
        node = RefinementNode()
        return await node.run(state)
    
    async def _node_final_formatter(self, state: ResearchState) -> dict:
        """Execute FinalFormatterNode."""
        node = FinalFormatterNode()
        return await node.run(state)
 
 
def create_graph():
    """Factory function to create and compile the graph."""
    builder = GraphBuilder()
    return builder.compile()
 
 
__all__ = ["GraphBuilder", "create_graph"]
 