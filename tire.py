import math

class Tire:
    def __init__(self, traction_coef, vertical_load, radius, inertia):

        self.traction_coef = traction_coef
        self.vertical_load = vertical_load
        self.radius = radius
        self.inertia = inertia

        self.angular_velocity = 0.0 #rad/s

        #Longitudinal Pacejka Coeficients
        self.B = 10.0 #Stifness
        self.C = 1.65 #Shape
        self.E = 0.97 #Grip lost

        #Lateral Pacejka Coeficients
        self.B_lat = 12.0 # Stifness (More compared with the longitudinal coeficient)
        self.C_lat = 1.30 # Shape
        self.E_lat = -1.0 # Grip loss (Softer fall)

    def get_max_grip(self):

        max_grip = self.vertical_load * self.traction_coef

        return max_grip

    #Method to get the updated load depending on the load transfer

    def update_load(self, new_load):
        self.vertical_load = new_load

    #Method to get the speed of the wheel, independent from the engine torque

    def update_spin (self, net_torque, dt):

        angular_aceleration = net_torque / self.inertia

        self.angular_velocity += angular_aceleration * dt


    def get_pacejka_force (self, car_velocity):

        D = self.get_max_grip()

        wheel_linear_velocity = self.angular_velocity * self.radius
        
        slip_ratio = (wheel_linear_velocity - car_velocity) / max(abs(car_velocity), 0.1)

        force = D * math.sin(self.C * math.atan(self.B * slip_ratio - self.E * (self.B * slip_ratio - math.atan(self.B * slip_ratio))))

        return force

    def get_pacejka_lateral_force (self, slip_angle):

        D = self.get_max_grip()
        
        force = D * math.sin(self.C_lat * math.atan(self.B_lat * slip_angle - self.E_lat * (self.B_lat * slip_angle - math.atan(self.B_lat * slip_angle))))
        
        return force


