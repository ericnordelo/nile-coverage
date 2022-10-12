"""Coverage command definition."""

import click
import pytest

from nile_coverage import logger
from nile_coverage.pytest_plugins.coverage import CoveragePlugin


@click.command()
@click.option("--mark", "-m", help="pytest mark")
def coverage():
    """Generate coverage report for Cairo Smart Contracts."""
    logger.info("\nGenerating coverage report")

    args = ["-p", "no:warnings"]

    if mark is not None:
        args += ["-m", mark]

    pytest.main(args, plugins=[CoveragePlugin()])
