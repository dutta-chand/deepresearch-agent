# utils/cache.py
from typing import Optional, Dict, Any
from pathlib import Path


class Cache:
    """Simple file-based cache."""

    def __init__(self, cache_dir: Path = None):
        self.cache_dir = cache_dir or Path(".cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get(self, key: str) -> Optional[Any]:
        """Get cached value."""
        cache_file = self.cache_dir / f"{key}.cache"
        if cache_file.exists():
            import json
            with open(cache_file, "r") as f:
                return json.load(f)
        return None

    def set(self, key: str, value: Any) -> None:
        """Set cached value."""
        cache_file = self.cache_dir / f"{key}.cache"
        import json
        with open(cache_file, "w") as f:
            json.dump(value, f)

    def clear(self) -> None:
        """Clear all cache."""
        import shutil
        shutil.rmtree(self.cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)