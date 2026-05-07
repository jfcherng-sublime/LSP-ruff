import abc
import sublime
from ..api_wrapper_interface import ApiWrapperInterface
from ..server_resource_interface import ServerResourceInterface
from LSP.plugin import ClientConfig, DottedDict, WorkspaceFolder
from abc import ABC, abstractmethod

__all__ = ['ClientHandlerInterface']

class ClientHandlerInterface(ABC, metaclass=abc.ABCMeta):
    package_name: str
    @classmethod
    @abstractmethod
    def setup(cls) -> None: ...
    @classmethod
    @abstractmethod
    def cleanup(cls) -> None: ...
    @classmethod
    @abstractmethod
    def get_displayed_name(cls) -> str: ...
    @classmethod
    @abstractmethod
    def package_storage(cls) -> str: ...
    @classmethod
    @abstractmethod
    def get_additional_variables(cls) -> dict[str, str]: ...
    @classmethod
    @abstractmethod
    def get_additional_paths(cls) -> list[str]: ...
    @classmethod
    @abstractmethod
    def manages_server(cls) -> bool: ...
    @classmethod
    @abstractmethod
    def get_command(cls) -> list[str]: ...
    @classmethod
    @abstractmethod
    def binary_path(cls) -> str: ...
    @classmethod
    @abstractmethod
    def get_server(cls) -> ServerResourceInterface | None: ...
    @classmethod
    @abstractmethod
    def get_binary_arguments(cls) -> list[str]: ...
    @classmethod
    @abstractmethod
    def read_settings(cls) -> tuple[sublime.Settings, str]: ...
    @classmethod
    @abstractmethod
    def on_settings_read(cls, settings: sublime.Settings) -> bool: ...
    @classmethod
    @abstractmethod
    def is_allowed_to_start(cls, window: sublime.Window, initiating_view: sublime.View, workspace_folders: list[WorkspaceFolder], configuration: ClientConfig) -> str | None: ...
    @abstractmethod
    def on_ready(self, api: ApiWrapperInterface) -> None: ...
    @abstractmethod
    def on_settings_changed(self, settings: DottedDict) -> None: ...
