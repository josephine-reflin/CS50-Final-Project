import numpy as np
from calibrate import calculate_nse, calculate_rmse, calculate_bias, calculate_pbias

# test sample data
obs_perfect = [1,2,3,4,5]
sim_perfect = [1,2,3,4,5]
obs_poor = [1,2,3,4,5]
sim_poor = [5,4,3,2,1]
obs = [10,15,20,25,30]
sim = [12,14,22,23,29]


def test_calculate_nse():
    assert calculate_nse(obs_perfect, sim_perfect) == 1.0
    result = calculate_nse(obs_poor, sim_poor)
    assert result < 0

def test_calculate_rmse():
    assert calculate_rmse(obs_perfect, sim_perfect) == 0.0

    result1 = calculate_rmse(obs, sim)
    assert result1 > 0

    result2 = calculate_rmse(obs, sim)
    assert round(result2, 2) == 1.67

def test_calculate_bias():
    differences = []

    for i in range(len(obs)):
        o = obs[i]
        s = sim[i]
        diff = s - o
        differences.append(diff)

    total = sum(differences)
    count = len(differences)
    expected = total/count

    result = calculate_bias(obs,sim)

    tolerance = 1e-6
    assert abs(result - expected) < tolerance

def test_calculate_pbias():
    differences = []

    for i in range(len(obs)):
        o = obs[i]
        s = sim[i]
        diff = s - o
        differences.append(diff)

    total = sum(differences)
    count = len(differences)
    expected = total/count

    result = calculate_pbias(obs,sim)

    tolerance = 1e-6
    assert abs(result - expected) < tolerance

    assert calculate_pbias(obs_perfect, sim_perfect) == 0.0

