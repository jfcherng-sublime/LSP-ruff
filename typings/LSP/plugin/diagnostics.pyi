import sublime
from .core.constants import DIAGNOSTIC_KINDS as DIAGNOSTIC_KINDS, REGIONS_INITIALIZE_FLAGS as REGIONS_INITIALIZE_FLAGS
from .core.protocol import Diagnostic as Diagnostic, DiagnosticSeverity as DiagnosticSeverity
from .core.settings import userprefs as userprefs
from .core.views import diagnostic_severity as diagnostic_severity, format_diagnostics_for_annotation as format_diagnostics_for_annotation

class DiagnosticsAnnotationsView:
    def __init__(self, view: sublime.View, config_name: str) -> None: ...
    def initialize_region_keys(self) -> None: ...
    def draw(self, diagnostics: list[tuple[Diagnostic, sublime.Region]]) -> None: ...
