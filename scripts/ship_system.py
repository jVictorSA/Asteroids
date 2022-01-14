from bge import logic, types


class Ship(types.KX_GameObject):
    def __init__(self, old_owner, lifes=int(3)):
        self.own = old_owner
        self.lifes = lifes
        self.force = [float(0.1), float(0.9), 0]
        self.acceleration = float(0.1)
        self.positions = [float(0.0), float(0.0), float(0.0)]
        self.max_velo = float(0.11)
        self.angle_acceleration = float(0.05)
        self.angle = float(0.0)
        self.wrap = True


    def TimeAction(self, time):
        if time>0.001:
            return [float(0.0), True]
        else:
            return [float(time), False]


    def ShipWrap(self, up, down):
        if (self.worldPosition[1]>6):
            #print('1')
            self.applyMovement([0, -2*self.worldPosition[1], 0], False)
        elif (self.worldPosition[1]<-6.2):
            #print('2')
            self.applyMovement([0, -2*self.worldPosition[1]-(0.3), 0], False)
        
        if (self.worldPosition[0]>8):
            #print('1')
            self.applyMovement([-2*self.worldPosition[0], 0, 0], False)
        elif (self.worldPosition[0]<-8.2):
            #print('2')
            self.applyMovement([-2*self.worldPosition[0]-(0.3), 0, 0], False)


    def ShipRotate(self, left, right, timer):
        if (left>0 and timer==True):
            self.angle += self.angle_acceleration
            self.applyRotation([0, 0, self.angle_acceleration], False)
        if (right>0 and timer==True):
            self.angle -= self.angle_acceleration
            self.applyRotation([0, 0, -self.angle_acceleration], False)


    def ShipMove(self, up, down, left, right, timer):
        if (up>0 and timer==True and self.positions[1]<self.max_velo):
            self.positions[1] += self.acceleration
            self.applyMovement([0, self.positions[1], 0], True)
            #self.applyForce(self.force, False)
        elif (timer==True and (self.positions[1]>float(0.0))):
            self.positions[1] -= self.acceleration
            self.applyMovement([0, self.positions[1], 0], True)
            #self.applyForce(self.force, False)
        
        if (down>0 and timer==True and self.positions[1]>-self.max_velo):
            self.positions[1] -= self.acceleration
            self.applyMovement([0, self.positions[1], 0], True)
            #self.applyForce(self.force, False)
        elif (timer==True and (self.positions[1]< float(0.0))):
            self.positions[1] += self.acceleration
            self.applyMovement([0, self.positions[1], 0], True)
            #self.applyForce(self.force, False)
        #if (self.positions[0]<self.acceleration) and (self.positions[1]<self.acceleration):
        self.ShipRotate(left, right, timer)
        '''
        if (left>0) and timer==True and self.positions[0]>-self.max_velo:
            self.positions[0] -= self.acceleration
            self.applyMovement([self.positions[0], 0, 0], False)
        elif (timer==True and self.positions[0]<float(0.0)):
            self.positions[0] += self.acceleration
            self.applyMovement([self.positions[0], 0, 0], False)
        if (right>0) and timer==True and self.positions[0]<self.max_velo:
            self.positions[0] += self.acceleration
            self.applyMovement([self.positions[0], 0, 0], False)
        elif (timer==True and self.positions[0]>float(0.0)):
            self.positions[0] -= self.acceleration
            self.applyMovement([self.positions[0], 0, 0], False)
        '''
        self.ShipWrap(up, down)
        #print("positions=[{}]".format(self.worldPosition))
        #print("getFrametime=", logic.getClockTime())