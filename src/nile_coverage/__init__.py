"""Nile plugin adding coverage reports for Cairo Smart Contracts."""
import logging

try:
    from importlib import metadata as importlib_metadata
except ImportError:
    import importlib_metadata

try:
    __version__ = importlib_metadata.version("nile-coverage")
except importlib_metadata.PackageNotFoundError:
    __version__ = None


__author__ = "Eric Nordelo"
__license__ = "MIT"
__url__ = "https://github.com/ericnordelo/nile-coverage"

logger = logging.getLogger(__name__)
