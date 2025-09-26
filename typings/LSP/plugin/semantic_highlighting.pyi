import sublime
from .core.registry import LspTextCommand as LspTextCommand
from _typeshed import Incomplete

class SemanticToken:
    region: Incomplete
    type: Incomplete
    modifiers: Incomplete
    def __init__(self, region: sublime.Region, type: str, modifiers: list[str]) -> None: ...

def copy(view: sublime.View, text: str) -> None: ...

class LspShowScopeNameCommand(LspTextCommand):
    capability: str
    def want_event(self) -> bool: ...
    def run(self, _: sublime.Edit) -> None: ...
    def on_navigate(self, link: str) -> None: ...
