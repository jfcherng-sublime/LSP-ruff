from __future__ import annotations

import re
from functools import cached_property

import sublime

from .constants import PACKAGE_NAME, PLATFORM_ARCH


class VersionManager:
    DOWNLOAD_URL_TEMPLATE = "https://github.com/astral-sh/ruff/releases/download/{version}/{tarball_name}"

    DOWNLOAD_TARBALL_NAMES = {
        "linux_arm64": "ruff-aarch64-unknown-linux-gnu.tar.gz",
        "linux_x64": "ruff-x86_64-unknown-linux-gnu.tar.gz",
        "osx_arm64": "ruff-aarch64-apple-darwin.tar.gz",
        "osx_x64": "ruff-x86_64-apple-darwin.tar.gz",
        "windows_x64": "ruff-x86_64-pc-windows-msvc.zip",
        "windows_x86": "ruff-i686-pc-windows-msvc.zip",
    }
    """`platform_arch`-specific tarball names for the ruff language server."""
    DOWNLOAD_TARBALL_NAME = DOWNLOAD_TARBALL_NAMES[PLATFORM_ARCH]

    DOWNLOAD_TARBALL_BIN_PATHS = {
        "linux_arm64": "ruff-aarch64-unknown-linux-gnu/ruff",
        "linux_x64": "ruff-x86_64-unknown-linux-gnu/ruff",
        "osx_arm64": "ruff-aarch64-apple-darwin/ruff",
        "osx_x64": "ruff-x86_64-apple-darwin/ruff",
        "windows_x64": "ruff.exe",
        "windows_x86": "ruff.exe",
    }
    """`platform_arch`-specific server executable relative path in the tarball."""
    DOWNLOAD_TARBALL_BIN_PATH = DOWNLOAD_TARBALL_BIN_PATHS[PLATFORM_ARCH]

    @cached_property
    def server_version(self) -> str:
        if m := re.match(
            r"^ruff==(.+)",
            sublime.load_resource(f"Packages/{PACKAGE_NAME}/requirements.txt"),
            re.MULTILINE,
        ):
            return m.group(1)
        return ""

    @property
    def server_download_url(self) -> str:
        return self.DOWNLOAD_URL_TEMPLATE.format(version=self.server_version, tarball_name=self.DOWNLOAD_TARBALL_NAME)

    @property
    def server_download_hash_url(self) -> str:
        return f"{self.server_download_url}.sha256"


version_manager = VersionManager()
