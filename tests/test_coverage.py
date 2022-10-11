"""Tests for coverage command."""

import logging

from click.testing import CliRunner

from nile_coverage import __name__
from nile_coverage.commands import coverage


def test_coverage(caplog):
    """Command tests."""
    caplog.set_level(logging.INFO, logger=__name__)

    CliRunner().invoke(coverage)

    assert "Generating coverage report" in caplog.text
    assert "Nothing to report" in caplog.text
