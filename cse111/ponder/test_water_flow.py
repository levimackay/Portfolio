from pytest import approx
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi
)

def test_water_column_height():
    '''This just checks that we're calculating water height correctly.'''
    assert water_column_height(30.0, 5.0) == approx(33.75, abs=0.001)
    assert water_column_height(20.5, 3.5) == approx(23.125, abs=0.001)
    assert water_column_height(50.0, 0.0) == approx(50.0, abs=0.001)

def test_pressure_gain_from_water_height():
    '''Making sure the pressure from water height is being calculated right.'''
    assert pressure_gain_from_water_height(0.0) == approx(0.0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    '''This tests pressure loss from pipe friction. The longer the pipe, the more pressure is lost. I seem to be having the most issues with this function for some reason.'''
    assert pressure_loss_from_pipe(0.048692, 0.0, 0.018, 1.75) == approx(0.0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.0, 1.75) == approx(0.0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0.0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)
    
def test_pressure_loss_from_fittings():
    '''This checks the pressure loss from the angles in the pipe. More bends = more pressure loss.'''
    assert pressure_loss_from_fittings(0, 3) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    '''Making sure the Reynolds number (flow behavior) calculation works right.'''
    assert reynolds_number(0.048692, 0) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.28687, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.28687, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    '''This tests the pressure drop that happens when going from a fat pipe to a skinny one.'''
    assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

def test_kpa_to_psi():
    '''This checks that the kilopascals to psi conversion is working correctly.'''
    assert kpa_to_psi(0) == approx(0.0, abs=0.001)
    assert kpa_to_psi(100) == approx(14.5038, abs=0.001)
    assert kpa_to_psi(158.7) == approx(23.017489, abs=0.001)

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "--tb=line", "-rN", __file__])
