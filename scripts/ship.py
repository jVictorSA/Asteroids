from bge import logic, events
from scripts.ship_system import Ship


def Start(cont):
    own = cont.owner
    own["lifes"] = 3
    ship = Ship(own, 3)
    


def Update(cont):
    ship = cont.owner

    keyboard = logic.keyboard.events
    
    w = keyboard[events.WKEY]
    a = keyboard[events.AKEY]
    s = keyboard[events.SKEY]
    d = keyboard[events.DKEY]
    
    left = keyboard[events.LEFTARROWKEY]
    right = keyboard[events.RIGHTARROWKEY]
    #print("w=", w)
    time = [float(0.0), bool(False)]
    time = ship.TimeAction(ship["time"])
    ship["time"] = time[0]
    ship.ShipMove(w, s, left, right, time[1])
    #ship.ShipRotate(left, right, time[1])

    ship.LevelManagement()
    tap = logic.KX_INPUT_JUST_ACTIVATED
    enter = keyboard[events.ENTERKEY] == tap
    scene = logic.getCurrentScene()
    if (enter==True):
        #scene_ina_objs = scene.objects
        if (ship.level==1):
            scene.addObject("bullet", "ship")
        elif (ship.level==2):
            bullet1=scene.addObject("bullet", "ship")
            bullet1.applyRotation([0.0, 0.0, ship.angle_attack], False)
            bullet2=scene.addObject("bullet", "ship")
            bullet2.applyRotation([0.0, 0.0, -ship.angle_attack], False)
        elif (ship.level==3):
            bullet1=scene.addObject("bullet", "ship")
            bullet1.applyRotation([0.0, 0.0, ship.angle_attack], False)
            bullet2=scene.addObject("bullet", "ship")
            bullet2.applyRotation([0.0, 0.0, -ship.angle_attack], False)
            bullet3=scene.addObject("bullet", "ship")
    #For script invoked_ship.py:
    #ship["posx"] = ship.positions[0]
    #ship["posy"] = ship.positions[1]

    red = bool(cont.sensors["red"].positive)
    green = bool(cont.sensors["green"].positive)
    blue = bool(cont.sensors["blue"].positive)
    white = bool(cont.sensors["white"].positive)
    if (red==True):
        with open(logic.expandPath("//color.txt"), 'w') as color_file:
            color_file.write("1")
        cont.activate(cont.actuators["restart_Scene"])
        #scene.end()
    elif (green==True):
        with open(logic.expandPath("//color.txt"), 'w') as color_file:
            color_file.write("2")
        cont.activate(cont.actuators["restart_Scene"])
        #scene.end()
    elif (blue==True):
        with open(logic.expandPath("//color.txt"), 'w') as color_file:
            color_file.write("3")
        cont.activate(cont.actuators["restart_Scene"])
        #scene.end()
    elif (white==True):
        with open(logic.expandPath("//color.txt"), 'w') as color_file:
            color_file.write("4")
        cont.activate(cont.actuators["restart_Scene"])
        #scene.end()