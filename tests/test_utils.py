import csv
from pathlib import Path
from typing import Optional

from ITS.Propagation import LFMF

# Test data is expected to exist in tests/data
TEST_DATA_DIR = Path(__file__).parent / "data"
ABSTOL__DB = 0.1  # Absolute tolerance, in dB, to ensure outputs match expected value

# Check if test data directory exists and is not empty
if not TEST_DATA_DIR.exists() or not any(TEST_DATA_DIR.iterdir()):
    raise RuntimeError(
        f"Test data is not available in {TEST_DATA_DIR}.\n Try running "
        + "`git submodule init` and `git submodule update` to clone the test data submodule."
    )


# Read CSV into dictionary and convert to specified data type
def _resolve_test_data_file(filename: str, data_dir: Optional[Path] = None) -> Path:
    """Resolve a CSV test-data file and raise a clear error when it is missing."""

    base_dir = data_dir or TEST_DATA_DIR
    file_path = base_dir / filename
    if not file_path.is_file():
        raise FileNotFoundError(
            f"Test data file '{filename}' was not found in '{base_dir}'. "
            "Clone or populate the test-data submodule before running data-backed tests."
        )
    return file_path


def read_csv_test_data(filename: str, data_dir: Optional[Path] = None):
    """Yield ``(*inputs, rtn, output)`` tuples from a simple numeric CSV file."""

    file_path = _resolve_test_data_file(filename, data_dir)
    with file_path.open(encoding="utf_8_sig", newline="") as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            # yields (*inputs, rtn, *outputs)
            yield tuple(map(float, row[:-5])), int(row[-5]), tuple(map(float, row[-4:]))


def test_LibraryName():
    name = LFMF.GetLibraryName()
    assert name == 'LFMF'


def test_LibraryVersion():
    version = LFMF.GetLibraryVersion()
    assert version == '1.2'