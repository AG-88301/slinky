from vpython import *
from math import pi

from slinky import Slinky

scene = canvas.get_selected()
scene.width = 1120
scene.height = 700

m = 0.19973 # mass of slinky in kg
g = 9.80655 # gravity
k = 25.7349 # spring constant

cd = 0.2
r = 1.293

L0 = 0.051

L = lambda x: ((x/m)*g)/(2*k) # length of slinky extended under gravity
f = lambda x: L(x - 1)**2 # {0 <= x <= 1}
dragA = lambda V, diameter, rad: (cd * ((r * V**2)/2) * ((2 * pi * rad) * pi * diameter/2))/m
# tensionA = lambda x, t, m: m * g + m * accel - 

slinky = Slinky(radius=0.05, thickness=(L0/66)*10, turns=66)

for i in range(slinky.turns + 1):
    slinky.balls[i].pos = vector(0, f((1/slinky.turns) * i), 0)
slinky.update()

print(slinky.balls[0].pos - slinky.balls[-1].pos)

t = 0
dt = 0.001

moving = 1
vel = 0
accel = 0

f1 = gcurve(color=color.cyan)
f2 = gcurve(color=color.purple)
f3 = gcurve(color=color.green)

while t < 0.5:
    rate(100)
    t += dt

while t < 10:
    rate(1000)

    accel = g - dragA(vel, slinky.thickness, slinky.radius)
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

    vel += (g - dragA(vel, slinky.thickness, slinky.radius)) * dt
    for i in range(slinky.turns + 1):
        slinky.balls[i].pos.y -= vel * dt
    slinky.update()
    f3.plot(t, vel)

    t += dt