from .generic_client_handler import GenericClientHandler
from .server_pip_resource import ServerPipResource
from .server_resource_interface import ServerResourceInterface
from typing_extensions import override

__all__ = ['PipClientHandler']

class PipClientHandler(GenericClientHandler):
    __server: ServerPipResource | None
    requirements_txt_path: str
    server_filename: str
    @classmethod
    def get_python_binary(cls) -> str: ...
    @classmethod
    @override
    def manages_server(cls) -> bool: ...
    @classmethod
    @override
    def get_server(cls) -> ServerResourceInterface | None: ...
    @classmethod
    @override
    def get_additional_paths(cls) -> list[str]: ...
