import time

import constants as const
from leg import Leg

class Hexapod:
    def __init__(self):
        self.legs = {
            const.LEFT_FRONT: Leg(const.LEFT_FRONT_DISTAL, const.LEFT_FRONT_MID, const.LEFT_FRONT_PROXIMAL, const.LEFT_FRONT),
            const.LEFT_MIDDLE: Leg(const.LEFT_MIDDLE_DISTAL, const.LEFT_MIDDLE_MID, const.LEFT_MIDDLE_PROXIMAL, const.LEFT_MIDDLE),
            const.LEFT_BACK: Leg(const.LEFT_BACK_DISTAL, const.LEFT_BACK_MID, const.LEFT_BACK_PROXIMAL, const.LEFT_BACK),
            const.RIGHT_FRONT: Leg(const.RIGHT_FRONT_DISTAL, const.RIGHT_FRONT_MID, const.RIGHT_FRONT_PROXIMAL, const.RIGHT_FRONT),
            const.RIGHT_MIDDLE: Leg(const.RIGHT_MIDDLE_DISTAL, const.RIGHT_MIDDLE_MID, const.RIGHT_MIDDLE_PROXIMAL, const.RIGHT_MIDDLE),
            const.RIGHT_BACK: Leg(const.RIGHT_BACK_DISTAL, const.RIGHT_BACK_MID, const.RIGHT_BACK_PROXIMAL, const.RIGHT_BACK, is_special=True),
        }

    def moveAllToHome(self):
        for leg in self.legs.values():
            leg.moveToHome()

    def moveLeg(self, leg, joint, value):
        if joint == const.DISTAL:
            self.legs[leg].moveJoint(self.legs[leg].distal_servo, value)
        elif joint == const.MID:
            self.legs[leg].moveJoint(self.legs[leg].mid_servo, value)
        elif joint == const.PROXIMAL:
            self.legs[leg].moveJoint(self.legs[leg].proximal_servo, value)

    def moveLegForward(self, leg):
        self.moveLeg(leg, const.DISTAL, -25)
        self.moveLeg(leg, const.MID, -25)
        time.sleep(1)
        self.moveLeg(leg, const.PROXIMAL, 25)
        time.sleep(1)
        self.moveLeg(leg, const.DISTAL, 0)
        self.moveLeg(leg, const.MID, 0)
        time.sleep(1)

    def moveLeftSideForward(self):
        self.moveLegForward(const.LEFT_FRONT)
        self.moveLegForward(const.LEFT_MIDDLE)
        self.moveLegForward(const.LEFT_BACK)
    
    def moveRightSideForward(self):
        self.moveLegForward(const.RIGHT_FRONT)
        self.moveLegForward(const.RIGHT_MIDDLE)
        self.moveLegForward(const.RIGHT_BACK)
        self.moveLegForward(const.RIGHT_FRONT)
        self.moveLegForward(const.RIGHT_MIDDLE)
        self.moveLegForward(const.RIGHT_BACK)