g = 9.81
pressure_at_surface = 101325 #kilo pascals
def calculate_bouyancy(V: float, density_fluid: float):
    '''calculates the buoyancy based on the formula'''
    if (V<=0 or density_fluid<=0):
        raise ValueError("Invalid volume/density")
    return density_fluid * V * g #should set this as a variable

def will_it_float(V:float, mass: float):
    '''determines if the object will float in water. Returns true if it does and false if it doesn't.'''
    if (V<=0 or mass<=0):
        raise ValueError("Invalid volume/mass")
    if round(calculate_bouyancy(V, 1000), 3) == round(mass*g, 3): #if you get an error from calculate density, the whole program will crash
        return None
    return calculate_bouyancy(V, 1000) > mass*g
def calculate_pressure(depth):
    '''returns the pressure given the depth (positve or negative) underwater'''
    return g*abs(depth)*1000 + pressure_at_surface

