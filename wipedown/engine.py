"""WipeDown Engine - Clean, silent, structured API for agentic brain stacks.

This module provides the WipeDown class for programmatic use in other projects
like BrainFood, Cursor agents, custom LLM pipelines, etc.

Key properties:
- Completely silent (no print statements, no terminal output)
- Returns rich structured dicts with source, content, metadata, events
- Source URL prepended to content for easy human audit when saved as .md
- Backward compatible: existing wipe_text/wipe_url/CLI calls unchanged
- Optimized for import into other brain stacks without side effects
"""

from typing import Optional, Dict, Any

import datetime

class WipeDown:
    """
    Primary entrypoint for malleable, agent-friendly use of WipeDown.

    Example for BrainFood or other stacks:
        from wipedown import WipeDown

        firewall = WipeDown(model="qwen-3.6", api_url="http://127.0.0.1:8080/v1")
        result = firewall.wipe_url("https://example.com/article")
        
        print(result["status"])      # "success"
        print(result["source"])      # the url
        # result["content"] starts with "# Source: https://..." then the cleaned markdown
        # Safe to save to .md for human review or ingest into knowledge base.
    """

    def __init__(
        self,
        model: Optional[str] = None,
        api_url: Optional[str] = None,
        strict: bool = False,
    ):
        """
        Initialize the engine.
        - model / api_url: override env vars WIPEDOWN_MODEL / WIPEDOWN_API_URL
        - strict: if True, raise on signature match instead of logging
        """
        self.model = model
        self.api_url = api_url
        self.strict = strict

    def wipe_text(self, text: str) -> Dict[str, Any]:
        """
        Clean raw text. Always returns structured dict. Silent.
        """
        from .sanitizer import wipe_text as _wipe_text
        return _wipe_text(
            text,
            model=self.model,
            api_url=self.api_url,
            strict=self.strict,
            show_stream=False,   # never stream/print in engine mode
            structured=True
        )

    def wipe_url(self, url: str, content_only: bool = False) -> Dict[str, Any]:
        """
        Fetch + clean any URL (or file://). Returns structured dict. Silent.
        
        content_only is passed through but when structured=True the full
        Safety Report + cleaned content is returned (recommended for agents).
        Set content_only=True only if you want legacy extraction behavior.
        """
        from .sanitizer import wipe_url as _wipe_url
        return _wipe_url(
            url,
            model=self.model,
            api_url=self.api_url,
            strict=self.strict,
            content_only=content_only,
            show_stream=False,
            structured=True
        )

    def __repr__(self):
        return f"WipeDown(model={self.model!r}, api_url={self.api_url!r}, strict={self.strict})"
