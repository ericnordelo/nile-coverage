"""Integration plugins."""
from nile_coverage.vendor import cairo_coverage


class PytestCairoCoveragePlugin:
    def __init__(self, contracts_folder, xml=False):
        self.contracts_folder = contracts_folder
        self.xml = xml

    def pytest_sessionfinish(self):
        """
        Called after whole test run finished, right before
        returning the exit status to the system.
        """
        cairo_coverage.run_report(self.contracts_folder, self.xml)
