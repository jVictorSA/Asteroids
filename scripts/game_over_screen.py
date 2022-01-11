from bge import logic, events


def Start(cont):
    pass


def Update(cont):
    #print("AQUI")
    keyboard = logic.keyboard.events
    tap = logic.KX_INPUT_JUST_ACTIVATED

    enter = keyboard[events.ENTERKEY]==tap

    #scn_list = logic.getSceneList()
    #index_scene = int(0)
    #for i in range(len(scn_list)):
       # if scn_list[i] == "Scene":
            #index_scene = i
            #break
    
    if enter==True:
        add_scene = cont.actuators["add_Scene"]
        cont.activate(add_scene)
        re_go = cont.actuators["re_game_over"]
        cont.activate(re_go)