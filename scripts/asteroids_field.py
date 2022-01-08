from bge import logic, events
from scripts.asteroids_system import Asteroids

def Start(cont):
    own = cont.owner
    own["invoked4"] = True
    asteroid = Asteroids(own, 3)


def Update(cont):
    field = cont.owner
    scene = logic.getCurrentScene()
    scene_ina_objs = scene.objects
    #asteroids = []
    if (field["invoked4"]==True):
        scene.addObject("AsteroideBotLeft", "BottomLeft")
        scene.addObject("AsteroideBotRight", "BottomRight")
        scene.addObject("AsteroideTopRight", "TopRight")
        scene.addObject("AsteroideTopLeft", "TopLeft")
        field["invoked4"] = False