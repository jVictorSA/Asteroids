from bge import logic, events
from scripts.asteroids_system import Asteroids

def Start(cont):
    own = cont.owner
    asteroid = Asteroids(own, 3)
    asteroid.positions = [0.8,0.6]

def Update(cont):
    asteroid = cont.owner
    asteroid.AsteroidsMove()
    cene = logic.getCurrentScene()
    cene_ina_objs = cene.objects
    cene.addObject("Asteroide", "Asteroids_Field")
