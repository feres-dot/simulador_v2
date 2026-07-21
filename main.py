from car import Car

def main():

    my_car = Car(1450) #Mass (kg)

    dt = 0.1 #Time step

    simulated_time = 0 

    force = 5000 #Constant Force (N)

    print ("Starting simulation")
    print("-" * 60)

    while simulated_time < 3:
        my_car.update_physics(force, dt)
        simulated_time += dt

        print(f"Time: {simulated_time:.1f}s | Position: {my_car.x:.2f} meters | Velocity: {my_car.v * 3.6:.2f} km/h | Aceleration: {my_car.a:.2f} m/s²")        # Velocity multiplied with 3.6 to convert from m/s to km/h

if __name__ == "__main__":
    main()