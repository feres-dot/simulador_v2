class Car:
    def __init__ (self, mass, torque, wheel_radius, gear_ratio, final_drive):
        
        self.mass = mass # Kilograms
        self.torque = torque #Newton meter
        self.wheel_radius = wheel_radius # Meters
        self.gear_ratio = gear_ratio
        self.final_drive = final_drive


        self.x = 0.0 # Distance (m)
        self.v = 0.0 # Speed (m/s)
        self.a = 0.0 # Acceleration (m/s^2)

        
    def calculate_traction_force(self):

        # 0.85 represents the looses of mechanical friction and all mechanisims from the engine till reach out the wheels
        
        traction_force = ((self.torque * self.gear_ratio * self.final_drive) / self.wheel_radius) * 0.85

        return traction_force 

        
    def update_physics (self, dt):

        force = self.calculate_traction_force()
        self.a = force /self.mass

        self.v += self.a * dt

        self.x += self.v * dt
        