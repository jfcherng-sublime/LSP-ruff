import sublime
from .constants import SublimeKind as SublimeKind
from .css import css as css
from .promise import Promise as Promise
from .registry import LspWindowCommand as LspWindowCommand, windows as windows
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from enum import IntEnum
from typing import TypeVar

T = TypeVar('T')

class TreeItemCollapsibleState(IntEnum):
    NONE = 1
    COLLAPSED = 2
    EXPANDED = 3

class TreeItem:
    label: Incomplete
    kind: Incomplete
    description: Incomplete
    tooltip: Incomplete
    command_url: Incomplete
    collapsible_state: Incomplete
    id: Incomplete
    def __init__(self, label: str, kind: SublimeKind = ..., description: str = '', tooltip: str = '', command_url: str = '') -> None: ...
    def html(self, sheet_name: str, indent_level: int) -> str: ...

class Node:
    element: Incomplete
    tree_item: Incomplete
    indent_level: Incomplete
    child_ids: Incomplete
    is_resolved: bool
    def __init__(self, element: T, tree_item: TreeItem, indent_level: int = 0) -> None: ...

class TreeDataProvider(metaclass=ABCMeta):
    @abstractmethod
    def get_children(self, element: T | None) -> Promise[list[T]]: ...
    @abstractmethod
    def get_tree_item(self, element: T) -> TreeItem: ...

class TreeViewSheet(sublime.HtmlSheet):
    nodes: Incomplete
    root_nodes: Incomplete
    name: Incomplete
    data_provider: Incomplete
    header: Incomplete
    def __init__(self, id: int, name: str, data_provider: TreeDataProvider, header: str = '') -> None: ...
    def set_provider(self, data_provider: TreeDataProvider, header: str = '') -> None: ...
    def expand_item(self, id: str) -> None: ...
    def collapse_item(self, id: str) -> None: ...

def new_tree_view_sheet(window: sublime.Window, name: str, data_provider: TreeDataProvider, header: str = '', flags: sublime.NewFileFlags = ..., group: int = -1) -> TreeViewSheet | None: ...
def toggle_tree_item(window: sublime.Window, name: str, id: str, expand: bool) -> None: ...

class LspExpandTreeItemCommand(LspWindowCommand):
    def run(self, name: str, id: str) -> None: ...

class LspCollapseTreeItemCommand(LspWindowCommand):
    def run(self, name: str, id: str) -> None: ...
