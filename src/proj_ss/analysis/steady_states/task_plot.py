import numpy as np
import matplotlib.pyplot as plt
import pytask

from proj_ss.analysis.steady_states.code_SS import plot_SS_K
from proj_ss.analysis.steady_states.code_SS import plot_SS_L
from proj_ss.analysis.steady_states.code_SS import plot_SS_E
from proj_ss.analysis.steady_states.code_SS import plot_SS_C

from proj_ss.config import BLD

import os

figures_dir = BLD / "python"/ "figures"/"steady_states"
os.makedirs(figures_dir, exist_ok=True)


@pytask.mark.depends_on(
    {
        "data_k0": BLD / "python" /"results"/ "kgen0.npy",
        "data_k1": BLD / "python" /"results"/ "kgen1.npy",
        "data_l0": BLD / "python" /"results"/ "labgen0.npy",
        "data_l1": BLD / "python" /"results"/ "labgen1.npy",
        "data_e0": BLD / "python" /"results"/ "earn_0.npy",
        "data_e1": BLD / "python" /"results"/ "earn_1.npy",
        "data_c0": BLD / "python" /"results"/ "cons_0.npy",
        "data_c1": BLD / "python" /"results"/ "cons_1.npy",
    },
)
def task_plot_SS(depends_on, produces):
    """Figure for SS"""
    kgen0=np.load(depends_on['data_k0'])
    kgen1=np.load(depends_on['data_k1'])
    labgen0=np.load(depends_on['data_l0'])
    labgen1=np.load(depends_on['data_l1'])
    earnings_0=np.load(depends_on['data_e0'])
    earnings_1=np.load(depends_on['data_e1'])
    cons_0=np.load(depends_on['data_c0'])
    cons_1=np.load(depends_on['data_c1'])
    fig_K = plot_SS_K(kgen0,kgen1)
    fig_K.savefig(BLD/"python"/"figures"/"steady_states"/"savings_by_age.png")
    fig_L = plot_SS_L(labgen0,labgen1)
    fig_L.savefig(BLD/"python"/"figures"/"steady_states"/"labor_by_age.png")
    fig_E = plot_SS_E(earnings_0,earnings_1)
    fig_E.savefig(BLD/"python"/"figures"/"steady_states"/"earnings_by_age.png")
    fig_C = plot_SS_C(cons_0,cons_1)
    fig_C.savefig(BLD/"python"/"figures"/"steady_states"/"consumption_by_age.png")
    return produces