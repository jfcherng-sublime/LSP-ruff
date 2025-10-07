from __future__ import annotations

import re
from functools import cached_property

import sublime

from .constants import PACKAGE_NAME, PLATFORM_ARCH


class VersionManager:
    # https://github.com/astral-sh/ruff
    DOWNLOAD_URL_TEMPLATE = "https://github.com/astral-sh/ruff/releases/download/{version}/{tarball_name}"

    TARBALL_NAMES = {
        "linux_arm64": "ruff-aarch64-unknown-linux-gnu.tar.gz",
        "linux_x64": "ruff-x86_64-unknown-linux-gnu.tar.gz",
        "osx_arm64": "ruff-aarch64-apple-darwin.tar.gz",
        "osx_x64": "ruff-x86_64-apple-darwin.tar.gz",
        "windows_x64": "ruff-x86_64-pc-windows-msvc.zip",
        "windows_x86": "ruff-i686-pc-windows-msvc.zip",
    }
    """`platform_arch`-specific tarball names for the server."""
    THIS_TARBALL_NAME = TARBALL_NAMES[PLATFORM_ARCH]
    """The tarball name for the current platform architecture."""

    TARBALL_BIN_PATHS = {
        "linux_arm64": "ruff-aarch64-unknown-linux-gnu/ruff",
        "linux_x64": "ruff-x86_64-unknown-linux-gnu/ruff",
        "osx_arm64": "ruff-aarch64-apple-darwin/ruff",
        "osx_x64": "ruff-x86_64-apple-darwin/ruff",
        "windows_x64": "ruff.exe",
        "windows_x86": "ruff.exe",
    }
    """`platform_arch`-specific relative path of the server executable in the tarball."""
    THIS_TARBALL_BIN_PATH = TARBALL_BIN_PATHS[PLATFORM_ARCH]
    """The relative path of the server executable in the tarball for the current platform architecture."""

    @cached_property
    def server_version(self) -> str:
        """The server version without a "v" prefix."""
        if m := re.search(
            r"^ruff==(.+)",
            sublime.load_resource(f"Packages/{PACKAGE_NAME}/requirements.txt"),
            re.MULTILINE,
        ):
            return m.group(1).strip()
        raise ValueError("Failed to parse server version from requirements.txt")

    @cached_property
    def server_download_url(self) -> str:
        """The URL for downloading the server tarball."""
        return self.DOWNLOAD_URL_TEMPLATE.format(version=self.server_version, tarball_name=self.THIS_TARBALL_NAME)

    @cached_property
    def server_download_hash_url(self) -> str:
        """The URL for downloading the SHA256 hash of the server tarball."""
        return f"{self.server_download_url}.sha256"


version_manager = VersionManager()
