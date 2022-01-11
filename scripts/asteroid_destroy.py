from bge import logic


def Update(cont):
    asteroid = cont.owner
    scene = logic.getCurrentScene()
    
    col = cont.sensors["Collision"].positive
    #print("Level 1, col=", col, "name=", asteroid.name)
    if col==True:
        #print("POSITIVE")
        #print("Level 2")
        scene.addObject("asteroid_mini", asteroid)
        scene.addObject("asteroid_mini", asteroid)
        scene.addObject("asteroid_mini", asteroid)
        asteroid.endObject()