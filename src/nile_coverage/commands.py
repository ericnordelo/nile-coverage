"""Coverage command definition."""

import click
import pytest

from nile_coverage import logger
from nile_coverage.plugins import CoveragePlugin


@click.command()
@click.option("--mark", "-m", help="Pytest mark wrapper.")
@click.option(
    "--single-thread", "-s", is_flag=True, help="Run the test suite in a single thread."
)
@click.option(
    "--contracts-folder",
    "-c",
    default="contracts",
    help="Specify contracts folder (default to 'contracts').",
)
@click.option(
    "--xml", is_flag=True, help="Create a coverage.xml report with Cobertura format."
)
def coverage(mark, single_thread, contracts_folder, xml):
    """Generate coverage report for Cairo Smart Contracts."""
    logger.info("\nGenerating coverage report")

    args = ["-p", "no:warnings"]

    if mark is not None:
        args += ["-m", mark]

    if single_thread:
        args += ["-n", "0"]

    pytest.main(args, plugins=[CoveragePlugin(contracts_folder, xml)])
