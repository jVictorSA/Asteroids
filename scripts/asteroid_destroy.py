from bge import logic


def Update(cont):
    asteroid = cont.owner
    scene = logic.getCurrentScene()
    
    col = cont.sensors["Collision"].positive
    print("MAIN, col=", col)
    if col==True:
        print("POSITIVE")
        scene.addObject("asteroid_mini", asteroid)
        scene.addObject("asteroid_mini", asteroid)
        scene.addObject("asteroid_mini", asteroid)
        asteroid.endObject()