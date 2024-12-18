from ctypes import *
from enum import IntEnum

from .proplib_loader import PropLibCDLL


class Result(Structure):
    # C Struct for library outputs
    _fields_ = [('A_btl__db', c_double),
                ('E__dBuVm', c_double),
                ('P_rx__dbm', c_double),
                ('method', c_int)]


# Load the shared library
lib = PropLibCDLL("LFMF-1.1")

# Define function prototypes
lib.LFMF.restype = c_int
lib.LFMF.argtypes = (
     c_double,
     c_double,
     c_double,
     c_double,
     c_double,
     c_double,
     c_double,
     c_double,
     c_int,
     POINTER(Result),
)


def LFMF(h_tx__meter: float, h_rx__meter: float, f__mhz: float, P_tx__watt: float,
         N_s: float, d__km: float, epsilon: float, sigma: float, pol: int) -> Result:
    """
    Compute the Low Frequency / Medium Frequency (LF/MF) propagation prediction

    :param    h_tx__meter: Height of the transmitter, in meters
    :param    h_rx__meter: Height of the receiver, in meters
    :param    f__mhz: Frequency, in MHz
    :param    P_tx__watt: Transmitter power, in watts
    :param    N_s: Surface refractivity, in N-Units
    :param    d__km: Path distance, in kilometers
    :param    epsilon: Relative permittivity (dimensionless)
    :param    sigma: Conductivity, in siemens per meter
    :param    pol: Polarization (enum value)

    :raises   ValueError: If any input parameter is not in its valid range.
    :raises   Exception: If an unknown error is encountered.

    :return:  In Result class.
    """
    result = Result()
    lib.err_check(
        lib.LFMF(
            c_double(h_tx__meter),
            c_double(h_rx__meter),
            c_double(f__mhz),
            c_double(P_tx__watt),
            c_double(N_s),
            c_double(d__km),
            c_double(epsilon),
            c_double(sigma),
            c_int(int(pol)),
            byref(result)
        )
    )

    return result
