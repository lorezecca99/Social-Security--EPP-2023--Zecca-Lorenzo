import pandas as pd
import pytask
import matplotlib.pyplot as plt
import os

from proj_ss.analysis.age_eff.predict import predict_eff_age
from proj_ss.config import BLD, SRC
from proj_ss.utilities import read_yaml


figure_dir = BLD / "python" / "age_efficiency" / "figure"
os.makedirs(figure_dir, exist_ok=True)             
##This is needed, otherwise, the folder is not created by "produces"
 
@pytask.mark.depends_on(
    {
        "scripts": ["predict.py"],
        "data": BLD / "python" / "age_efficiency" / "age_eff.csv",
    },
)
@pytask.mark.produces(
    {BLD / "python" / "age_efficiency"/"figure"}
)
def task_age_eff_txt_python(depends_on, produces):
    """Figure (Python version)."""
    data=pd.read_csv(depends_on["data"])
    fig_eff=predict_eff_age(data)
    fig_eff.savefig(BLD / "python" / "age_efficiency" / "figure"/ "eff_age_profile.png")
    return produces