from __future__ import annotations

import re

import sublime
from LSP.plugin import register_plugin, unregister_plugin

from .client import LspRuffPlugin
from .constants import PACKAGE_NAME
from .version_manager import version_manager

__all__ = (
    # ST: core
    "plugin_loaded",
    "plugin_unloaded",
    # ...
    "LspRuffPlugin",
)


def plugin_loaded() -> None:
    """Executed when this plugin is loaded."""
    register_plugin(LspRuffPlugin)

    version_manager.client_cls = LspRuffPlugin
    version_manager.server_version = _get_server_version()


def plugin_unloaded() -> None:
    """Executed when this plugin is unloaded."""
    unregister_plugin(LspRuffPlugin)


def _get_server_version() -> str:
    """The server version without a "v" prefix."""
    if m := re.search(
        r"^ruff==(.+)",
        sublime.load_resource(f"Packages/{PACKAGE_NAME}/requirements.txt"),
        re.MULTILINE,
    ):
        return m.group(1).strip()
    raise ValueError("Failed to parse server version from requirements.txt")
