from bge import logic


def CreateShip():
    scene = logic.getCurrentScene()
    scn_objs = scene.objects
    #print("objs=", scn_objs)
    ship = scene.addObject("ship", "invoked_ship", 0)
    print("ship=", ship.name)
    cannon = scn_objs["cannon"]
    print("cannon=", cannon.name)
    cannon.setParent(ship)


def Start(cont):
    own = cont.owner
    own["lifes"] = 3
    CreateShip()


def Update(cont):
    own = cont.owner
    col = cont.sensors["Collision"].positive
    if (col==True):
        own["lifes"] -= 1
        scene = logic.getCurrentScene()
        scn_objs = scene.objects
        ship = scn_objs["ship"]
        ship.endObject()
        CreateShip()
        if (own["lifes"]==0):
            scene.restart()