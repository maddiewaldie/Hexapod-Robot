import constants as const
from servoWrapper import ServoWrapper

class Leg:
    def __init__(self, distal_port, mid_port, proximal_port, location, is_special=False):
        self.location = location
        self.is_special = is_special
        if self.is_special:
            self.distal_servo = ServoWrapper(distal_port, is_cluster=True, cluster_pins=[distal_port, distal_port + 1])
            self.mid_servo = ServoWrapper(mid_port, is_cluster=True, cluster_pins=[mid_port, mid_port + 1])
            self.proximal_servo = ServoWrapper(proximal_port)
        else:
            self.distal_servo = ServoWrapper(distal_port)
            self.mid_servo = ServoWrapper(mid_port)
            self.proximal_servo = ServoWrapper(proximal_port)

    def enableServos(self):
        self.distal_servo.enable()
        self.mid_servo.enable()
        self.proximal_servo.enable()

    def disableServos(self):
        self.distal_servo.disable()
        self.mid_servo.disable()
        self.proximal_servo.disable()

    def homeJoint(self, servo):
        servo.value(0)

    def moveJoint(self, servo, position):
        servo.value(position)

    def moveToHome(self):
        self.homeJoint(self.distal_servo)
        self.homeJoint(self.mid_servo)
        self.homeJoint(self.proximal_servo)

    def incrementJoint(self, joint, increment):
        if joint == const.DISTAL:
            self.distal_position = max(min(self.distal_position + increment, 90), -90)
            self.moveJoint(self.distal_servo, self.distal_position)
        elif joint == const.MID:
            self.mid_position = max(min(self.mid_position + increment, 90), -90)
            self.moveJoint(self.mid_servo, self.mid_position)
        elif joint == const.PROXIMAL:
            self.proximal_position = max(min(self.proximal_position + increment, 90), -90)
            self.moveJoint(self.proximal_servo, self.proximal_position)