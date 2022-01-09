from bge import logic


def Update(cont):
    asteroid = cont.owner
    scene = logic.getCurrentScene()
    
    col = cont.actuators["Collision"]
    print("MAIN")
    if col.positive==True:
        print("POSITIVE")
        scene.addObject("asteroid_mini", asteroid)
        scene.addObject("asteroid_mini", asteroid)
        scene.addObject("asteroid_mini", asteroid)
        asteroid.endObject()