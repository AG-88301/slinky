from math import pi

# Constants related to slinky
m = 0.19973                             # Mass of Slinky in kg
k = 25.7349                             # Spring Constant
cd = 2 * m * (1/(2 * pi)) * (k/m)**.5   # Damping Coefficent
L0 = 0.051                              # Compressed Length

# Universal Constants
g = 9.80655     # Gravity
r = 1.293       # Density of air

# Slinky Functions
L = lambda x: ((x/m)*g)/(2*k)                                                                   # Helper function to f(x)
f = lambda x: L(x - 1)**2                                                                       # Returns length of hanging slinky
dragA = lambda V, diameter, rad: (cd * ((r * V**2)/2) * ((2 * pi * rad) * pi * diameter/2))/m   # Returns acceleration due to drag on slinky
# tensionA = lambda x, t, m: m * g + m * accel - 

# Environoment Constants
t = 0                               # Time elapsed
dt = 0.001                          # Delta Time

moving = 1                          # Number of coils moving
vel = 0                             # Velocity of slinky
accel = 0                           # Total acceleration of slinky