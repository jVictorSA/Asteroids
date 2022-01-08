from bge import logic, types
from scripts.asteroids_system import Asteroids
from random import choice

aList = [[0.05, 0.01], [0.01, 0.5], [-0.9, -0.06], [0.02, 0.1], [-0.4, -0.07], [0.08, -0.03], [0.06, -0.08]]


def Start(cont):
    own = cont.owner
    asteroid = Asteroids(own, 3)
    
def randomNumber():
    rand = choice(aList)
    return rand

def Update(cont):
    asteroid = cont.owner
    randNum = randomNumber()
    asteroid.AsteroidsMoveBotLeft(randNum[0], randNum[1])
