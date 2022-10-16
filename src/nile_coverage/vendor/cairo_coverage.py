import os
from collections import defaultdict
from typing import Any, DefaultDict, Dict, List, Optional, Set

from starkware.cairo.lang.compiler.instruction import Instruction
from starkware.cairo.lang.compiler.program import ProgramBase
from starkware.cairo.lang.vm import cairo_runner
from starkware.cairo.lang.vm.builtin_runner import BuiltinRunner
from starkware.cairo.lang.vm.relocatable import MaybeRelocatable
from starkware.cairo.lang.vm.vm_core import RunContext, VirtualMachine

from nile_coverage import logger
from nile_coverage.vendor.reporters import TextReporter, XmlReporter
from nile_coverage.vendor.utils import process_file


def run_report(contracts_folder: str = "", xml: bool = False):
    logger.info("\nGenerating coverage report. This can take a minute...")

    if not os.path.isdir(contracts_folder):
        logger.info(
            f'\n\nNothing to report (couldn\'t find "{contracts_folder}" directory)'
        )

    report_dict = OverrideVm.covered()
    statements = OverrideVm.statements()

    if xml:
        reporter = XmlReporter(contracts_folder, statements, report_dict)
        reporter.report(outfile="coverage.xml")
    else:
        reporter = TextReporter(contracts_folder, statements, report_dict)
        reporter.report()


class OverrideVm(VirtualMachine):
    def __init__(
        self,
        program: ProgramBase,
        run_context: RunContext,
        hint_locals: Dict[str, Any],
        static_locals: Optional[Dict[str, Any]] = None,
        builtin_runners: Optional[Dict[str, BuiltinRunner]] = None,
        program_base: Optional[MaybeRelocatable] = None,
    ):
        super().__init__(
            program=program,
            run_context=run_context,
            hint_locals=hint_locals,
            static_locals=static_locals,
            builtin_runners=builtin_runners,
            program_base=program_base,
        )
        self.old_end_run = (
            super().end_run
        )  # Save the old end run function to wrap it afterwards.
        self.old_run_instruction = (
            super().run_instruction
        )  # Save the old run instruction function to wrap it afterwards.
        self.old_as_vm_exception = (
            super().as_vm_exception
        )  # Save the old vm as exception function to wrap it afterwards.
        self.touched_pcs: List[int] = []

    def run_instruction(self, instruction: Instruction):
        """Saves the current pc and runs the instruction."""
        self.touched_pcs.append(self.run_context.pc.offset)
        self.old_run_instruction(instruction=instruction)

    def end_run(self):
        """In case the run doesn't fail creates report coverage."""
        self.old_end_run()
        self.cover_file()

    def as_vm_exception(
        self,
        exc,
        with_traceback: bool = True,
        notes: Optional[List[str]] = None,
        hint_index: Optional[int] = None,
    ):
        """In case the run fails creates report coverage."""
        self.cover_file()
        return self.old_as_vm_exception(exc, with_traceback, notes, hint_index)

    @staticmethod
    def covered(
        val: DefaultDict[str, List[int]] = defaultdict(list)
    ) -> DefaultDict[str, list]:
        """To share the covered files between all the instances."""
        return val

    @staticmethod
    def statements(
        val: DefaultDict[str, List[int]] = defaultdict(list)
    ) -> DefaultDict[str, list]:
        """To share the lines of codes in files between all the instances."""
        return val

    def pc_to_line(
        self,
        pc,
        statements: DefaultDict[str, list],
        report_dict: DefaultDict[str, List[int]],
    ) -> None:
        """Converts the touched pcs to the line numbers of the original file and saves them."""
        should_update_report = (
            pc in self.touched_pcs
        )  # If the pc is not touched by the test don't report it.
        instruct = self.program.debug_info.instruction_locations[
            pc
        ].inst  # First instruction in the debug info.
        file = process_file(
            instruct.input_file.filename
        )  # Current analyzed file relative path.
        while True:
            if "autogen" not in file:  # If file is auto generated discard it.
                lines = list(
                    range(
                        instruct.start_line,
                        instruct.end_line + 1,
                    )
                )  # Get the lines touched.
                if should_update_report:
                    report_dict[file].extend(lines)
                statements[file].extend(lines)
            if (
                instruct.parent_location is not None
            ):  # Continue until we have last parent location.
                instruct = instruct.parent_location[0]
                file = process_file(instruct.input_file.filename)
            else:
                return

    def cover_file(
        self,
    ):
        """Add the coverage report in the report dict and all the lines of code."""
        if self.program.debug_info is not None:
            report_dict = self.__class__.covered()
            statements = self.__class__.statements()
            for pc in set(self.program.debug_info.instruction_locations.keys()):
                self.pc_to_line(pc=pc, report_dict=report_dict, statements=statements)


cairo_runner.VirtualMachine = OverrideVm
