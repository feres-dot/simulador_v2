from car import Car

def main():

    my_car = Car(1450,400,0.4,3.4,4.1,0.39, 2.0, 1.225) #Mass (kg)

    dt = 0.1 #Time step

    simulated_time = 0 

    print ("Starting simulation")
    print("-" * 60)

    while simulated_time < 40:
        my_car.update_physics(dt)
        simulated_time += dt

        # Velocity multiplied with 3.6 to convert from m/s to km/h
        print(f"Time: {simulated_time:.1f}s | Position: {my_car.x:.2f} meters | Velocity: {my_car.v * 3.6:.2f} km/h | Aceleration: {my_car.a:.2f} m/s²")     

if __name__ == "__main__":
    main()