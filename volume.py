import math

def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_volume(radius):
    return (4/3) * math.pi * (radius**3)

def main():
    radius = get_input("Enter radius of sphere: ")
    volume = calculate_volume(radius)
    print(f"Volume of sphere: {volume:.2f}")

if __name__ == "__main__":
    main()