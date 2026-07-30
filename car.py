import math
from tire import Tire

class Car:
    def __init__ (self, mass, torque, wheel_radius, 
                  gear_ratios, final_drive, 
                  cd, frontal_area, air_density, 
                  max_rpm, cg_height, wheelbase):
        
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
        self.front_tires = [Tire(1.0, weight_per_tire,self.wheel_radius, 1.5) for _ in range(2)]
        self.rear_tires = [Tire(1.0, weight_per_tire, self.wheel_radius, 1.5) for _ in range(2)]

        self.cg_height = cg_height
        self.wheelbase = wheelbase

    def update_physics (self, dt):

        self.update_weight_transfer()

        current_rpm = self.calculate_rpm()

        if current_rpm > self.max_rpm - 200 and self.current_gear_index < len(self.gear_ratios)-1:
            self.current_gear_index += 1

        if self.is_braking == False:

            drive_torque = self.calculate_drive_torque()

            engine_torque_per_wheel = drive_torque/2

            brake_torque_per_wheel = 0

        else:

            engine_torque_per_wheel = 0

            brake_torque = self.brake_force * self.wheel_radius

            brake_torque_per_wheel = brake_torque / 4

        total_traction_force = 0.0


        for tire in self.front_tires:   #Front Tires Physics (Spin and Brake, do not drive the car)
        
            force = tire.get_pacejka_force(self.v)
            total_traction_force += force
            road_torque = force * self.wheel_radius
            net_torque = 0 - brake_torque_per_wheel - road_torque
            tire.update_spin(net_torque, dt)

            #clamping to prevent reverse speed

            if self.is_braking and tire.angular_velocity < 0:
                tire.angular_velocity = 0

        for tire in self.rear_tires:   #Rear Tires Physics (Spin, Brake and Drive the car)

            force = tire.get_pacejka_force(self.v)
            total_traction_force += force
            road_torque = force * self.wheel_radius
            net_torque = engine_torque_per_wheel - brake_torque_per_wheel - road_torque
            tire.update_spin(net_torque,dt)

            #clamping to prevent reverse speed

            if self.is_braking and tire.angular_velocity < 0:
                tire.angular_velocity = 0

        
        drag_force = self.calculate_drag_force()
        force = total_traction_force - drag_force
        self.a = force / self.mass
    
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
        wheel_rpm = self.rear_tires[0].angular_velocity * (60 / (2 * math.pi))
        
        self.rpm = wheel_rpm * self.gear_ratios[self.current_gear_index] * self.final_drive
        
        if self.rpm < 800:
            self.rpm = 800
            
        return self.rpm
    
        
    def calculate_drive_torque(self):

        engine_rpm = self.calculate_rpm()

        if engine_rpm < self.max_rpm:

            # 0.85 represents the looses of mechanical friction and all mechanisims from the engine till reach out the wheels
            
            drive_torque = ((self.torque * self.gear_ratios[self.current_gear_index] * self.final_drive)) * 0.85

        else:  #RPMs limit to protect the engine

            drive_torque = 0

        return drive_torque

    def get_total_grip(self):
        max_grip = 0
        for tire in self.front_tires:
            max_grip += tire.get_max_grip()
        for tire in self.rear_tires:
            max_grip += tire.get_max_grip()
        return max_grip
    
    def update_weight_transfer(self):
        load_transfer = (self.mass * self.a * (self.cg_height/self.wheelbase))
        front_tires_weight = (self.mass * 9.81 / 2) - load_transfer
        rear_tires_weight = (self.mass * 9.81 / 2) + load_transfer

        front_tire_weight = front_tires_weight / 2
        rear_tire_weight = rear_tires_weight / 2

        for tire in self.front_tires:
            tire.update_load(front_tire_weight)
            
        for tire in self.rear_tires:
            tire.update_load(rear_tire_weight) 
   
            

    
    
        