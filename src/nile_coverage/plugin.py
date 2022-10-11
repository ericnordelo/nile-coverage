"""PyTest plugin to print coverage report."""
from cairo_coverage import cairo_coverage


class CoveragePlugin:
    def pytest_sessionfinish(self):
        """
        Called after whole test run finished, right before
        returning the exit status to the system.
        """
        cairo_coverage.report_runs()
