from .uv_runner import UvRunner
from _typeshed import Incomplete
from pathlib import Path

__all__ = ['UvVenvManager']

class UvVenvManager:
    _source_resource_path: Incomplete
    _storage_path: Incomplete
    _package_storage: Incomplete
    _uv: UvRunner | None
    def __init__(self, package_name: str, project_toml_resource_path: str, storage_path: Path) -> None: ...
    @property
    def venv_path(self) -> Path: ...
    @property
    def venv_bin_path(self) -> Path: ...
    def needs_install_or_update(self) -> bool: ...
    def install(self) -> None: ...
