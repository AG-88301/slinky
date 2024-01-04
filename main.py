from vpython import *
from time import sleep

from __init__ import *
from slinky import Slinky

scene = canvas.get_selected()
scene.width = 1120
scene.height = 350
scene.background = color.gray(0.15)

# Graphs
f1 = gcurve(color=color.cyan)
f2 = gcurve(color=color.purple)
f3 = gcurve(color=color.green)
f4 = gcurve(color=color.blue)
f5 = gcurve(color=color.black)
f6 = gcurve(color=color.red)

# Set up the scene
slinky = Slinky(radius=0.05, thickness=(L1/66)*10, turns=66)
floor = box(pos=vector(0, floorY, 0), size=vector(1, 0.1, 1))
scene.camera.follow(slinky.balls[32])

# Set slinky to correct position
for i in range(slinky.turns + 1):
    slinky.balls[i].pos = vector(0, L((1/slinky.turns) * i), 0)
slinky.update()

sleep(3)

# Height between points at previous dt, used to calculate delta height
h = [abs(slinky.balls[i].pos.y - slinky.balls[i+1].pos.y) for i in range(len(slinky.balls)-1)]
    
while t < 10:
    rate(1000)

    # Force and Velocity applying on (moving section) of slinky
    F = g * (((slinky.turns - moving)/slinky.turns) * m) - (k * L(moving/slinky.turns))
    vel += (F/((moving/slinky.turns) * m)) * dt
    
    # update position
    for i in range(moving):
        slinky.balls[i].pos.y -= vel * dt
    slinky.update()

    # Check if wave has collided with next coil, if so, add coil to moving section
    if (slinky.balls[moving-1].pos.y - slinky.balls[moving].pos.y) <= (L1/(slinky.turns)):
        slinky.balls[moving].pos.y = slinky.balls[moving-1].pos.y - L1/slinky.turns
        
        moving += 1
        vel = (vel * moving * (m/slinky.turns)) / ((moving + 1) * (m/slinky.turns))
        if moving >= slinky.turns: break


    # update height map
    h = [abs(slinky.balls[i].pos.y - slinky.balls[i+1].pos.y) for i in range(len(slinky.balls)-1)]
    

    # update graphs
    f1.plot(t, slinky.balls[0].pos.y)
    f2.plot(t, slinky.balls[15].pos.y)
    f3.plot(t, slinky.balls[32].pos.y)
    f4.plot(t, slinky.balls[47].pos.y)
    f5.plot(t, slinky.balls[-1].pos.y)

    t += dt
    
# t_c <= t -> slinky has collapsed
while True:
    rate(1000)

    if abs(slinky.balls[-1].pos.mag - floor.pos.mag) > 0.05: # not collided with floor
        vel += 0.5 * g * dt
        for i in range(slinky.turns + 1):
            slinky.balls[i].pos.y -= vel * dt
        slinky.update()
    else: break
    
    # update graphs
    f1.plot(t, slinky.balls[0].pos.y)
    f2.plot(t, slinky.balls[15].pos.y)
    f3.plot(t, slinky.balls[32].pos.y)
    f4.plot(t, slinky.balls[47].pos.y)
    f5.plot(t, slinky.balls[-1].pos.y)

    t += dt


while t <= 0.43:
    rate(1000)
    
    # update graphs
    f1.plot(t, slinky.balls[0].pos.y)
    f2.plot(t, slinky.balls[15].pos.y)
    f3.plot(t, slinky.balls[32].pos.y)
    f4.plot(t, slinky.balls[47].pos.y)
    f5.plot(t, slinky.balls[-1].pos.y)

    t += dt

while True: rate(30)
