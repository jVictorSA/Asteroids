from bge import logic, types
#from ship_system.Ship import ShipWrap


class Asteroids(types.KX_GameObject):
    def __init__(self, old_owner, lifes=int(3)):
        self.own = old_owner
        self.lifes = lifes
        self.acceleration = float(0.03)
        self.positions = [float(0), float(244.5)]
        self.angle_acceleration = float(0.06)
        self.angle = float(0.0)
        #seed(1)
        self.randomNumber = [float(0), float(0)]


    def AsteroidsInit(self):
        self.positions

    def AsteroidsMoveBotLeft(self, randx, randy):
        #print(self.randomNumber[0], self.randomNumber[1])
        #print(randx, randy)
        self.applyMovement([0, randy, 0], False)
        self.applyMovement([randx, 0, 0], False)
    
    def AsteroidsMoveBotRight(self, randx, randy):
        self.applyMovement([0, randy, 0], False)
        self.applyMovement([randx, 0, 0], False)

    def AsteroidsMoveTopRight(self, randx, randy):
        self.applyMovement([0, randy, 0], False)
        self.applyMovement([randx, 0, 0], False)
    
    def AsteroidsMoveTopLeft(self, randx, randy):
        self.applyMovement([0, randy, 0], False)
        self.applyMovement([randx, 0, 0], False)