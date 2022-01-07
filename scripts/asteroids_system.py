from bge import logic, types
from random import randint, seed
from random import random, choice

class Asteroids(types.KX_GameObject):
    def __init__(self, old_owner, lifes=int(3)):
        self.own = old_owner
        self.lifes = lifes
        self.acceleration = float(0.03)
        self.positions = [float(0), float(244.5)]
        self.angle_acceleration = float(0.06)
        self.angle = float(0.0)
        seed(1)
        self.randomNumber = [float(0), float(0)]


    def AsteroidsInit(self):
        self.positions

    def AsteroidsMoveBotLeft(self, randx, randy):
        #print(self.randomNumber[0], self.randomNumber[1])
        print(randx, randy)
        self.applyMovement([0, randy, 0], False)
        self.applyMovement([randx, 0, 0], False)
    
    def AsteroidsMoveBotRight(self):
        self.applyMovement([0, self.acceleration + 0.3, 0], False)
        self.applyMovement([-self.acceleration - 0.01, self.acceleration, 0], False)

    def AsteroidsMoveTopRight(self):
        self.applyMovement([0, -self.acceleration - 0.04, 0], False)
        self.applyMovement([-self.acceleration - 0.03, self.acceleration, 0], False)
    
    def AsteroidsMoveTopLeft(self):
        self.applyMovement([0, -self.acceleration - 0.02, 0], False)
        self.applyMovement([self.acceleration, self.acceleration, 0], False)