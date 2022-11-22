"""Coverage command definition."""

import sys

import asyncclick as click
import pytest

from nile_coverage import logger
from nile_coverage.plugins import PytestCairoCoveragePlugin


@click.command()
@click.option("--mark", "-m", help="Pytest mark wrapper.")
@click.option(
    "--single-thread", "-s", is_flag=True, help="DEPRECATED OPTION."
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
    args = ["-p", "no:warnings"]

    if mark is not None:
        args += ["-m", mark]

    sys.exit(
        pytest.main(args, plugins=[PytestCairoCoveragePlugin(contracts_folder, xml)])
    )
