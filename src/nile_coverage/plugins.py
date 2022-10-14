"""PyTest plugin to print coverage report."""
from nile_coverage.vendor import cairo_coverage


class CoveragePlugin:
    def __init__(self, contracts_folder, xml=False):
        self.contracts_folder = contracts_folder

    def pytest_sessionfinish(self):
        """
        Called after whole test run finished, right before
        returning the exit status to the system.
        """
        if xml:
            cairo_coverage.report_runs_xml(self.contracts_folder)
        else:
            cairo_coverage.report_runs(self.contracts_folder)

