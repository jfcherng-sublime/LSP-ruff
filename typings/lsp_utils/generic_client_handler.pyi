import sublime
from ._client_handler import ClientHandler
from .api_wrapper_interface import ApiWrapperInterface
from .server_resource_interface import ServerResourceInterface
from LSP.plugin import ClientConfig, DottedDict, WorkspaceFolder
from typing import Any
from typing_extensions import override

__all__ = ['GenericClientHandler']

class GenericClientHandler(ClientHandler):
    package_name: str
    @classmethod
    @override
    def setup(cls) -> None: ...
    @classmethod
    @override
    def cleanup(cls) -> None: ...
    @classmethod
    @override
    def get_displayed_name(cls) -> str: ...
    @classmethod
    @override
    def storage_path(cls) -> str: ...
    @classmethod
    @override
    def package_storage(cls) -> str: ...
    @classmethod
    @override
    def get_command(cls) -> list[str]: ...
    @classmethod
    @override
    def binary_path(cls) -> str: ...
    @classmethod
    @override
    def get_binary_arguments(cls) -> list[str]: ...
    @classmethod
    @override
    def read_settings(cls) -> tuple[sublime.Settings, str]: ...
    @classmethod
    @override
    def get_additional_variables(cls) -> dict[str, str]: ...
    @classmethod
    @override
    def get_additional_paths(cls) -> list[str]: ...
    @classmethod
    @override
    def manages_server(cls) -> bool: ...
    @classmethod
    @override
    def get_server(cls) -> ServerResourceInterface | None: ...
    @classmethod
    @override
    def on_settings_read(cls, settings: sublime.Settings) -> bool: ...
    @classmethod
    @override
    def is_allowed_to_start(cls, window: sublime.Window, initiating_view: sublime.View, workspace_folders: list[WorkspaceFolder], configuration: ClientConfig) -> str | None: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def on_ready(self, api: ApiWrapperInterface) -> None: ...
    @override
    def on_settings_changed(self, settings: DottedDict) -> None: ...
