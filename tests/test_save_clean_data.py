import os
import pandas as pd
import pytest
from proj_ss.config import BLD

@pytest.fixture
def output_file_path():
    """Returns the expected file path of the produced CSV file."""
    return BLD/"python"/"age_efficiency"/"age_eff.csv"

def test_output_file_path(output_file_path):
    """Tests that the produced CSV file is saved in the correct directory."""
    assert os.path.exists(output_file_path), \
        f"Expected output file {output_file_path} does not exist."
    assert os.path.isfile(output_file_path), \
        f"Expected output file {output_file_path} is not a file."