import csv
from pathlib import Path

# Test data is expected to exist in tests/data
TEST_DATA_DIR = Path(__file__).parent / "data"
ABSTOL__DB = 0.1  # Absolute tolerance, in dB, to ensure outputs match expected value

# Check if test data directory exists and is not empty
if not TEST_DATA_DIR.exists() or not any(TEST_DATA_DIR.iterdir()):
    raise RuntimeError(
        f"Test data is not available in {TEST_DATA_DIR}.\n Try running "
        + "`git submodule init` and `git submodule update` to clone the test data submodule."
    )


def read_csv_test_data(filename: str):
    with open(TEST_DATA_DIR / filename) as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            # yields (*inputs, rtn, *outputs)
            yield tuple(map(float, row[:-5])), int(row[-5]), tuple(map(float, row[-4:]))
