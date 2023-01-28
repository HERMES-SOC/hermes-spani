# Licensed under Apache License v2 - see LICENSE.rst
import os.path

from hermes_core import log
from hermes_spani.io.file_tools import read_file

try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")

__all__ = ["log", "read_file"]

INST_NAME = "spani"
INST_SHORTNAME = "spn"
INST_TARGETNAME = "SPANI"
INST_TO_SHORTNAME = {INST_NAME: INST_SHORTNAME}
INST_TO_TARGETNAME = {INST_NAME: INST_TARGETNAME}

_package_directory = os.path.dirname(os.path.abspath(__file__))
_data_directory = os.path.abspath(os.path.join(_package_directory, "data"))

log.info(f"hermes_spani version: {__version__}")
