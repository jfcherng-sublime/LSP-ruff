from _typeshed import Incomplete
from enum import IntEnum

Architecture: Incomplete

class ImageFileMachine(IntEnum):
    IMAGE_FILE_MACHINE_AMD64 = 34404
    IMAGE_FILE_MACHINE_ARM64 = 43620
    IMAGE_FILE_MACHINE_I386 = 332
    IMAGE_FILE_MACHINE_UNKNOWN = 0

MACHINE_NAMES: dict[ImageFileMachine, Architecture]

def get_host_arch() -> Architecture: ...
