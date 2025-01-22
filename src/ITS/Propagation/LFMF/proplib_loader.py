"""
This module defines a class for interacting with a compiled shared library using
the ctypes library in Python. It manages loading the library, defining some
expected function prototypes, and parsing exit codes returned by the library functions.

The class `PropLibCDLL` is a thin wrapper for `ctypes.CDLL` which automatically
determines the appropriate shared library file based on the operating system and
provides methods for checking function return codes.

Classes:
--------
- PropLibCDLL: A subclass of `ctypes.CDLL` that manages loading a PropLib shared
    library and provides error checking for its functions.

Methods:
--------
- __init__(name):
    Initializes the `PropLibCDLL` instance by loading the specified library and
    setting up the expected function prototypes.

- get_lib_name(lib_name: str) -> str:
    Static method that constructs the full filename of the library based on the
    current platform.

- err_check(rtn_code: int) -> None:
    Checks the return code from the library's function call and raises a RuntimeError
    with the associated error message if the return code indicates an error.

Usage:
------
1. Create an instance of `PropLibCDLL` with the name of the shared library (without
   extension).
2. Call functions from the library using the instance.
3. Use `err_check` to handle error codes returned by those functions.

Example:
--------
```python
lib = PropLibCDLL("SomePropLibLibrary-1.0")
return_code = lib.SomeLibraryFunction()
lib.err_check(return_code)
```
"""

import platform
import struct
from ctypes import *
from pathlib import Path


class PropLibCDLL(CDLL):
    def __init__(self, name):
        full_name = self.get_lib_name(name)
        super().__init__(full_name)
        # Define expected function prototypes
        self.GetReturnStatusCharArray.restype = POINTER(c_char_p)
        self.GetReturnStatusCharArray.argtypes = (c_int,)
        self.FreeReturnStatusCharArray.restype = None
        self.FreeReturnStatusCharArray.argtypes = (POINTER(c_char_p),)

    @staticmethod
    def get_lib_name(lib_name: str) -> str:
        """Get the full filename of the library specified by `lib_name`.

        This function appends the correct file extension based on the current platform,
        and prepends the full absolute file path. The shared library is expected
        to exist in the same directory as this file.

        :param lib_name: The library name, with no extension or path, e.g., "P2108-1.0"
        :raises NotImplementedError: For platforms other than Windows, Linux, or macOS.
        :raises RuntimeError: On Windows, if unable to determine system architecture.
        :return: The full filename, including path and extension, of the library.
        """
        # Load the compiled library
        if platform.uname()[0] == "Windows":
            arch = struct.calcsize("P") * 8  # 32 or 64
            if arch == 64:
                lib_name += "-x64.dll"
            elif arch == 32:
                lib_name += "-x86.dll"
            else:
                raise RuntimeError(
                    "Failed to determine system architecture for DLL loading"
                )
        elif platform.uname()[0] == "Linux":
            lib_name += "-x86_64.so"
        elif platform.uname()[0] == "Darwin":
            lib_name += "-universal.dylib"
        else:
            raise NotImplementedError("Your OS is not yet supported")
        # Library should be in the same directory as this file
        lib_path = Path(__file__).parent / lib_name
        return str(lib_path.resolve())

    def err_check(self, rtn_code: int) -> None:
        """Parse the library's return code and raise an error if one occurred.

        Returns immediately for `rtn_code == 0`, otherwise retrieves the
        status message string from the underlying library and raises a
        RuntimeError with the status message.

        :param rtn_code: Integer return code from the underlying library.
        :raises RuntimeError: For any non-zero inputs.
        :return: None
        """
        if rtn_code == 0:
            return
        else:
            msg = self.GetReturnStatusCharArray(c_int(rtn_code))
            msg_str = cast(msg, c_char_p).value.decode("utf-8")
            self.FreeReturnStatusCharArray(msg)
            raise RuntimeError(msg_str)
