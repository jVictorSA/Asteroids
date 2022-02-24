from bge import logic, types
#from movementLists import BotLeftList0, BotLeftList1, BotLeftList2, BotLeftList3, BotLeftList4, BotLeftList5
#from movementLists import TopLeftList0, TopLeftList1, TopLeftList2, TopLeftList3, TopLeftList4, TopLeftList5
#from movementLists import BotRightList0, BotRightList1, BotRightList2, BotRightList3, BotRightList4, BotRightList5
#from movementLists import TopRightList0, TopRightList1, TopRightList2, TopRightList3, TopRightList4, TopRightList5

BotLeftList0 = [0.03,   0.5]; BotLeftList1 = [0.05,  0.07]; BotLeftList2 = [0.02,  0.08]; BotLeftList3 = [0.09,  0.06]; BotLeftList4 = [0.04,  0.07]; BotLeftList5 = [0.08,  0.03]

BotRightList0 = [-0.02,   0.5]; BotRightList1 = [-0.05,  0.04]; BotRightList2 = [-0.02,  0.03]; BotRightList3 = [-0.09,  0.06]; BotRightList4 = [-0.06,  0.07]; BotRightList5 = [-0.02,  0.09]

TopLeftList0 = [0.03,   -0.5]; TopLeftList1 = [0.05,  -0.01]; TopLeftList2 = [0.02,  -0.03]; TopLeftList3 = [0.09,  -0.06]; TopLeftList4 = [0.04,  -0.02]; TopLeftList5 = [0.08,  -0.08]

TopRightList0 = [-0.02,   -0.5]; TopRightList1 = [-0.05,  -0.07]; TopRightList2 = [-0.02,  -0.06]; TopRightList3 = [-0.09,  -0.02]; TopRightList4 = [-0.06,  -0.08]; TopRightList5 = [-0.02,  -0.03]


class Asteroids(types.KX_GameObject):
    def __init__(self, old_owner, lifes=int(3)):
        self.own = old_owner
        self.lifes = lifes
        self.acceleration = float(0.03)
        self.positions = [float(0), float(244.5)]
        self.angle_acceleration = float(0.06)
        self.angle = float(0.0)
        self.wrap = True
        with open(logic.expandPath("//color.txt"), 'r') as color_file:
            c = int(color_file.read())
            if c==1:
                self.color = [1,0,0,0]
            elif (c==2):
                self.color = [0,1,0,0]
            elif (c==3):
                self.color = [0,0,1,0]
            elif (c==4):
                self.color = [0,0,0,0]


    def AsteroidsWrap(self):
        if (self.worldPosition[1]>6):
            self.applyMovement([0, -2*self.worldPosition[1], 0], False)
        elif (self.worldPosition[1]<-6.2):
            self.applyMovement([0, -2*self.worldPosition[1]-(0.3), 0], False)
        
        if (self.worldPosition[0]>8):
            self.applyMovement([-2*self.worldPosition[0], 0, 0], False)
        elif (self.worldPosition[0]<-8.2):
            self.applyMovement([-2*self.worldPosition[0]-(0.3), 0, 0], False)

    def AsteroidsMoveBotLeft0(self):
        #print(aList0[0], aList0[1])
        self.applyMovement([0, BotLeftList0[1], 0], False)
        self.applyMovement([BotLeftList0[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveBotLeft1(self):
        #print(aList1[0], aList1[1])
        self.applyMovement([0, BotLeftList1[1], 0], False)
        self.applyMovement([BotLeftList1[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveBotLeft2(self):
        #print(aList1[0], aList1[1])
        self.applyMovement([0, BotLeftList2[1], 0], False)
        self.applyMovement([BotLeftList2[0], 0, 0], False)
        self.AsteroidsWrap()
    
    def AsteroidsMoveBotLeft3(self):
        #print(aList1[0], aList1[1])
        self.applyMovement([0, BotLeftList3[1], 0], False)
        self.applyMovement([BotLeftList3[0], 0, 0], False)
        self.AsteroidsWrap()
    
    def AsteroidsMoveBotLeft4(self):
        #print(aList4[0], aList4[1])
        self.applyMovement([0, BotLeftList4[1], 0], False)
        self.applyMovement([BotLeftList4[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveBotLeft5(self):
        #print(aList5[0], aList5[1])
        self.applyMovement([0, BotLeftList5[1], 0], False)
        self.applyMovement([BotLeftList5[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveBotRight0(self):
        self.applyMovement([0, BotRightList0[1], 0], False)
        self.applyMovement([BotRightList0[0], 0, 0], False)
        self.AsteroidsWrap()
    
    def AsteroidsMoveBotRight1(self):
        self.applyMovement([0, BotRightList1[1], 0], False)
        self.applyMovement([BotRightList1[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveBotRight2(self):
        self.applyMovement([0, BotRightList2[1], 0], False)
        self.applyMovement([BotRightList2[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveBotRight3(self):
        self.applyMovement([0, BotRightList3[1], 0], False)
        self.applyMovement([BotRightList3[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveBotRight4(self):
        self.applyMovement([0, BotRightList4[1], 0], False)
        self.applyMovement([BotRightList4[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveBotRight5(self):
        self.applyMovement([0, BotRightList5[1], 0], False)
        self.applyMovement([BotRightList5[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopRight0(self):
        self.applyMovement([0, TopRightList0[1], 0], False)
        self.applyMovement([TopRightList0[0], 0, 0], False)
        self.AsteroidsWrap()
    
    def AsteroidsMoveTopRight1(self):
        self.applyMovement([0, TopRightList1[1], 0], False)
        self.applyMovement([TopRightList1[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopRight2(self):
        self.applyMovement([0, TopRightList2[1], 0], False)
        self.applyMovement([TopRightList2[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopRight3(self):
        self.applyMovement([0, TopRightList3[1], 0], False)
        self.applyMovement([TopRightList3[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopRight4(self):
        self.applyMovement([0, TopRightList4[1], 0], False)
        self.applyMovement([TopRightList4[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopRight5(self):
        self.applyMovement([0, TopRightList5[1], 0], False)
        self.applyMovement([TopRightList5[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopLeft0(self):
        self.applyMovement([0, TopLeftList0[1], 0], False)
        self.applyMovement([TopLeftList0[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopLeft1(self):
        self.applyMovement([0, TopLeftList1[1], 0], False)
        self.applyMovement([TopLeftList1[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopLeft2(self):
        self.applyMovement([0, TopLeftList2[1], 0], False)
        self.applyMovement([TopLeftList2[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopLeft3(self):
        self.applyMovement([0, TopLeftList3[1], 0], False)
        self.applyMovement([TopLeftList3[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopLeft4(self):
        self.applyMovement([0, TopLeftList4[1], 0], False)
        self.applyMovement([TopLeftList4[0], 0, 0], False)
        self.AsteroidsWrap()

    def AsteroidsMoveTopLeft5(self):
        self.applyMovement([0, TopLeftList5[1], 0], False)
        self.applyMovement([TopLeftList5[0], 0, 0], False)
        self.AsteroidsWrap()