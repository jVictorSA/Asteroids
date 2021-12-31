from bge import logic, types


class Asteroids(types.KX_GameObject):
    def __init__(self, old_owner, lifes=int(3)):
        self.own = old_owner
        self.lifes = lifes
        self.acceleration = float(0.03)
        self.positions = [float(0.7), float(0.5)]
        self.angle_acceleration = float(0.06)
        self.angle = float(0.0)


    def AsteroidsMove(self):
        self.positions[0] += self.acceleration
        self.positions[1] += self.acceleration
        self.applyMovement([0, self.acceleration, 0], False)
        self.applyMovement([self.acceleration, self.acceleration, 0], False)
        #print("positions=[{}, {}]".format(self.positions[0], self.positions[1]))
        #print("getFrametime=", logic.getClockTime())