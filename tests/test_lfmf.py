import csv
from pathlib import Path

import pytest

from ITS.Propagation import LFMF


# Test data is expected to exist in parent repository tests/data
TEST_DATA_DIR = (Path(__file__).parent.parent.parent.parent / "tests") / "data"
ABSTOL__DB = 1.0E-1  # Absolute tolerance, in dB, to ensure outputs match expected value


def read_csv_test_data(filename: str):
    with open(TEST_DATA_DIR / filename) as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            # yields (*inputs, rtn, *outputs)
            yield tuple(map(float, row[:-5])), int(row[-5]), tuple(map(float, row[-4:]))


@pytest.mark.parametrize(
    "inputs,rtn,expected",
    read_csv_test_data("LFMF_Examples.csv"),
)
def test_lfmf(inputs, rtn, expected):
    if rtn == 0:
        result = LFMF.LFMF(*inputs)
        assert result.A_btl__db == pytest.approx(expected[0], abs=ABSTOL__DB)
        assert result.E_dBuVm == pytest.approx(expected[1], abs=ABSTOL__DB)
        assert result.P_rx__dbm == pytest.approx(expected[2], abs=ABSTOL__DB)
        assert result.method == int(expected[3])
    else:
        with pytest.raises(RuntimeError):
            LFMF.LFMF(*inputs)
