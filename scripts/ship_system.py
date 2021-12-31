from bge import logic, types


class Ship(types.KX_GameObject):
    def __init__(self, old_owner, lifes=int(3)):
        self.own = old_owner
        self.lifes = lifes
        self.acceleration = float(0.0001)
        self.positions = [float(0.0), float(0.0)]
        self.max_velo = float(0.01)
        self.angle_acceleration = float(0.01)
        self.angle = float(0.0)


    def TimeAction(self, time):
        if time>0.001:
            return [float(0.0), True]
        else:
            return [float(time), False]


    def ShipMove(self, up, down, left, right, timer):
        if (up>0 and timer==True and self.positions[1]<self.max_velo):
            self.positions[1] += self.acceleration
            self.applyMovement([0, self.positions[1], 0], True)
        elif (timer==True and (self.positions[1]>float(0.0))):
            self.positions[1] -= self.acceleration
            self.applyMovement([0, self.positions[1], 0], True)

        if (down>0 and timer==True and self.positions[1]>-self.max_velo):
            self.positions[1] -= self.acceleration
            self.applyMovement([0, self.positions[1], 0], True)
        elif (timer==True and (self.positions[1]< float(0.0))):
            self.positions[1] += self.acceleration
            self.applyMovement([0, self.positions[1], 0], True)

        #print("positions=[{}, {}]".format(self.positions[0], self.positions[1]))
        #print("getFrametime=", logic.getClockTime())

    
    def ShipRotate(self, left, right, timer):
        if (left>0 and timer==True):
            self.angle += self.angle_acceleration
            self.applyRotation([0, 0, self.angle_acceleration], True)
        if (right>0 and timer==True):
            self.angle -= self.angle_acceleration
            self.applyRotation([0, 0, -self.angle_acceleration], True)