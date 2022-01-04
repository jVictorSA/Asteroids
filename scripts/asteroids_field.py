from bge import logic, events
from scripts.asteroids_system import Asteroids

def Start(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    scene_ina_objs = scene.objects
    scene.addObject("Asteroide", "Asteroids_Field")
    asteroid = Asteroids(own, 3)
    asteroid.positions = [0.8,0.6]

def Update(cont):
    asteroid = cont.owner
    asteroid.AsteroidsMove()
