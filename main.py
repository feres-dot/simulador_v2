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
        if simulated_time > 60:
            my_car.is_braking = True
            
        physics_steps = 100
        micro_dt = dt / physics_steps
        
        for _ in range(physics_steps):
            my_car.update_physics(micro_dt)
            
        simulated_time += dt

        tire_speed_kmh = my_car.rear_tires[0].angular_velocity * my_car.wheel_radius * 3.6

        print(f"Time: {simulated_time:.1f}s | "
              f"Car Vel: {my_car.v * 3.6:.1f} km/h | "
              f"Tire Vel: {tire_speed_kmh:.1f} km/h | "
              f"Accel: {my_car.a:.2f} m/s² | "
              f"Gear: {my_car.current_gear_index + 1} | "
              f"Tire Force: {my_car.rear_tires[0].get_pacejka_force(my_car.v):.0f} N")     

if __name__ == "__main__":
    main()