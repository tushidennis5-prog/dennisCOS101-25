def show_menu():
    """Displays the menu of physics formularas."""
    print("\nWelcome to the Physics Calculator")
    print("\nSelect a Physics Formualar:")
    print("1. Speed = Distance/time")
    print("2. Force = Mass * Accelaration")
    print("3. Work done = Force * Acceleration")
    print("4. Pressure = Force/Area")
    print("5. Density = Mass/Volume")

def calculate(choice): 
    """Performs the calculation based on the user's choice."""
    if choice == "1":
        # Speed = Distance / Time
        d = float(input("Enter Distance (m): "))
        t = float(input("Enter Time (s): "))
        print(f"speed = {d / t} m/s")
    
    elif choice == "2":
        #Force = Mass * Acceleration
        f = float(input("Enter Force (N):"))
        a = float(input("Enter Acceleration (m/s^2):"))
        print(f"Force = {f * a} Nms^2")

    elif choice == "3":
        #Work_done = Force *  Distance
        f = float(input("Enter Force (N):"))
        d = float(input("Enter Distance (m):"))
        print(f"Work done = {f * d} J")

    elif choice == "4":
        #Pressure = Force / Area
        f = float(input("Enter Force (N):"))
        a = float(input("Enter Area (m^2):"))
        print(f"Pressure = {f / a} Pa")
        
    elif choice == "5":
        #Density = Mass / Volume
        m = float(input("Enter Mass (kg):"))
        v = float(input("Enter Volume (m^3):"))
        print(f"Density = {m / v} kg/m^3")

    else:
        print("Invalid choice. Please select a valid option.")

def main():
    """Main function to run the physics calculator."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-5) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting the Physics Calculator. Goodbye!")
            break

        calculate(choice)

if __name__ == "__main__":
    main()


