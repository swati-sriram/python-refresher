g = 9.81
def calculate_bouyancy(V: float, density_fluid: float):
    # calculates the buoyancy based on the formula
    if (V<=0 or density_fluid<=0):
        raise ValueError("Invalid volume/density")
    return density_fluid * V * g

def will_it_float(V:float, mass: float):
    # determines if the object will float in water. Returns true if it does and false if it doesn't.
    if (V<=0 or mass<=0):
        raise ValueError("Invalid volume/mass")
    if round(calculate_bouyancy(V, 1000), 3) == round(mass*g, 3):
        return None
    return calculate_bouyancy(V, 1000) > mass*g
def calculate_pressure(depth):
    # returns the pressure given the depth underwater
    return g*abs(depth)*1000

