import math

# Prompt the user to input the radius and convert it to a floating-point number
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume using the mathematical formula: (4/3) * pi * r^3
# The exponential operator (**) is used to compute r cubed as required
volume = (4/3) * math.pi * (radius ** 3)

# Display the calculated volume rounded to two decimal places
print(f"The volume of the sphere is: {volume:.2f}")
