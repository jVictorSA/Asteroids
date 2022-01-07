from bge import logic, types
from scripts.asteroids_system import Asteroids

def Start(cont):
    own = cont.owner
    asteroid = Asteroids(own, 3)

def Update(cont):
    asteroid = cont.owner
    asteroid.AsteroidsMoveTopLeft()
