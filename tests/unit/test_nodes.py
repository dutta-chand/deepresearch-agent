# tests/unit/test_nodes.py
import pytest
from schemas.state import ResearchState
from nodes.layer1_context.input_normalizer import InputNormalizerNode


@pytest.mark.asyncio
async def test_input_normalizer_valid():
    """Test input normalizer with valid inputs."""
    node = InputNormalizerNode()
    state = ResearchState(
        keyword="test",
        website_url="https://example.com",
        pincode="12345",
    )
    result = await node.run(state)
    assert result.get("keyword") == "test"
    assert result.get("current_stage") == "input_normalized"


@pytest.mark.asyncio
async def test_input_normalizer_missing_keyword():
    """Test input normalizer with missing keyword."""
    node = InputNormalizerNode()
    state = ResearchState(
        keyword="",
        website_url="https://example.com",
        pincode="12345",
    )
    with pytest.raises(ValueError):
        await node.run(state)