from ctypes import *
from enum import IntEnum

from .proplib_loader import PropLibCDLL


class Polarization(IntEnum):
    Horizontal = 0
    Vertical = 1


class SolutionMethod(IntEnum):
    FlatEarthCurveCorrection = 0
    ResidueSeries = 1


class c_LFMFResult(Structure):
    # C Struct for library outputs
    _fields_ = [
        ("A_btl__db", c_double),    # Basic transmission loss, in dB
        ("E__dBuVm", c_double),     # Electic field strength, in db(uV/m)
        ("P_rx__dbm", c_double),    # Received power, in dBm
        ("method", c_int),          # Solution method used
    ]


class LFMFResult(Structure):
    A_btl__db: float = None    # Basic transmission loss, in dB
    E__dBuVm: float = None     # Electic field strength, in db(uV/m)
    P_rx__dbm: float = None    # Received power, in dBm
    method: SolutionMethod = None       # Solution method used


# Load the shared library
lib = PropLibCDLL("LFMF-1.2")

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
    POINTER(c_LFMFResult),
)


def LFMF(
    h_tx__meter: float,
    h_rx__meter: float,
    f__mhz: float,
    P_tx__watt: float,
    N_s: float,
    d__km: float,
    epsilon: float,
    sigma: float,
    pol: Polarization,
) -> LFMFResult:
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
    result = c_LFMFResult()
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
            c_int(pol),
            byref(result),
        )
    )

    return __convertResultStruct(result)


def __convertResultStruct(c_result):
    result = LFMFResult
    result.A_btl__db = c_result.A_btl__db
    result.E__dBuVm = c_result.E__dBuVm
    result.P_rx__dbm = c_result.P_rx__dbm
    result.method = SolutionMethod(c_result.method)

    return result
