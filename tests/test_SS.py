import numpy as np


from proj_ss.config import BLD

import pytest

@pytest.fixture
def test_interest_rate_SS():
    r_SS=np.loadtxt(BLD/ "python" /"results"/ "r0_0.txt")
    r_NOSS=np.loadtxt(BLD/ "python" /"results"/ "r0_1.txt")
    if r_NOSS > r_SS:
        raise AssertionError("Interest rate does not seem to decrease. The result is not in line with the theory.") 
        #interest rate should be lower in the steady state 
        # without social security since K/L goes up
def test_wages_SS():
    w_SS=np.loadtxt(BLD/ "python" /"results"/ "w0_0.txt")
    w_NOSS=np.loadtxt(BLD/ "python" /"results"/ "w0_1.txt")
    #w_NOSS=0  
    #For instance,if w_NOSS is set to 0, the error will be raised
    if w_NOSS < w_SS:
        raise AssertionError("Wages do not seem to decrease. The result is not in line with the theory.")
        #wages should be higher in the steady state without social 
        # security since K/L goes up
def test_capital_SS():
    J=66 
    kgen=np.load(BLD/ "python" /"results"/ "kgen0.npy")
    kgen_first_gen=kgen[0]
    assert kgen_first_gen==0 #capital for new-born agents/generations is 0
    for i in range(0,J):
        if kgen[i]<0:
            raise AssertionError("Agents cannot borrow, so we cannot have savings)")