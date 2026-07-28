import math
from tire import Tire

class Car:
    def __init__ (self, mass, torque, wheel_radius, gear_ratios, final_drive, cd, frontal_area, air_density, max_rpm):
        
        self.mass = mass # Kilograms
        self.torque = torque #Newton meter
        self.wheel_radius = wheel_radius # Meters
        self.gear_ratios = gear_ratios
        self.final_drive = final_drive


        self.x = 0.0 # Distance (m)
        self.v = 0.0 # Speed (m/s)
        self.a = 0.0 # Acceleration (m/s^2)

        self.cd = cd
        self.frontal_area = frontal_area
        self.air_density = air_density

        self.max_rpm = max_rpm

        self.rpm = 0.0

        self.current_gear_index = 0 
        self.current_gear = 0.0

        self.brake_force = 12000
        self.is_braking = False

        weight_per_tire = (self.mass * 9.81) / 4
        self.tires = [Tire(1.0, weight_per_tire) for _ in range(4)]

    def update_physics (self, dt):

            current_rpm = self.calculate_rpm()
            max_grip = self.get_total_grip()

            if current_rpm > self.max_rpm - 200 and self.current_gear_index < len(self.gear_ratios)-1:

                self.current_gear_index += 1

    
            drag_force = self.calculate_drag_force()

            if self.is_braking == False:
                traction_force = self.calculate_traction_force()
                force = traction_force - drag_force
            else:
                traction_force = 0
                current_brake_force = self.brake_force
                if current_brake_force >= max_grip:
                    current_brake_force = max_grip
                force = traction_force - drag_force - current_brake_force
    
            self.a = force /self.mass
    
            self.v += self.a * dt

            if self.v <= 0:
                self.v = 0
                self.a = 0
                self.rpm = 800
    
            self.x += self.v * dt



    def calculate_drag_force(self):

        drag_force = 0.5 * self.air_density * self.cd * self.frontal_area * (self.v **2)

        return drag_force
    

    def calculate_rpm(self):
        if self.v != 0:
            self.rpm = ((self.v)/(2*math.pi*self.wheel_radius))*self.gear_ratios[self.current_gear_index]*self.final_drive*60
        else:
            self.rpm = 800 #Relenti RPMs

        return self.rpm
    
        
    def calculate_traction_force(self):

        max_grip = self.get_total_grip()
        engine_rpm = self.calculate_rpm()

        if engine_rpm < self.max_rpm:

            # 0.85 represents the looses of mechanical friction and all mechanisims from the engine till reach out the wheels
            
            traction_force = ((self.torque * self.gear_ratios[self.current_gear_index] * self.final_drive) / self.wheel_radius) * 0.85

        else:  #RPMs limit to protect the engine

            traction_force = 0

        if traction_force >= max_grip:

            traction_force = max_grip

        return traction_force 

    def get_total_grip(self):
        max_grip = 0
        for tire in self.tires:
            max_grip += tire.get_max_grip()
        return max_grip
            

    
    
        