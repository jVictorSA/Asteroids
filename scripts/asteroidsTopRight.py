from bge import logic, types
from scripts.asteroids_system import Asteroids

def Start(cont):
    own = cont.owner
    asteroid = Asteroids(own, 3)

def Update0(cont):
    asteroid = cont.owner
    asteroid.AsteroidsMoveTopRight0()

def Update1(cont):
    asteroid = cont.owner
    asteroid.AsteroidsMoveTopRight1()

def Update2(cont):
    asteroid = cont.owner
    asteroid.AsteroidsMoveTopRight2()
    
def Update3(cont):
    asteroid = cont.owner
    asteroid.AsteroidsMoveTopRight3()

def Update4(cont):
    asteroid = cont.owner
    asteroid.AsteroidsMoveTopRight4()

def Update5(cont):
    asteroid = cont.owner
    asteroid.AsteroidsMoveTopRight5()
