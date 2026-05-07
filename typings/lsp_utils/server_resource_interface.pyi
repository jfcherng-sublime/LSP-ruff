import abc
from abc import ABC, abstractmethod

__all__ = ['ServerStatus', 'ServerResourceInterface']

class ServerStatus:
    UNINITIALIZED: int
    ERROR: int
    READY: int

class ServerResourceInterface(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def needs_installation(self) -> bool: ...
    @abstractmethod
    def install_or_update(self) -> None: ...
    @abstractmethod
    def get_status(self) -> int: ...
    @property
    @abstractmethod
    def binary_path(self) -> str: ...
