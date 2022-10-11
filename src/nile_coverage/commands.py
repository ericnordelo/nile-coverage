"""Coverage command definition."""

import click
import pytest

from nile_coverage import logger
from nile_coverage.pytest_plugins.coverage import CoveragePlugin


@click.command()
def coverage():
    """Generate coverage report for Cairo Smart Contracts."""
    logger.info("Generating coverage report")

    pytest.main(plugins=[CoveragePlugin()])
