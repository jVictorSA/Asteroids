from bge import logic, events
from scripts.asteroids_system import Asteroids

def Start(cont):
    own = cont.owner
    asteroid = Asteroids(own, 3)

def Update(cont):
    asteroid = cont.owner
    scene = logic.getCurrentScene()
    scene_ina_objs = scene.objects
    scene.addObject("AsteroideBotLeft", "BottomLeft")
    scene.addObject("AsteroideBotRight", "BottomRight")
    scene.addObject("AsteroideTopRight", "TopRight")
    scene.addObject("AsteroideTopLeft", "TopLeft")
