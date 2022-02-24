from bge import logic
import random


def CreateShip():
    #DEPRECATED
    scene = logic.getCurrentScene()
    scn_objs = scene.objects
    #print("objs=", scn_objs)
    ship = scene.addObject("ship1", "invoked_ship", 0)
    #print("ship=", ship.name)
    return ship
    

def ChoiceMaxTimePortal(cont):
    time_list = [4, 5, 6, 7, 8]
    return random.choice(time_list)

def Start(cont):
    own = cont.owner
    with open(logic.expandPath("//lifes.txt"), 'w') as lifes:
        lifes.write('3')
    #with open(logic.expandPath("//score.txt"), 'w') as score_file:
        #score_file.write('0')
    #CreateShip()
    own["max_time_portal"] = ChoiceMaxTimePortal(cont)
    own["portal_on"] = bool(False)


def Update(cont):
    own = cont.owner
    
    scene = logic.getCurrentScene()
    scn_objs = scene.objects
    ship = scn_objs["ship"]
    #cannon = scn_objs["cannon"]
    #cannon.applyMovement([ship["posx"], ship["posy"], 0], False)

    with open(logic.expandPath("//lifes.txt"), 'r') as lfs:
        lifes = lfs.read()
        scn_objs["lifes"]["Text"] = "Space Ships: "+lifes
    
    with open(logic.expandPath("//score.txt"), 'r') as score_file:
        score = score_file.read()
        scn_objs["score"]["Text"] = "Score: "+score


    if (own["portal_on"]==False and own["timer_portal"]>own["max_time_portal"]):
        own["portal_on"] = True
        portal_reference = ["invoked_1_portal", "invoked_2_portal", "invoked_3_portal"]
        portal_ref_choice = random.choice(portal_reference)
        portal_list = ["portal_red", "portal_green", "portal_blue", "portal_white"]
        portal_choice = random.choice(portal_list)
        scene.addObject(portal_choice, portal_ref_choice, 0)


    col = cont.sensors["Collision"].positive
    if (col==True) and (own["timer_invencible"]>float(3.0)):
        lifes = int(0)
        with open(logic.expandPath("//lifes.txt"), 'r') as lfs:
            l = lfs.read()
            #print("llifes=", l)
            lifes = int(l)-1
        with open(logic.expandPath("//lifes.txt"), 'w') as lfs:
            lfs.write(str(lifes))
        #print("lifes=", lifes)
        ship.applyMovement([-ship.worldPosition[0], -ship.worldPosition[1], 0], False)
        if (lifes<=int(0)):
            act = cont.actuators["add_game_over"]
            cont.activate(act)
            re_Scene = cont.actuators["re_Scene"]
            cont.activate(re_Scene)
        own["timer_invencible"] = float(0.0)

