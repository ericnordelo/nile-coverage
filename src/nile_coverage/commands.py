"""Coverage command definition."""

import click
import pytest

from nile_coverage import logger
from nile_coverage.pytest_plugins.coverage import CoveragePlugin


@click.command()
@click.option("--mark", "-m", help="Pytest mark wrapper.")
@click.option(
    "--single-thread", "-s", is_flag=True, help="Run the test suite in a single thread."
)
def coverage(mark, single_thread):
    """Generate coverage report for Cairo Smart Contracts."""
    logger.info("\nGenerating coverage report")

    args = ["-p", "no:warnings"]

    if mark is not None:
        args += ["-m", mark]

    if single_thread:
        args += ["-n", "0"]

    pytest.main(args, plugins=[CoveragePlugin()])
