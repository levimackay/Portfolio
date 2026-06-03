
from math import isclose
import pytest
from water_flow import (
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi,
    pressure_loss_from_pipe,
    pressure_gain_from_water_height,
    water_column_height
)

def test_pressure_loss_from_fittings():
    assert isclose(pressure_loss_from_fittings(0, 3), 0, abs_tol=0.001)
    assert isclose(pressure_loss_from_fittings(1.65, 0), 0, abs_tol=0.001)
    assert isclose(pressure_loss_from_fittings(1.65, 2), -0.109, abs_tol=0.001)
    assert isclose(pressure_loss_from_fittings(1.75, 2), -0.122, abs_tol=0.001)
    assert isclose(pressure_loss_from_fittings(1.75, 5), -0.306, abs_tol=0.001)

def test_reynolds_number():
    assert isclose(reynolds_number(0.048692, 0), 0, abs_tol=1)
    assert isclose(reynolds_number(0.048692, 1.65), 80069, abs_tol=1)
    assert isclose(reynolds_number(0.048692, 1.75), 84922, abs_tol=1)
    assert isclose(reynolds_number(0.28687, 1.65), 471729, abs_tol=1)
    assert isclose(reynolds_number(0.28687, 1.75), 500318, abs_tol=1)

def test_pressure_loss_from_pipe_reduction():
    assert isclose(pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692), 0, abs_tol=0.001)
    assert isclose(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692), -0.309, abs_tol=0.001)
    assert isclose(pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692), -0.347, abs_tol=0.001)

def test_kpa_to_psi():
    assert isclose(kpa_to_psi(0), 0, abs_tol=0.001)
    assert isclose(kpa_to_psi(101.325), 14.6959, abs_tol=0.001)
    assert isclose(kpa_to_psi(158.7), 23.0175, abs_tol=0.001)

def test_pressure_loss_from_pipe():
    assert isclose(pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75), -113.008, abs_tol=0.01)
    assert isclose(pressure_loss_from_pipe(0.28687, 200, 0.013, 1.65), -9.401, abs_tol=0.01)

def test_pressure_gain_from_water_height():
    assert isclose(pressure_gain_from_water_height(0), 0, abs_tol=0.001)
    assert isclose(pressure_gain_from_water_height(30.48), 298.369, abs_tol=0.01)

def test_water_column_height():
    assert isclose(water_column_height(30, 10), 37.5, abs_tol=0.001)
    assert isclose(water_column_height(0, 8), 6, abs_tol=0.001)


pytest.main(["-v", "--tb=line", "-rN", __file__])
