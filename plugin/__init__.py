from __future__ import annotations

from .client import LspRuffPlugin

__all__ = (
    # ST: core
    "plugin_loaded",
    "plugin_unloaded",
    # ...
    "LspRuffPlugin",
)


def plugin_loaded() -> None:
    """Executed when this plugin is loaded."""
    LspRuffPlugin.setup()


def plugin_unloaded() -> None:
    """Executed when this plugin is unloaded."""
    LspRuffPlugin.cleanup()
