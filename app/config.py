"""
app/config.py

Central configuration management using Pydantic BaseSettings.
"""

from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables
ENV_PATH = Path(__file__).parent.parent / ".env"
load_dotenv(ENV_PATH, override=False)


class Settings(BaseSettings):
    """Application settings."""
    
    # ========================================================================
    # API KEYS
    # ========================================================================
    
    groq_api_key: str = ""
    tavily_api_key: str = ""
    
    # ========================================================================
    # LLM SETTINGS
    # ========================================================================
    
    groq_model: str = "llama-3.3-70b-versatile"
    groq_temperature: float = 0.7
    groq_max_tokens: int = 2048
    
    # ========================================================================
    # RESEARCH SETTINGS
    # ========================================================================
    
    max_search_results: int = 10
    max_content_sources: int = 5
    content_max_length: int = 4000
    fetch_timeout: float = 30.0
    
    # ========================================================================
    # ARTICLE SETTINGS
    # ========================================================================
    
    target_word_count: int = 1500
    min_word_count: int = 800
    max_word_count: int = 3000
    enforce_keyword_density: bool = True
    keyword_density_target: float = 1.5
    
    # ========================================================================
    # FACT-CHECKING
    # ========================================================================
    
    fact_check_enabled: bool = True
    confidence_threshold: float = 0.6
    require_sources: bool = True
    
    # ========================================================================
    # PATHS
    # ========================================================================
    
    project_root: Path = Path(__file__).parent.parent
    output_dir: Path = project_root / "outputs"
    cache_dir: Path = project_root / ".cache"
    logs_dir: Path = project_root / "logs"
    
    # ========================================================================
    # GRAPH SETTINGS
    # ========================================================================
    
    max_iterations: int = 10
    recursion_limit: int = 25
    graph_timeout_seconds: int = 300
    
    # ========================================================================
    # LOGGING
    # ========================================================================
    
    log_level: str = "INFO"
    verbose: bool = False
    
    class Config:
        env_file = str(ENV_PATH)
        case_sensitive = False
    
    def __init__(self, **data):
        super().__init__(**data)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)


settings = Settings()


