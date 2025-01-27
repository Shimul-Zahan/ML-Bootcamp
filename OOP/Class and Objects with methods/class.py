# Class for Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        """Check if the point falls inside the given rectangle."""
        if rectangle.lower_left.x < self.x < rectangle.upper_right.x \
                and rectangle.lower_left.y < self.y < rectangle.upper_right.y:
            return True
        else:
            return False


# Class for Rectangle
class Rectangle:
    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def area(self):
        """Calculate the area of the rectangle."""
        width = self.upper_right.x - self.lower_left.x
        height = self.upper_right.y - self.lower_left.y
        return width * height


# Taking input for lower-left coordinate
x, y = map(int, input("Give values for x and y coordinate for lower-left point (space-separated): ").split())
lower_left = Point(x, y)

# Taking input for upper-right coordinate
a, b = map(int, input("Give values for x and y coordinate for upper-right point (space-separated): ").split())
upper_right = Point(a, b)

# Creating a rectangle
rectangle = Rectangle(lower_left, upper_right)

# Taking input for a point to check if it falls inside the rectangle
px, py = map(int, input("Enter x and y coordinates of the point to check (space-separated): ").split())
point = Point(px, py)

# Output the details
print(f"Lower-left point: ({lower_left.x}, {lower_left.y})")
print(f"Upper-right point: ({upper_right.x}, {upper_right.y})")
print(f"Point to check: ({point.x}, {point.y})")

# Check if point falls inside rectangle
if point.falls_in_rectangle(rectangle):
    print("The point falls inside the rectangle.")
else:
    print("The point does not fall inside the rectangle.")

# Print area of the rectangle
print(f"The area of the rectangle is: {rectangle.area()}")
