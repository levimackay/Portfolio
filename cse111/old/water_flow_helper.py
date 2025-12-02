WATER_DENSITY = 998.2  # kg/m^3
GRAVITY = 9.80665  # m/s^2


def water_column_height(tower_height, tank_height):
    return tower_height + tank_height


def pressure_gain_from_water_height(height):
    return WATER_DENSITY * GRAVITY * height / 1000  # Convert from Pa to kPa


def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    return -friction_factor * (length / diameter) * WATER_DENSITY * velocity**2 / 2000  # in kPa