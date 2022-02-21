from bge import logic, events


def Start(cont):
    score = int(0)
    with open(logic.expandPath("//score.txt"), 'r') as score_file:
        score = int(score_file.read())

    scene_objs = logic.getCurrentScene().objects
    scene_objs["score_game_over"]["Text"] = "Final score: "+str(score)
    

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
        with open(logic.expandPath("//score.txt"), 'w') as score_file:
            score_file.write("0")
        add_scene = cont.actuators["add_Scene"]
        cont.activate(add_scene)
        re_go = cont.actuators["re_game_over"]
        cont.activate(re_go)