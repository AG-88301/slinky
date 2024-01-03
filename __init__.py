from math import pi

# Constants related to slinky
m = 0.19973                             # Mass of Slinky in kg
k = 1.086                               # Spring Constant
cd = 2 * m * (1/(2 * pi)) * (k/m)**.5   # Damping Coefficent
L1 = 0.051                              # Compressed Length

# Universal Constants
g = 9.80655                             # Gravity
r = 1.293                               # Density of air

# Slinky Functions
f = lambda x: ((m * g)/(2 * k)) * (1 - (x-1)**2)                                                # Returns length of hanging slinky
dragA = lambda V, diameter, rad: (cd * ((r * V**2)/2) * ((2 * pi * rad) * pi * diameter/2))/m   # Returns acceleration due to drag on slinky
tensionA = lambda x, m, a: m * g + m * a - k * x                                                # Returns (upwards) acceleration due to tension on slinky

# Environoment Constants
floorY = -1.3                           # Y position of floor

t = 0                                   # Time elapsed
dt = 0.001                              # Delta Time

moving = 1                              # Number of coils moving
vel = 0                                 # Velocity of slinky
accel = 0                               # Total acceleration of slinky