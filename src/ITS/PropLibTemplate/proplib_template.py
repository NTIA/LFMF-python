# TODO-TEMPLATE: Rename this file to your library name
from ctypes import *

from .proplib_loader import PropLibCDLL


# TODO-TEMPLATE: Rename to your library's main entry point, e.g., "P2108-1.0"
# Load the shared library.
lib = PropLibCDLL("PropLibTemplate-1.2")

# Define function prototypes
# TODO-TEMPLATE add function prototypes here. Each function should have
# its restype and argtypes defined. Examples:
# lib.AeronauticalStatisticalModel.restype = c_int
# lib.AeronauticalStatisticalModel.argtypes = (
#     c_double,
#     c_double,
#     c_double,
#     POINTER(c_double),
# )


def GetLibraryName() -> str:
    return __read_char_array(lib.GetLibraryNameCharArray())


def GetLibraryVersion() -> str:
    return __read_char_array(lib.GetLibraryVersionCharArray())


def __read_char_array(msg) -> str:
    try:
        msg_bytes = cast(msg, c_char_p).value
        if msg_bytes is None:
            raise RuntimeError("The TODO-TEMPLATE library returned an empty text response.")
        return msg_bytes.decode("utf-8")
    finally:
        lib.FreeCharArray(msg)
