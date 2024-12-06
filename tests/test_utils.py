import csv
from pathlib import Path

# Test data is expected to exist in tests/data
TEST_DATA_DIR = Path(__file__).parent / "data"
ABSTOL__DB = 0.1  # Absolute tolerance, in dB, to ensure outputs match expected value


# TODO-TEMPLATE: Update CSV reader based on test data CSV structure
def read_csv_test_data(filename: str):
    with open(TEST_DATA_DIR / filename) as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            # yields (*inputs, rtn, output)
            yield tuple(map(float, row[:-2])), int(row[-2]), float(row[-1])


# TODO-TEMPLATE: Delete this dummy test and write your own in another file.
def test_always_pass():
    return
