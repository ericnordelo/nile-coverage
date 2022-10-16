"""Utils for vendor packages."""

import os
from dataclasses import dataclass
from textwrap import wrap
from typing import Dict, List, Set

from starkware.starknet.compiler.compile import compile_starknet_files


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


def process_file(file: str):
    """Get relative path."""
    cwd = os.getcwd()
    if file.startswith(cwd):
        return file.removeprefix(cwd + "/")
    return file


def get_file_statements(files, cairo_path=None):
    """Get the statements from the filename."""
    if cairo_path is None:
        cairo_path = []

    statements = dict()
    cc = compile_starknet_files(files, cairo_path=cairo_path, debug_info=True)

    for pc in set(cc.program.debug_info.instruction_locations.keys()):
        instruct = cc.program.debug_info.instruction_locations[
            pc
        ].inst
        file = process_file(
            instruct.input_file.filename
        )
        while True:
            # If file is auto generated discard it.
            if "autogen" not in file:
                lines = list(
                    range(
                        instruct.start_line,
                        instruct.end_line + 1,
                    )
                )
                if not file in statements:
                    statements[file] = set()
                statements[file].update(lines)
            if (
                instruct.parent_location is not None
            ):  # Continue until we have last parent location.
                instruct = instruct.parent_location[0]
                file = process_file(instruct.input_file.filename)
            else:
                break

    return statements
