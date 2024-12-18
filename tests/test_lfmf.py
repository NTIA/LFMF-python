import pytest

from ITS.Propagation import LFMF

from .test_utils import ABSTOL__DB, read_csv_test_data


@pytest.mark.parametrize(
    "inputs,rtn,expected",
    read_csv_test_data("LFMF_Examples.csv"),
)
def test_lfmf(inputs, rtn, expected):
    if rtn == 0:
        result = LFMF.LFMF(*inputs)
        assert result.A_btl__db == pytest.approx(expected[0], abs=ABSTOL__DB)
        assert result.E__dBuVm == pytest.approx(expected[1], abs=ABSTOL__DB)
        assert result.P_rx__dbm == pytest.approx(expected[2], abs=ABSTOL__DB)
        assert result.method == int(expected[3])
    else:
        with pytest.raises(RuntimeError):
            LFMF.LFMF(*inputs)
