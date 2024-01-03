# Constants related to slinky
m = 0.19973                             # Mass of Slinky in kg
k = 1.086                               # Spring Constant
L1 = 0.051                              # Compressed Length

# Universal Constants
g = 9.81                                # Gravity
r = 1.293                               # Density of air

# Slinky Functions
f = lambda x: (
    (m * g)/(2 * k)) * (1 - (x-1)**2
)                                       # Returns length of hanging slinky

# Environoment Constants
floorY = -1.3                           # Y position of floor

t = 0                                   # Time elapsed
dt = 0.001                              # Delta Time

moving = 1                              # Number of coils moving
vel = 0                                 # Velocity of slinky
