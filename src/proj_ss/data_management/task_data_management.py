"""Tasks for managing the data."""

import pandas as pd
import pytask
import os 

from proj_ss.config import BLD, SRC
from proj_ss.data_management import clean_data
from proj_ss.utilities import read_yaml

data_dir = BLD / "python"/ "data"
os.makedirs(data_dir, exist_ok=True)

@pytask.mark.depends_on(
    {
        "scripts": ["clean_data.py"],
        "data": SRC / "data"/ "dataset.csv"
    },
)
@pytask.mark.produces(BLD / "python" / "data"/"cleaned_data.csv")
def task_clean_data_python(depends_on,produces):
    """Clean the data (Python version)."""
    #data_info = read_yaml(depends_on["data_info"])
    data = pd.read_csv(depends_on["data"])
    data = clean_data(data)
    data.to_csv(produces)
