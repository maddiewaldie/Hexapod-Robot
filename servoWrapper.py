from servo import Servo, ServoCluster

class ServoWrapper:
    def __init__(self, servo_port, is_cluster=False, cluster_pins=None, cluster_pio=0, cluster_sm=0):
        self.is_cluster = is_cluster
        if self.is_cluster:
            if cluster_pins is None:
                raise ValueError("Cluster pins must be provided for a servo cluster.")
            self.cluster = ServoCluster(cluster_pio, cluster_sm, cluster_pins)
            self.servo_index = cluster_pins.index(servo_port)
            self.cluster.enable(self.servo_index)
        else:
            self.servo = Servo(servo_port)
            self.servo.enable()
    
    def enable(self):
        if self.is_cluster:
            self.cluster.enable(self.servo_index)
        else:
            self.servo.enable()
    
    def disable(self):
        if self.is_cluster:
            self.cluster.disable(self.servo_index)
        else:
            self.servo.disable()
    
    def value(self, val=None):
        if val is not None:
            if self.is_cluster:
                self.cluster.value(self.servo_index, val)
            else:
                self.servo.value(val)
        else:
            if self.is_cluster:
                return self.cluster.value(self.servo_index)
            else:
                return self.servo.value()
    
    def to_min(self):
        if self.is_cluster:
            self.cluster.to_min(self.servo_index)
        else:
            self.servo.to_min()
    
    def to_mid(self):
        if self.is_cluster:
            self.cluster.to_mid(self.servo_index)
        else:
            self.servo.to_mid()
    
    def to_max(self):
        if self.is_cluster:
            self.cluster.to_max(self.servo_index)
        else:
            self.servo.to_max()