import csv
from pathlib import Path
from typing import Any, Optional

from ITS import PropLibTemplate

# Test data is expected to exist in tests/data
# TODO-TEMPLATE: Remove the '#' in the line below after adding your test data submodule
TEST_DATA_DIR = Path(__file__).parent  # / "data"
ABSTOL__DB = 0.001  # Absolute tolerance, in dB, to ensure outputs match expected value

# Check if test data directory exists and is not empty
if not TEST_DATA_DIR.exists() or not any(TEST_DATA_DIR.iterdir()):
    raise RuntimeError(
        f"Test data is not available in {TEST_DATA_DIR}.\n Try running "
        + "`git submodule init` and `git submodule update` to clone the test data submodule."
    )


# TODO-TEMPLATE: Update CSV reader based on test data CSV structure
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
            # yields (*inputs, rtn, output)
            yield tuple(map(float, row[:-2])), int(row[-2]), float(row[-1])


"""
Read CSV into dictionary and convert to specified data type
For example: 
csv_to_test_dict("TestData.csv",
    {"rtn" : int, "input_1" : float, "input_2" : int, "output" : float}),
"""
def csv_to_test_dict(
    filename: str,
    type_dict: dict[str, type[Any]],
    data_dir: Optional[Path] = None,
):
    """Yield dictionaries converted from CSV rows using the supplied type map."""

    file_path = _resolve_test_data_file(filename, data_dir)
    with file_path.open(encoding="utf_8_sig", newline="") as infile:
        reader = csv.reader(infile, skipinitialspace=True)
        keys = next(reader)
        for row in reader:
            test_dict = {}
            for key, value in zip(keys, row):
                if key in type_dict:
                    test_dict[key] = type_dict[key](value)
            yield test_dict


# TODO-TEMPLATE: Delete this dummy test and write your own in another file.
def test_always_pass():
    return


def test_LibraryName():
    name = PropLibTemplate.GetLibraryName()
    assert name == 'PropLibTemplate'


def test_LibraryVersion():
    version = PropLibTemplate.GetLibraryVersion()
    assert version == '1.2'