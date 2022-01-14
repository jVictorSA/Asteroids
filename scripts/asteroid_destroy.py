from bge import logic
from scripts.asteroidsLinkedList import Node
from scripts.asteroids_field import asteroidsLinkedList

miniAsteroids = ["asteroid_mini0", "asteroid_mini1", "asteroid_mini2", "asteroid_mini3", "asteroid_mini4",
                 "asteroid_mini5", "asteroid_mini6"]

choice = 0

def SelectMiniAsteroid():
    global choice
    if choice > 6:
        choice = 0
    
    choice += 1

    return miniAsteroids[choice-1]

def Update(cont):
    asteroid = cont.owner
    scene = logic.getCurrentScene()
    
    col = cont.sensors["Collision"].positive
    #print("Level 1, col=", col, "name=", asteroid.name)
    if col==True:
        #print("POSITIVE")
        #print("Level 2")
        scene.addObject(SelectMiniAsteroid(), asteroid)
        scene.addObject(SelectMiniAsteroid(), asteroid)
        scene.addObject(SelectMiniAsteroid(), asteroid)
        scene.addObject(SelectMiniAsteroid(), asteroid)
        #commented because cause malfunction of the code.
        #need further research to function properly as intended
        #asteroid["linkedList"].printList()
        asteroid.endObject()