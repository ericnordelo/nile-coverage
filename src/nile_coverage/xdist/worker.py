"""xdist WorkerController overrides."""
import pytest

import nile_coverage.xdist.remote


class CustomRemoteHook:
    """RemoteHook extension to handle integration."""

    @pytest.hookimpl(trylast=True)
    def pytest_xdist_getremotemodule(self):
        return nile_coverage.xdist.remote
