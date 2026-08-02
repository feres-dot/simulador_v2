import math 
from car import Car

def main():
    gears = [3.4, 2.1, 1.4, 1.0, 0.8, 0.6]
    my_car = Car(1450, 400, 0.4, gears, 4.1, 0.39, 2.0, 1.225, 7000, 0.45, 2.50) #Mass (kg)
    
    # Version 9.0: Tiempo visual
    dt = 0.1
    simulated_time = 0.0 

    print ("Starting simulation")
    print("-" * 80)
    
    while simulated_time < 70:
        if simulated_time > 10 and simulated_time < 20:
            my_car.steering_angle = 0.1
        else:
            my_car.steering_angle = 0.0

        if simulated_time > 60:
            my_car.is_braking = True
            
        physics_steps = 100
        micro_dt = dt / physics_steps
        
        for _ in range(physics_steps):
            my_car.update_physics(micro_dt)

        true_speed_kmh = math.sqrt(my_car.vx**2 + my_car.vy**2) * 3.6
           
        simulated_time += dt

        true_accel = math.sqrt(my_car.ax**2 + my_car.ay**2)

        tire_speed_kmh = my_car.rear_tires[0].angular_velocity * my_car.wheel_radius * 3.6

        print(f"Time: {simulated_time:.1f}s | "
              f"Car Vel: {true_speed_kmh:.1f} km/h | "  # <-- Usamos la Velocidad Real
              f"Tire Vel: {tire_speed_kmh:.1f} km/h | "
              f"Accel: {true_accel:.2f} m/s² | "        # <-- Usamos la Aceleración Real
              f"Gear: {my_car.current_gear_index + 1} | "
              f"Yaw Rate: {my_car.yaw_rate:.3f} rad/s | "
              f"Slip Front: {my_car.telemetry_slip_front:.3f} rad | "
              f"Lat Force F: {my_car.telemetry_lat_force:.0f} N")
        
if __name__ == "__main__":
    main()