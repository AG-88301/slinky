from vpython import *

from __init__ import *
from slinky import Slinky

scene = canvas.get_selected()
scene.width = 1120
scene.height = 700

f1 = gcurve(color=color.cyan)
f2 = gcurve(color=color.purple)
f3 = gcurve(color=color.green)

slinky = Slinky(radius=0.05, thickness=(L0/66)*10, turns=66)
floor = box(pos=vector(0, floorY, 0), size=vector(1, 0.1, 1))

for i in range(slinky.turns + 1):
    slinky.balls[i].pos = vector(0, f((1/slinky.turns) * i), 0)
slinky.update()

print(slinky.balls[0].pos - slinky.balls[-1].pos)

while t < 0.5:
    rate(100)
    t += dt

while t < 10:
    rate(1000)

    accel = g - dragA(vel, slinky.thickness, slinky.radius) - tensionA((slinky.turns - moving - 1)/slinky.turns, (moving + 1) * (m/slinky.turns), accel)
    vel += accel * dt
    for i in range(moving):
        slinky.balls[i].pos.y -= vel * dt
    slinky.update()

    if moving > slinky.turns:
        break
    
    if (slinky.balls[moving-1].pos.y - slinky.balls[moving].pos.y) <= (L0/(slinky.turns)):
        slinky.balls[moving].pos.y = slinky.balls[moving-1].pos.y - L0/slinky.turns
        
        moving += 1
        vel = (vel * moving * (m/slinky.turns)) / ((moving + 1) * (m/slinky.turns))

    f1.plot(t, slinky.balls[0].pos.y)
    f2.plot(t, slinky.balls[-1].pos.y)
    f3.plot(t, vel)

    t += dt

print(slinky.height())

while True:
    rate(1000)

    if abs(slinky.balls[-1].pos.mag - floor.pos.mag) > 0.05:
        vel += (g - dragA(vel, slinky.thickness, slinky.radius)) * dt
        for i in range(slinky.turns + 1):
            slinky.balls[i].pos.y -= vel * dt
        slinky.update()

    f3.plot(t, vel)

    t += dt