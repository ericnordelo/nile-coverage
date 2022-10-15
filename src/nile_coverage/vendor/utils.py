"""Utils for vendor packages."""

import os
from dataclasses import dataclass
from textwrap import wrap
from typing import Dict, List, Set


@dataclass
class CoverageFile:
    name: str  # Filename.
    covered: Set[int]  # Tested lines.
    statements: Set[int]  # Lines with code.
    precision: int = 1  # Decimals for %.

    @staticmethod
    def col_sizes(sizes=[]):
        """To share the column sizes between all the instances."""
        return sizes

    def __post_init__(self):
        """Finish initialization."""
        self.nb_statements = len(
            self.statements
        )  # Nb of lines with code in the cairo file.
        self.nb_covered = len(self.covered)  # Nb of lines tested.
        self.missed = sorted(list(self.statements - self.covered))  # Lines not tested.
        self.nb_missed = len(self.missed)  # Nb of lines not tested.
        self.pct_covered = (
            0
            if self.nb_statements == 0
            else (100 * self.nb_covered / self.nb_statements)
        )  # % of lines tested.
        self.pct_missed = (
            100
            if self.nb_statements == 0
            else (100 * self.nb_missed / self.nb_statements)
        )  # % of lines not tested.


class Headers:
    """Headers for the report table."""

    FILE: str = "File "
    FILE_INDEX: int = 0

    COVERED: str = "Covered(%) "
    COVERED_INDEX: int = 1

    MISSED: str = "Missed(%) "
    MISSED_INDEX: int = 2

    LINES_MISSED: str = "Lines missed"
    LINE_MISSED_INDEX: int = 3


def add_files_to_report(contracts_folder: str, report_dict):
    """Add zero coverage files to report."""
    for path, _, files in os.walk(contracts_folder):
        for name in files:
            f = os.path.join(path, name)
            if f not in report_dict and f.endswith(".cairo"):
                report_dict[f] = []


def get_file_lines_count(file):
    """Count the lines of a file."""
    return sum(1 for line in open(file))
