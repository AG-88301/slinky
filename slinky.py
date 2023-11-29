from vpython import *

class Slinky:
    def __init__(self, radius, thickness, turns):
        self.BALLR = 0.01
        self.DIST = 0.05

        self.balls = [sphere(pos = vector(0, 0, 0), radius = self.BALLR, color = color.yellow)] # balls[0] = top 
        self.coils = [] # len(coils) = len(balls) - 1

        self.radius = radius
        self.thickness = thickness
        self.turns = turns

        self.create()

    def create(self):
        for i in range(self.turns):
            ball = sphere(pos = vector(0, -(self.DIST * (i + 1)), 0), radius = self.BALLR)

            top = self.balls[-1] # top of coil
            coil = helix(pos=top.pos, axis=ball.pos-top.pos, radius=self.radius, thickness=self.thickness,color=color.cyan, coils=1)

            self.balls.append(ball)
            self.coils.append(coil)

    def update(self):
        for i in range(len(self.balls)-1):
            self.coils[i].pos = self.balls[i].pos
            self.coils[i].axis = self.balls[i + 1].pos - self.balls[i].pos

    def height(self):
        return abs(self.balls[0].pos.y - self.balls[-1].pos.y)