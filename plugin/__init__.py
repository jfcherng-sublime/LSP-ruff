from __future__ import annotations

from LSP.plugin import register_plugin, unregister_plugin

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
    # Somehow "unregister_plugin" in "plugin_unloaded" doesn't seem to work for plugin update
    # I have to do it like this to make sure the plugin is re-registered.
    # Hence a newer version of the server will be downloaded and used.
    unregister_plugin(LspRuffPlugin)
    register_plugin(LspRuffPlugin)


def plugin_unloaded() -> None:
    """Executed when this plugin is unloaded."""
