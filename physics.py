import numpy as np

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

def calculate_acceleration(F, m):
    '''calculates the acceleration given the force and mass'''
    if (F<0 or m<=0):
        raise ValueError("Invalid force or mass")
    acceleration = F/m
    return acceleration

def calculate_angular_acceleration(tau, I):
    if (I<=0):
        raise ValueError("Invalid moment of inertia")
    angular_a = tau/I
    return angular_a

def calculate_torque(F_magnitude, F_direction, r): 
    if (F_magnitude<=0 or r<=0):
        raise ValueError("Invalid magitude or radius")
    F_direction_rad = F_direction * np.pi / 180 #convert direction to radians
    torque = r * F_magnitude * np.sin(F_direction_rad)
    return torque

def calculate_moment_of_inertia(m, r):
    if (m<=0 or r<=0):
        raise ValueError("Invalid mass or radius")
    inertia = m*(r**2)
    return inertia

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100, volume = 0.1, thruster_distance=0.5):
    # find the total force and divide by the mass, F_angle is in radians
    F_x = F_magnitude*np.cos(F_angle)
    F_y=F_magnitude*np.sin(F_angle)
    acceleration_arr = np.array([F_x/mass, F_y/mass])
    return acceleration_arr

#def calculate_auv_angular_acceleration(F_maginitude, F_angle, inertia, thruster_distance):
