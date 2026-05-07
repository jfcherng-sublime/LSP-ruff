import sublime_plugin
from .code_actions import CodeActionsOnFormatOnSaveTask as CodeActionsOnFormatOnSaveTask, CodeActionsOnSaveTask as CodeActionsOnSaveTask
from .formatting import FormatOnSaveTask as FormatOnSaveTask, WillSaveWaitTask as WillSaveWaitTask
from .lsp_task import LspTask as LspTask, LspTextCommandWithTasks as LspTextCommandWithTasks
from typing import Any
from typing_extensions import override

class LspSaveCommand(LspTextCommandWithTasks):
    @property
    @override
    def tasks(self) -> list[type[LspTask]]: ...
    @override
    def on_before_tasks(self) -> None: ...
    @override
    def on_tasks_completed(self, **kwargs: dict[str, Any]) -> None: ...
    def _trigger_on_pre_save_async(self) -> None: ...

class LspSaveAllCommand(sublime_plugin.WindowCommand):
    @override
    def run(self, only_files: bool = False) -> None: ...
