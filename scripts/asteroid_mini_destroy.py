from bge import logic
from scripts.asteroidsLinkedList import Node
from scripts.asteroids_field import Node, asteroidsLinkedList

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
        
        scrore = int(0)
        with open(logic.expandPath("//score.txt"), 'r') as score_file:
            score = int(score_file.read())
        with open(logic.expandPath("//score.txt"), 'w') as score_file:
            score_file.write(str((score+1)))
        
        asteroid.endObject()
