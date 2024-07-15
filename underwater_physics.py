import numpy as np
import math
import matplotlib.pyplot as plt

g = 9.81

def calculate_buoyancy(V, density_fluid):
    '''
    Calculate the buoyance of an object within a fluid

    Parameters:
        V: the volume of the object in cubic meters,
        density_fluid: the density of the fluid in 𝑘𝑔/𝑚^3   
        

    '''
    buoyancy = g * density_fluid * V
    return buoyancy

def will_it_float(V, mass):
    density_water = 1000
    density_object = mass/V
    return density_water > density_water

def calculate_pressure(depth):
    return depth*1000*g

def calculate_acceleration(F,m):
    return F/m

def calculate_angular_acceleration(tau,I):
    return tau/I

def calculate_torque(F_magnitude, F_direction, r):
    return F_magnitude * np.sin(F_direction) * r

def calculate_moment_of_inertia(m,r):
    return m*r**2

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100, volume = .1, thruster_distance = .5):
    buoyant_force = calculate_buoyancy(volume, 1000)
    #return np.sqrt(F_magnitude**2+buoyant_force**2)/mass
    #return np.sqrt((F_magnitude*np.sin(F_angle)+buoyant_force)**2+(F_magnitude*np.cos(F_angle)))/mass
    return np.sqrt(F_magnitude**2)/mass

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia, thruster_distance = .5):
    thruster_torque = calculate_angular_acceleration(calculate_torque(F_magnitude,F_magnitude,thruster_distance))

def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    horizontal = np.cos(alpha)*(T[0]+ T[1]- T[2] - T[3])
    vertical = np.sin(alpha)*(T[0] - T[1] - T[2] + T[3])
    return np.sqrt(horizontal**2+vertical**2)/mass

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    moment_arm = np.sqrt(l**2+L**2)
    net_torque = moment_arm*np.sin(alpha)*(T[0]+T[2]-T[1]-T[3])
    return calculate_torque(net_torque, math.pi/2, moment_arm)/inertia

def simulate_av2_motion(T, alpha, L, l, mass=100, inertia=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0):
    t = np.arange(0,t_final+dt,dt)

    moment_arm = np.sqrt(l**2+L**2)
    net_torque = moment_arm*np.sin(alpha)*(T[0]+T[2]-T[1]-T[3])
    theta = t**2 * 1/2 * net_torque/inertia + theta0
    print(theta)

    horizontal = np.sin(math.pi/2-alpha+theta)*(T[0]+ T[1]- T[2] - T[3])/mass
    vertical = np.cos(math.pi/2-alpha+theta)*(T[0] - T[1] - T[2] + T[3])/mass
    a = np.sqrt(horizontal**2 + vertical**2)
    print(a)

    horizontal_v = np.array([sum(horizontal[:i])*dt for i in range(len(horizontal))])
    vertical_v = np.array([sum(vertical[:i])*dt for i in range(len(vertical))])
    v = np.sqrt(horizontal_v**2 + vertical_v**2)
    print(v)

    x = x0+np.array([sum(horizontal_v[:i])*dt for i in range(len(horizontal_v))])
    y = y0+np.array([sum(vertical_v[:i])*dt for i in range(len(vertical_v))])
    v = np.sqrt(horizontal_v**2 + vertical_v**2)
    print(x)
    print(y)

    omega = net_torque/inertia * t
    print(omega)


    return t, x, y, theta, v, omega, a

def plot_auv2_motion(t, x, y, x0=0, y0=0, theta0=0):
    plt.plot(x,y)
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.show()


T= np.array([100,0,90,0])
t,x,y,theta,v,omega,a = simulate_av2_motion(T,math.pi/4,10,10)
plot_auv2_motion(t,x,y)