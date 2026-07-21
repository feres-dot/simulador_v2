class Car:
    def __init__ (self, mass):
        self.mass = mass

        self.x = 0.0 # Distance (m)
        self.v = 0.0 # Speed (m/s)
        self.a = 0.0 # Acceleration (m/s^2
        
    def update_physics (self, force, dt):
        self.a = force/self.mass

        self.v += self.a * dt

        self.x = self.v * dt
        