import pytest
from proj_ss.analysis.age_eff.predict import predict_eff
import pandas as pd
import numpy as np
from numpy.testing import assert_almost_equal

@pytest.fixture
def small_data():
    """Testing the model to predict with a small dataset."""
    data = pd.DataFrame({
        'age': [20,20,25, 25, 30,30, 35,35, 40,40],
        'age2': [400,400, 625, 625,900,900, 1225,1225, 1600, 1600],
        'col': [0,1, 0, 1,0, 1, 0,1,0,1],
        'lwage': [3.5, 4.0, 4.0, 4.5, 4.9,5.0, 5.0, 5.5,5.0,6.3],
        'hhwgt': [100, 200, 150, 250, 175,200, 200, 150, 250, 175]
    })
    return data

def test_predict(small_data):
    result = predict_eff(small_data)

    average_eff=result['average_eff']

    expected_output = pd.DataFrame({
        #'age': [20, 25, 30, 35, 40],
        'average_eff': [0.283697, 0.533658, 0.904288, 1.380339, 1.898018]
    })
    expected_output

    #assert_almost_equal(np.array(average_eff), np.array(expected_output), decimal=5, err_msg='The values of average efficiency do not match.')
    np.testing.assert_allclose(average_eff, expected_output.values.reshape(-1), rtol=1e-5, atol=1e-8, err_msg='The values of average efficiency do not match.')