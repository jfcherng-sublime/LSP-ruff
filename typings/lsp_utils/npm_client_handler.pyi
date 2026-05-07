import sublime
from .generic_client_handler import GenericClientHandler
from .server_npm_resource import ServerNpmResource
from .server_resource_interface import ServerResourceInterface
from LSP.plugin import ClientConfig, WorkspaceFolder
from typing_extensions import override

__all__ = ['NpmClientHandler']

class NpmClientHandler(GenericClientHandler):
    __server: ServerNpmResource | None
    server_directory: str
    server_binary_path: str
    skip_npm_install: bool
    @classmethod
    def minimum_node_version(cls) -> tuple[int, int, int]: ...
    @classmethod
    def required_node_version(cls) -> str: ...
    @classmethod
    @override
    def get_additional_variables(cls) -> dict[str, str]: ...
    @classmethod
    @override
    def get_additional_paths(cls) -> list[str]: ...
    @classmethod
    @override
    def get_command(cls) -> list[str]: ...
    @classmethod
    @override
    def get_binary_arguments(cls) -> list[str]: ...
    @classmethod
    @override
    def manages_server(cls) -> bool: ...
    @classmethod
    @override
    def get_server(cls) -> ServerResourceInterface | None: ...
    @classmethod
    @override
    def cleanup(cls) -> None: ...
    @classmethod
    @override
    def can_start(cls, window: sublime.Window, initiating_view: sublime.View, workspace_folders: list[WorkspaceFolder], configuration: ClientConfig) -> str | None: ...
    @classmethod
    def _server_directory_path(cls) -> str: ...
    @classmethod
    def _node_bin(cls) -> str: ...
    @classmethod
    def _node_env(cls) -> dict[str, str] | None: ...
