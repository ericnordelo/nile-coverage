"""nile-coverage common module."""
import json
import shutil
from dataclasses import dataclass
from typing import DefaultDict, Set

from nile_coverage.utils import JsonEncoder

COVERAGE_DIRECTORY = "cairo-coverage"


@dataclass
class CairoTraceReport:
    """Wrapper for the coverage trace results."""

    lines: DefaultDict[str, set]
    covered_lines: DefaultDict[str, set]

    def __repr__(self):
        data = {
            "lines": self.lines,
            "covered_lines": self.covered_lines,
        }
        return json.dumps(data, indent=2, cls=JsonEncoder)


@dataclass
class CoverageFile:
    name: str  # Filename.
    covered: Set[int]  # Tested lines.
    statements: Set[int]  # Lines with code.

    def __post_init__(self):
        """Finish initialization."""
        # Number of lines with code in the cairo file.
        self.nb_statements = len(self.statements)
        # Number of lines tested.
        self.nb_covered = len(self.covered)


def clean():
    """Remove coverage files after execution."""
    shutil.rmtree(COVERAGE_DIRECTORY)
