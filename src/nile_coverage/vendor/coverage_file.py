from dataclasses import dataclass
from typing import Dict, List, Set
import os

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
        self.nb_statements = len(
            self.statements
        )  # Nb of lines with code in the cairo file.
        self.nb_covered = len(self.covered)  # Nb of lines tested.
        self.missed = sorted(list(self.statements - self.covered))  # Lines not tested.
        self.nb_missed = len(self.missed)  # Nb of lines not tested.
        self.pct_covered = 0 if self.nb_statements == 0 else (
            100 * self.nb_covered / self.nb_statements
        )  # % of lines tested.
        self.pct_missed = 100 if self.nb_statements == 0 else (
            100 * self.nb_missed / self.nb_statements
        )  # % of lines not tested.


def add_files_to_report(contracts_folder: str, report_dict):
    for path, subdirs, files in os.walk(contracts_folder):
        for name in files:
            f = os.path.join(path, name)
            if f not in report_dict and f.endswith('.cairo'):
                report_dict[f] = []
