"""Integration plugins."""
import pytest
from xdist.workermanage import WorkerController

from nile_coverage.common import clean
from nile_coverage.vendor.reporters import run_report
from nile_coverage.xdist.worker import CustomRemoteHook


class PytestCairoCoveragePlugin:
    """Coverage Plugin."""

    def __init__(self, contracts_folder, xml=False):
        self.contracts_folder = contracts_folder
        self.xml = xml

    @pytest.hookimpl(hookwrapper=True)
    def pytest_sessionfinish(self):
        yield
        run_report(self.contracts_folder, self.xml)

        clean()


WorkerController.RemoteHook = CustomRemoteHook
