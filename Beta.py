# MATH, part 2
# Particle Physics
#-------------------------------------
# Getting started:

# install "numpy", "matplotlib" packages
# in terminal use:
# pip install sympy
# pip install matplotlib
    # if pip doesn't work, use pip3
    # if pip3 doesn't work, try "python -m pip install matplotlib"
    # if else: "python3 -m pip install matplotlib
    # if else: go to terminal and try:
    # curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
    # if else....~\_o_/~


# import these packages with this code:
import matplotlib.pyplot as plt
import numpy as np
#--------------------------------------

# review of variables
x = 3
y = 2
z = 5
eq = x*y-z
print(eq)

#------------------------------------
# delete values assigned to variables.
del x,y,z
#------------------------------------

# plotting:

# linspace creates a series of values with the syntax:
# (left value, right value, number of points within range)
x = np.linspace(-10,10,100)
# pass the series through the function
y = x**2
# plot
plt.plot(x,y)
plt.show()

#-----------------------------------------
# Solving Complex (math) relationships
#-----------------------------------------

# In physics, the frequency at which particles come into surface
# contact through mixing can be calculated as:

# betaS = (1/6)*((di+dj)**3)*G {=} (m^3/#/s)

# where
# di [=] diameter of particles of size i (m)
# dj [=] diameter of particles of size j (m)
# G is the velocity gradient (s^-1)


# equation:

#betaS = (1/6)*((di+dj)**3)*float(G) # (m^3/#/s)
di = np.linspace(10**-7,10**-5,1000)
dj = np.linspace(10**-7,10**-4,1000)
G = 70
betaS = (1/6)*((di+dj)**3)*float(G) # (m^3/#/s)
plt.plot(di,betaS,'r')
plt.xlabel('Particle Size, m')
plt.ylabel('Beta_Mixing, m^3/#/S')
plt.axis('tight')
plt.show()

#--------------------------------------------
# apart from mixing, particles also come into contact in a fluid from:
# 1. Differential settling
# 2. Brownian (thermal) motion
# 3. Mixing (as we jsut explored)

# some constants we'll need:
# gravitational constant
g = 9.81 # m/s/s
# fluid viscosity
mu = 10**-3 # pascal seconds
# fluid density
rhol = 1000 #kg/m^3
# desnity of particle
rhop = 1.1*rhol # kg/m^3
# Boltzmann constant
kB = 1.38*10**-23 # m2kg/s/s/K
# Temperature of system (K)
T = 273 #K kelvin

# Beta for differential settling
betaDS = (np.pi*g/(72*mu))*np.absolute(di-dj)*(rhop-rhol)*(di+dj)**3
# Beta for Brownian motion
betaBM = (2*kB*T)/(3*mu)*((di+dj)**2)/(di*dj)
# Beta for Shear mixing
betaS = (1/6)*((di+dj)**3)*(G) # (m^3/#/s)
# Total:
Beta = betaS + betaBM+betaDS

plt.plot(di,betaDS,'r',label = "DS")
plt.plot(di,betaBM,'b',label ='BM')
plt.plot(di,betaS,'g',label ='S/M')
plt.plot(di,betaBM,'k',label ='Total')
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.show()


