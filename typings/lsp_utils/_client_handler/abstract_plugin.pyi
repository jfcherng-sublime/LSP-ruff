import abc
import sublime
from ..api_wrapper_interface import ApiNotificationHandler, ApiRequestHandler, ApiWrapperInterface
from .interface import ClientHandlerInterface
from LSP.plugin import AbstractPlugin, ClientConfig, Session, WorkspaceFolder
from _typeshed import Incomplete
from abc import ABC
from typing import Any, Callable
from typing_extensions import override
from weakref import ref

__all__ = ['ClientHandler']

class ApiWrapper(ApiWrapperInterface):
    __plugin: Incomplete
    def __init__(self, plugin: ref[AbstractPlugin]) -> None: ...
    def __session(self) -> Session | None: ...
    @override
    def on_notification(self, method: str, handler: ApiNotificationHandler) -> None: ...
    @override
    def on_request(self, method: str, handler: ApiRequestHandler) -> None: ...
    @override
    def send_notification(self, method: str, params: Any) -> None: ...
    @override
    def send_request(self, method: str, params: Any, handler: Callable[[Any, bool], None]) -> None: ...

class ClientHandler(AbstractPlugin, ClientHandlerInterface, ABC, metaclass=abc.ABCMeta):
    @classmethod
    @override
    def name(cls) -> str: ...
    @classmethod
    @override
    def configuration(cls) -> tuple[sublime.Settings, str]: ...
    @classmethod
    @override
    def additional_variables(cls) -> dict[str, str]: ...
    @classmethod
    @override
    def needs_update_or_installation(cls) -> bool: ...
    @classmethod
    @override
    def install_or_update(cls) -> None: ...
    @classmethod
    @override
    def can_start(cls, window: sublime.Window, initiating_view: sublime.View, workspace_folders: list[WorkspaceFolder], configuration: ClientConfig) -> str | None: ...
    @classmethod
    @override
    def on_pre_start(cls, window: sublime.Window, initiating_view: sublime.View, workspace_folders: list[WorkspaceFolder], configuration: ClientConfig) -> str | None: ...
    @classmethod
    @override
    def setup(cls) -> None: ...
    @classmethod
    @override
    def cleanup(cls) -> None: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
