import math

# Function to calculate the area of a circle
def circle_area(radius):
    # Calculate the area
    area = math.pi * radius**2
    # Return the area
    return area

# Example usage
radius = float(input('Please Enter the Radius of a Circle: '))

# Calculate the area of a Circle
area = circle_area(radius)

print("The Area of a Circle using", radius, " = ", area)