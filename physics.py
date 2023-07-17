import numpy as np
import matplotlib.pyplot as plt

g = 9.81
pressure_at_surface = 101325  # kilo pascals


def calculate_bouyancy(V: float, density_fluid: float):
    """calculates the buoyancy based on the formula"""
    if V <= 0 or density_fluid <= 0:
        raise ValueError("Invalid volume/density")
    return density_fluid * V * g  # should set this as a variable


def will_it_float(V: float, mass: float):
    """determines if the object will float in water. Returns true if it does and false if it doesn't."""
    if V <= 0 or mass <= 0:
        raise ValueError("Invalid volume/mass")
    if round(calculate_bouyancy(V, 1000), 3) == round(
        mass * g, 3
    ):  # if you get an error from calculate density, the whole program will crash
        return None
    return calculate_bouyancy(V, 1000) > mass * g


def calculate_pressure(depth):
    """returns the pressure given the depth (positve or negative) underwater"""
    return g * abs(depth) * 1000 + pressure_at_surface


def calculate_acceleration(F, m):
    """calculates the acceleration given the force and mass"""
    if F < 0 or m <= 0:
        raise ValueError("Invalid force or mass")
    acceleration = F / m
    return acceleration


def calculate_angular_acceleration(tau, I):
    if I <= 0:
        raise ValueError("Invalid moment of inertia")
    angular_a = tau / I
    return angular_a


def calculate_torque(F_magnitude, F_direction, r):
    if F_magnitude <= 0 or r <= 0:
        raise ValueError("Invalid magitude or radius")
    F_direction_rad = F_direction * np.pi / 180  # convert direction to radians
    torque = r * F_magnitude * np.sin(F_direction_rad)
    return torque


def calculate_moment_of_inertia(m, r):
    if m <= 0 or r <= 0:
        raise ValueError("Invalid mass or radius")
    inertia = m * (r**2)
    return inertia


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    # find the total force and divide by the mass, F_angle is in radians
    if F_magnitude <= 0 or mass <= 0 or volume <= 0 or thruster_distance <= 0:
        raise ValueError("Invalid magnitude/mass/volume/thruster distance")
    F_x = F_magnitude * np.cos(F_angle)
    F_y = F_magnitude * np.sin(F_angle)
    acceleration_arr = np.array([F_x / mass, F_y / mass])
    return acceleration_arr


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    if F_magnitude <= 0 or inertia <= 0 or thruster_distance <= 0:
        raise ValueError("Invalid magnitude or radius")
    perpendicular_force = F_magnitude * np.sin(F_angle)
    a_acceleration = calculate_angular_acceleration(
        perpendicular_force * thruster_distance, inertia
    )
    return a_acceleration


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    if mass <= 0:
        raise ValueError("Invalid mass")
    matrix = np.array(
        [
            [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
            [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],
        ]
    )
    rotation = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
    )
    force = np.matmul(rotation, np.matmul(matrix, T))
    acceleration = force / mass
    return acceleration


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    if L <= 0 or l <= 0 or inertia < 0:
        raise ValueError("Invalid length/width/inertia")
    matrix = np.array(
        [
            L * np.sin(alpha) + l * np.cos(alpha),
            -L * np.sin(alpha) - l * np.cos(alpha),
            L * np.sin(alpha) + l * np.cos(alpha),
            -L * np.sin(alpha) - l * np.cos(alpha),
        ]
    )
    torque = np.matmul(matrix, T)
    angular_acceleration = calculate_angular_acceleration(torque, inertia)
    return angular_acceleration


def simulate_auv2_motion(
    T, alpha, L, l, mass=100, inertia=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0
):
    t = np.arange(0, t_final, dt)
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    theta = np.zeros_like(t)
    v = np.zeros(shape=(2, len(t)))
    omega = np.zeros_like(t)
    a = np.zeros(shape=(2, len(t)))
    x[0] = x0
    y[0] = y0
    theta[0] = theta0
    aa = np.zeros_like(t)
    for i in range(1, len(t)):
        inst_acc = calculate_auv2_acceleration(T, alpha, theta[i], mass)
        a[0][i] = a[0][i - 1] + inst_acc[0]
        a[1][i] = a[1][i - 1] + inst_acc[1]
        v[0][i] = v[0][i - 1] + a[0][i - 1] * dt
        v[1][i] = v[1][i - 1] + a[1][i - 1] * dt
        x[i] = x[i - 1] + v[0][i - 1] * dt + 0.5 * a[0][i - 1] * np.power(dt, 2)
        y[i] = y[i - 1] + v[1][i - 1] * dt + 0.5 * a[1][i - 1] * np.power(dt, 2)
        aa[i] = aa[i - 1] + calculate_auv2_angular_acceleration(T, alpha, L, l)
        omega[i] = omega[i - 1] + aa[i - 1] * dt
        theta[i] = theta[i - 1] + omega[i - 1] * dt + 0.5 * aa[i - 1] * np.power(dt, 2)
    output = (t, x, y, theta, v, omega, a)
    return output


def plot_auv2_motion(t, x, y, theta, v, omega, a):
    plt.plot(t, x, label="X-position")
    plt.plot(t, y, label="Y-position")
    plt.plot(t, theta, label="Angular Displacement")
    vx = v[0]
    vy = v[1]
    ax = a[0]
    ay = a[1]
    plt.plot(t, omega, label="Angular Velocity")
    plt.plot(t, vx, label="X-Velocity")
    plt.plot(t, vy, label="Y-Velocity")
    plt.plot(t, ax, label="X-Acceleration")
    plt.plot(t, ay, label="Y-Accerleration")
    plt.xlabel("Time (s)")
    plt.ylabel(
        "Position (m), Velocity (m/s), Acceleration (m/s^2), Angles (rad), Angular Velocity (rad/s)"
    )
    plt.legend()
    plt.show()
