from vpython import *
from time import sleep

from __init__ import *
from slinky import Slinky

scene = canvas.get_selected()
scene.width = 1120
scene.height = 700

f1 = gcurve(color=color.cyan)
f2 = gcurve(color=color.purple)
f3 = gcurve(color=color.green)
f4 = gcurve(color=color.purple)
f5 = gcurve(color=color.green)

slinky = Slinky(radius=0.05, thickness=(L1/66)*10, turns=66)
floor = box(pos=vector(0, floorY, 0), size=vector(1, 0.1, 1))

for i in range(slinky.turns + 1):
    slinky.balls[i].pos = vector(0, -f((1/slinky.turns) * i), 0)
slinky.update()

print(slinky.balls[0].pos - slinky.balls[-1].pos)

sleep(3)

while t < 10:
    rate(1000)

    accel = g
    vel += accel * dt
    for i in range(moving):
        slinky.balls[i].pos.y -= vel * dt
    slinky.update()

    if moving > slinky.turns:
        break
    
    if (slinky.balls[moving-1].pos.y - slinky.balls[moving].pos.y) <= (L1/(slinky.turns)):
        slinky.balls[moving].pos.y = slinky.balls[moving-1].pos.y - L1/slinky.turns
        
        moving += 1
        vel = (vel * moving * (m/slinky.turns)) / ((moving + 1) * (m/slinky.turns))

    f1.plot(t, slinky.balls[0].pos.y)
    f2.plot(t, slinky.balls[15].pos.y)
    f3.plot(t, slinky.balls[32].pos.y)
    f4.plot(t, slinky.balls[47].pos.y)
    f5.plot(t, slinky.balls[-1].pos.y)

    t += dt

print(slinky.height())

while True:
    rate(1000)

    if abs(slinky.balls[-1].pos.mag - floor.pos.mag) > 0.05:
        vel += (g - dragA(vel, slinky.thickness, slinky.radius)) * dt
        for i in range(slinky.turns + 1):
            slinky.balls[i].pos.y -= vel * dt
        slinky.update()
    else: break
        
    f1.plot(t, slinky.balls[0].pos.y)
    f2.plot(t, slinky.balls[15].pos.y)
    f3.plot(t, slinky.balls[32].pos.y)
    f4.plot(t, slinky.balls[47].pos.y)
    f5.plot(t, slinky.balls[-1].pos.y)

    t += dt