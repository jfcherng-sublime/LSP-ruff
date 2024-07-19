from __future__ import annotations

from pathlib import Path
from typing import Any

import sublime
from LSP.plugin import ClientConfig, DottedDict, WorkspaceFolder
from lsp_utils.pip_client_handler import PipClientHandler

from .constants import PACKAGE_NAME
from .log import log_warning
from .template import load_string_template


class LspRuffPlugin(PipClientHandler):
    package_name = PACKAGE_NAME
    requirements_txt_path = "requirements.txt"
    server_filename = "ruff"

    server_requirements_txt_path = "requirements.txt"
    """The path to the `requirements.txt` file of the language server. Relative to "Package Storage/PACKAGE_NAME/"."""
    server_version = ""
    """The version of the language server."""

    @classmethod
    def should_ignore(cls, view: sublime.View) -> bool:
        return bool(
            # ignore REPL views (https://github.com/sublimelsp/LSP-pyright/issues/343)
            view.settings().get("repl")
            # ignore Python-like syntax test files
            or view.substr(sublime.Region(0, 20)).startswith("# SYNTAX TEST ")
        )

    @classmethod
    def on_pre_start(
        cls,
        window: sublime.Window,
        initiating_view: sublime.View,
        workspace_folders: list[WorkspaceFolder],
        configuration: ClientConfig,
    ) -> str | None:
        super().on_pre_start(window, initiating_view, workspace_folders, configuration)

        cls.server_version = cls.parse_server_version()
        return None

    def on_settings_changed(self, settings: DottedDict) -> None:
        super().on_settings_changed(settings)

        self.update_status_bar_text()

    # -------------- #
    # custom methods #
    # -------------- #

    def update_status_bar_text(self, extra_variables: dict[str, Any] | None = None) -> None:
        if not (session := self.weaksession()):
            return

        variables: dict[str, Any] = {
            "server_version": self.server_version,
        }

        if extra_variables:
            variables.update(extra_variables)

        rendered_text = ""
        if template_text := str(session.config.settings.get("statusText") or ""):
            try:
                rendered_text = load_string_template(template_text).render(variables)
            except Exception as e:
                log_warning(f'Invalid "statusText" template: {e}')
        session.set_config_status_async(rendered_text)

    @classmethod
    def parse_server_version(cls) -> str:
        with open(Path(cls.package_storage()) / cls.server_requirements_txt_path, encoding="utf-8") as f:
            for line in f:
                if line.startswith("ruff=="):
                    return line[6:].strip()
        return ""
