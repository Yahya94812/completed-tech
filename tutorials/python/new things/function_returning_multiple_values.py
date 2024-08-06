# Define a function that returns two values
def get_coordinates():
    x = 10
    y = 20
    return x, y

# Call the function and receive the two values
coordinates = get_coordinates()
print("Coordinates as tuple:", coordinates)

# You can also unpack the values directly into two variables
x, y = get_coordinates()
print("x:", x)
print("y:", y)
