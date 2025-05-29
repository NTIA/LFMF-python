import csv
from pathlib import Path

# Test data is expected to exist in tests/data
# TODO-TEMPLATE: Remove the '#' in the line below after adding your test data submodule
TEST_DATA_DIR = Path(__file__).parent  # / "data"
ABSTOL__DB = 0.1  # Absolute tolerance, in dB, to ensure outputs match expected value

# Check if test data directory exists and is not empty
if not TEST_DATA_DIR.exists() or not any(TEST_DATA_DIR.iterdir()):
    raise RuntimeError(
        f"Test data is not available in {TEST_DATA_DIR}.\n Try running "
        + "`git submodule init` and `git submodule update` to clone the test data submodule."
    )


# TODO-TEMPLATE: Update CSV reader based on test data CSV structure
def read_csv_test_data(filename: str):
    with open(TEST_DATA_DIR / filename) as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            # yields (*inputs, rtn, output)
            yield tuple(map(float, row[:-2])), int(row[-2]), float(row[-1])


"""
Read CSV into dictionary and convert to specified data type
For example: 
csv_to_test_dict("TestData.csv",
    {"rtn" : int, "input_1" : float, "input_2" : int, "output" : float}),
"""
def csv_to_test_dict(filename, type_dict):
    with open(TEST_DATA_DIR / filename, mode='r', encoding='utf_8_sig') as infile:
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
