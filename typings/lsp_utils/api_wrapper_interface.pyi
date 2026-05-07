import abc
from abc import ABC, abstractmethod
from typing import Any, Callable

__all__ = ['ApiNotificationHandler', 'ApiRequestHandler', 'ApiWrapperInterface']

ApiNotificationHandler = Callable[[Any], None]
ApiRequestHandler = Callable[[Any, Callable[[Any], None]], None]

class ApiWrapperInterface(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def on_notification(self, method: str, handler: ApiNotificationHandler) -> None: ...
    @abstractmethod
    def on_request(self, method: str, handler: ApiRequestHandler) -> None: ...
    @abstractmethod
    def send_notification(self, method: str, params: Any) -> None: ...
    @abstractmethod
    def send_request(self, method: str, params: Any, handler: Callable[[Any, bool], None]) -> None: ...
