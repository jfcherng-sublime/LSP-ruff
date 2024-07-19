from __future__ import annotations

import os
import re
from typing import Any

import sublime
from LSP.plugin import DottedDict
from lsp_utils.pip_client_handler import PipClientHandler

from .constants import PACKAGE_NAME
from .log import log_warning
from .template import load_string_template


class LspRuffPlugin(PipClientHandler):
    package_name = PACKAGE_NAME
    requirements_txt_path = "requirements.txt"
    server_filename = "ruff"

    server_version = ""
    """The version of the language server."""

    @classmethod
    def should_ignore(cls, view: sublime.View) -> bool:
        return bool(
            # SublimeREPL views
            view.settings().get("repl")
            # syntax test files
            or os.path.basename(view.file_name() or "").startswith("syntax_test")
        )

    @classmethod
    def setup(cls) -> None:
        super().setup()

        cls.server_version = cls.parse_server_version()

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
        lock_file_content = sublime.load_resource(f"Packages/{PACKAGE_NAME}/requirements.txt")
        return m.group(1) if (m := re.search(r"^ruff==(.*)", lock_file_content, flags=re.MULTILINE)) else ""
