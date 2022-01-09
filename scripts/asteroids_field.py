from bge import logic, events, types
from scripts.asteroids_system import Asteroids

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
choice = 0

def Start(cont):
    own = cont.owner
    asteroid = Asteroids(own, 3)

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

class asteroidsTree:
    root = None

    def __init__(self):
        self.leftNode = None
        self.rightNode = None

    def insert(self, obj):
        if asteroidsTree.root == None:
            asteroidsTree.root = obj
            print(asteroidsTree.root)
        else:
            pass

asteroidCount = 0
tree1 = asteroidsTree(); tree2 = asteroidsTree(); tree3 = asteroidsTree(); tree4 = asteroidsTree()
tree5 = asteroidsTree(); tree6 = asteroidsTree(); tree7 = asteroidsTree(); tree8 = asteroidsTree()
tree9 = asteroidsTree(); tree10 = asteroidsTree()

def AsteroidsMax():
    if asteroidCount == 10:
        return 1
    else:
        return 0

def Update(cont):
    global asteroidCount
    asteroid = cont.owner
    scene = logic.getCurrentScene()
    scene_ina_objs = scene.objects
    botLeftAst  = SelectBotLeftAsteroid()
    topRightAst = SelectTopRightAsteroid()
    topLeftAst  = SelectTopLeftAsteroid()
    botRightAst = SelectBotRightAsteroid()
    #print(topRightAst)
    if AsteroidsMax() == 1:
        return
    scene.addObject(botLeftAst, "BottomLeft")
    asteroidCount += 1
    if AsteroidsMax() == 1:
        return
    obj = scene.addObject(botRightAst, "BottomRight")
    if tree1.root == None:
        tree1.insert(obj)
    print(tree1.root)
    '''
    elif tree2.root == None:
        tree2.insert(obj)
    elif tree3.root == None:
        tree3.insert(obj)
    '''
    asteroidCount += 1
    if AsteroidsMax() == 1:
        return
    scene.addObject(topRightAst, "TopRight")
    asteroidCount += 1
    if AsteroidsMax() == 1:
        return
    scene.addObject(topLeftAst, "TopLeft")
    asteroidCount += 1
