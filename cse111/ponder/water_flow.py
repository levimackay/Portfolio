# These are constants for physical values and standard pipe specs.
# I'm using these instead of hardcoding values in functions to keep things clean and readable.
WATER_DENSITY = 998.2  # kg/m^3
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa·s
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2

PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013
SUPPLY_VELOCITY = 1.65

HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018
HOUSEHOLD_VELOCITY = 1.75

def water_column_height(tower_height, tank_height):
    '''This just adds the full height of the water in the tower to 75% of the tank wall height.
        That's the total height of the water column the system is using.'''
    return tower_height + (3 * tank_height)/4

def pressure_gain_from_water_height(height):
    '''Calculates the pressure from the water height using gravity and density.
        Returns pressure in kilopascals (kPa).'''
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(diameter, length, friction_factor, fluid_velocity):
    '''I feel like I lowkey have something wrong here, but this is how you calculate pressure loss from pipe friction.'''
    return (-friction_factor * length * WATER_DENSITY * (fluid_velocity**2)) / (2000 * diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    '''Calculates pressure loss from fittings like elbows in the pipe.
        The more angles and the faster the water moves, the more pressure you lose.'''
    return (-0.04 * WATER_DENSITY * (fluid_velocity**2) * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    '''Reynolds number is basically how "turbulent" or "smooth" the flow is.
        This lets us figure out how the water's going to behave inside the pipe.'''
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    ratio = (((larger_diameter / smaller_diameter) ** 4) - 1)
    k = (0.1 + (50 / reynolds_number)) * ratio
    return (-k * WATER_DENSITY * (fluid_velocity**2)) / 2000

def kpa_to_psi(kpa):
    '''Just converts kilopascals to psi since that's what people in the U.S. are used to.'''
    return kpa * 0.1450377

def rate_pressure_system(pressure_kpa):
    '''This just gives a simple “health rating” for the pressure.
       Like, is your system doing fine? Is it too low? Is it gonna explode?
       Helps you know if you need to adjust anything without diving into the math.'''
    if pressure_kpa < 150:
        return "⚠️ Low – You might want to check your pipe length or tank height."
    elif pressure_kpa > 500:
        return "💥 Too high – You might need a pressure regulator."
    else:
        return "✅ Optimal – Your system looks good."

def main():
    '''Main function that asks for inputs, does the math, and prints the final pressure.
        The flow goes from the tower, through the supply pipe, down to the house.'''
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    pressure += pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    pressure += pressure_loss_from_pipe(diameter, length2, friction, velocity)

    psi = kpa_to_psi(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals ({psi:.1f} psi)")
    print("System Pressure Rating:", rate_pressure_system(pressure))

# The icing to the cake
if __name__ == "__main__":
    main()
