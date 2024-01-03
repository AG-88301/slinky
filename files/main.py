from vpython import *
from time import sleep
from scipy.integrate import quad

from __init__ import *
from slinky import Slinky

scene = canvas.get_selected()
scene.width = 1120
scene.height = 350

f1 = gcurve(color=color.cyan)
f2 = gcurve(color=color.purple)
f3 = gcurve(color=color.green)
f4 = gcurve(color=color.blue)
f5 = gcurve(color=color.black)

slinky = Slinky(radius=0.05, thickness=(L1/66)*10, turns=66)
floor = box(pos=vector(0, floorY, 0), size=vector(1, 0.1, 1))
scene.camera.follow(slinky.balls[32]) 

for i in range(slinky.turns + 1):
    slinky.balls[i].pos = vector(0, -f((1/slinky.turns) * i), 0)
slinky.update()

print(slinky.height())

sleep(3)

prev_vel = 0
heights = {}

h = [abs(slinky.balls[i].pos.y - slinky.balls[i+1].pos.y) for i in range(len(slinky.balls)-1)]
    
while t < 10:
    rate(1000)
    prev_vel = vel
    #dy = h[moving-1]
    
    if moving > slinky.turns:
        break
    
    lmd = (m - (i/66) * m)/abs(slinky.balls[-1].pos.y - slinky.balls[moving - 1].pos.y)
    lmdf = lambda x: lmd * h[moving - 1] * g
    integral = quad(lmdf, 0, abs(slinky.balls[-1].pos.y - slinky.balls[moving - 1].pos.y))[0]

    F = g * (((slinky.turns - moving)/slinky.turns) * m) - (5 * (m*moving/slinky.turns) * g/24) - integral
    vel += (F/m) * dt
    
    for i in range(moving):
        slinky.balls[i].pos.y -= vel * dt
    slinky.update()

    h = [abs(slinky.balls[i].pos.y - slinky.balls[i+1].pos.y) for i in range(len(slinky.balls)-1)]
    
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
    prev_vel = vel

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