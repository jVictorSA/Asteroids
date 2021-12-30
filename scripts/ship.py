from bge import logic, events
from scripts.ship_system import Ship


def Start(cont):
    own = cont.owner
    ship = Ship(own, 3)


def Update(cont):
    ship = cont.owner

    keyboard = logic.keyboard.events
    #tap = logic.KX_INPUT_JUST_ACTIVATED
    w = keyboard[events.WKEY]
    a = keyboard[events.AKEY]
    s = keyboard[events.SKEY]
    d = keyboard[events.DKEY]
    #Tiros:
    left = keyboard[events.LEFTARROWKEY]
    right = keyboard[events.RIGHTARROWKEY]
    #print("w=", w)
    time = [float(0.0), bool(False)]
    time = ship.TimeAction(ship["time"])
    ship["time"] = time[0]
    ship.ShipMove(w, s, a, d, time[1])
    ship.ShipRotate(left, right, time[1])