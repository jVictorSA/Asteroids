from bge import logic, events, types
from scripts.asteroids_system import Asteroids
from scripts.asteroidsLinkedList import Node, asteroidsLinkedList

botLeftList = [ "AsteroideBotLeft0", "AsteroideBotLeft1",
                "AsteroideBotLeft2", "AsteroideBotLeft3",
                "AsteroideBotLeft4", "AsteroideBotLeft5"]

botRightList = ["AsteroideBotRight0", "AsteroideBotRight1",
                "AsteroideBotRight2", "AsteroideBotRight3",
                "AsteroideBotRight4", "AsteroideBotRight5"]

topLeftList = [ "AsteroideTopLeft0", "AsteroideTopLeft1",
                "AsteroideTopLeft2", "AsteroideTopLeft3",
                "AsteroideTopLeft4", "AsteroideTopLeft5"]

topRightList = ["AsteroideTopRight0", "AsteroideTopRight1",
                "AsteroideTopRight2", "AsteroideTopRight3",
                "AsteroideTopRight4", "AsteroideTopRight5"]

#variable for selection of asteroids
choice = 0

def SelectBotLeftAsteroid():
    global choice
    if choice > 5:
        choice = 0
    
    choice += 1

    return botLeftList[choice-1]

def SelectTopLeftAsteroid():
    global choice
    if choice > 5:
        choice = 0
    
    choice += 1

    return topLeftList[choice-1]

def SelectBotRightAsteroid():
    global choice
    if choice > 5:
        choice = 0
    
    choice += 1

    return botRightList[choice-1]

def SelectTopRightAsteroid():
    global choice
    if choice > 5:
        choice = 0
    
    choice += 1
    return topRightList[choice-1]

#counter to track how many asteroids were cast in the scene
asteroidCount = 0

def AsteroidsMax():
    if asteroidCount == 10:
        return 1
    else:
        return 0


def Start(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    
    botLeftAst  = SelectBotLeftAsteroid()
    botRightAst = SelectBotRightAsteroid()
    topRightAst = SelectTopRightAsteroid()
    topLeftAst  = SelectTopLeftAsteroid()
    
    #own["linkedList"] = scene.addObject("asteroidsLinkedList", own)

    own["asteroid1"] = scene.addObject(botLeftAst, "BottomLeft")
    botLeftNode = Node(own["asteroid1"])
    asteroidsLinkedList.insertFront(botLeftNode)
    
    own["asteroid2"] = scene.addObject(botRightAst, "BottomRight")
    botRightNode = Node(own["asteroid2"])
    asteroidsLinkedList.insertBack(botRightNode)
    
    own["asteroid3"] = scene.addObject(topRightAst, "TopRight")
    topRightNode = Node(own["asteroid3"])
    asteroidsLinkedList.insertBack(topRightNode)

    own["asteroid4"] = scene.addObject(topLeftAst, "TopLeft")
    topLeftNode = Node(own["asteroid4"])
    
    asteroidsLinkedList.insertBetween(botRightNode,topLeftNode)
    asteroidsLinkedList.printList()
    asteroidsLinkedList.deleteNode(botRightNode, botLeftNode)
    print("\n")
    asteroidsLinkedList.printList()

    asteroid = Asteroids(own, 3)


def Update(cont):
    global asteroidCount
    asteroid = cont.owner
        
