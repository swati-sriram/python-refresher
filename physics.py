g = 9.81
# calculates the buoyancy based on the formula
def calculate_bouyancy(V: float, density_fluid: float):
    if (V<0 or density_fluid<0):
        raise ValueError("Volume or density fluid can't be negative")
    return density_fluid * V * g
# determines if the object will float in water, returns true if it does and false if it doesn't.
def will_it_float(V:float, mass: float):
    if (V<0 or mass<0):
        raise ValueError("Volume or mass can't be negative")
    if round(calculate_bouyancy(V, 1000), 3) == round(mass*g, 3):
        return None
    return calculate_bouyancy(V, 1000) > mass*g
# returns the pressure given the depth underwater
def calculate_pressure(depth):
    return g*abs(depth)*1000

