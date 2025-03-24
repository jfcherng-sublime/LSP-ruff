from __future__ import annotations

import sublime

assert __package__

PACKAGE_NAME = __package__.partition(".")[0]

PLATFORM_ARCH = f"{sublime.platform()}_{sublime.arch()}"
SERVER_VERSION = "0.11.2"

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

DOWNLOAD_URL_TEMPLATE = "https://github.com/astral-sh/ruff/releases/download/{version}/{tarball_name}"
SERVER_DOWNLOAD_URL = DOWNLOAD_URL_TEMPLATE.format(version=SERVER_VERSION, tarball_name=DOWNLOAD_TARBALL_NAME)
SERVER_DOWNLOAD_HASH_URL = f"{SERVER_DOWNLOAD_URL}.sha256"
