"""Task to obtain the estimated age-efficiency."""

import pandas as pd
import pytask
import matplotlib.pyplot as plt
import os

from proj_ss.analysis.predict import predict_eff
from proj_ss.analysis.predict import predict_eff_age
from proj_ss.config import BLD, SRC
from proj_ss.utilities import read_yaml



@pytask.mark.depends_on(
    {
        "scripts": ["predict.py"],
        "data": BLD / "python" / "data" / "cleaned_data.csv",
    },
)
@pytask.mark.produces(BLD / "python" / "age_efficiency"/"age_eff.csv")
def task_age_eff_csv_python(depends_on, produces):
    """Fit a logistic regression model (Python version)."""
    #data_info = read_yaml(depends_on["data_info"])
    data = pd.read_csv(depends_on["data"])
    data = predict_eff(data)
    data.to_csv(produces, index=False)


@pytask.mark.depends_on(
    {
        "scripts": ["predict.py"],
        "data": BLD / "python" / "data" / "cleaned_data.csv",
    },
)
@pytask.mark.produces(BLD / "python" / "age_efficiency"/"eff_profiles_py.txt")
def task_age_eff_txt_python(depends_on, produces):
    """Fit a logistic regression model (Python version)."""
    #data_info = read_yaml(depends_on["data_info"])
    data = pd.read_csv(depends_on["data"])
    data = predict_eff(data)
    data[['average_eff']].to_csv(produces, sep=' ', header=False, index=False)