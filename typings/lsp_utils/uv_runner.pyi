from _typeshed import Incomplete
from pathlib import Path

__all__ = ['UvRunner']

class UvRunner:
    _storage_path: Incomplete
    _uv: str
    def __init__(self, storage_path: Path) -> None: ...
    def run_command(self, *args: str, cwd: str) -> None: ...
