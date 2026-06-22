# tests/unit/test_services.py
import pytest
from app.config import settings


def test_settings_load():
    """Test settings loading."""
    assert settings is not None
    assert hasattr(settings, "google_api_key")
    assert hasattr(settings, "tavily_api_key")


def test_settings_paths_exist():
    """Test that configured paths exist."""
    assert settings.output_dir.exists()
    assert settings.logs_dir.exists()