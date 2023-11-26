from vpython import *

from slinky import Slinky

scene = canvas.get_selected()
scene.width = 1120
scene.height = 700

m = 0.19973 # mass of slinky in kg
g = 9.80655 # gravity
k = 25.7349 # spring constant

L = lambda x: ((x/m)*g)/(2*k) # length of slinky extended under gravity
f = lambda x: L(x - 1)**2 # {0 <= x <= 1}

slinky = Slinky(radius=0.05, thickness=0.00727, turns=66)

scene.camera.follow(slinky.balls[-2 + slinky.turns//2])

f1 = gcurve(color=color.cyan)
for i in range(len(slinky.balls)):
    slinky.balls[i].pos = vector(0, f((1/slinky.turns) * i), 0)
    f1.plot((1/slinky.turns) * i, f((1/slinky.turns) * i))
slinky.update()

print(slinky.balls[0].pos - slinky.balls[-1].pos)

t = 0
dt = 0.001

while t < 10:
    rate(100)

    for i in range(len(slinky.balls)):
        slinky.balls[i].pos = vector(0, slinky.balls[i].pos.y, 0)
    slinky.update()

    t += dt