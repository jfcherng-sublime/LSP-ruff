from .server_resource_interface import ServerResourceInterface
from _typeshed import Incomplete
from pathlib import Path
from typing_extensions import override

__all__ = ['ServerPipResource']

class ServerPipResource(ServerResourceInterface):
    _pip_venv_manager: Incomplete
    _server_binary_filename: Incomplete
    _status: Incomplete
    def __init__(self, storage_path: str, package_name: str, requirements_path: str, server_binary_filename: str, python_binary: str) -> None: ...
    def _server_binary(self) -> Path: ...
    @property
    @override
    def binary_path(self) -> str: ...
    @override
    def get_status(self) -> int: ...
    @override
    def needs_installation(self) -> bool: ...
    @override
    def install_or_update(self) -> None: ...
