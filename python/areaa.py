shape = int(input("Enter the shape: 1 for Square, 2 for Rectangle and for Rhombus:"))
if shape == 1:
    side = int(input("Enter the side of square:"))
    area = side * side
    print(f"The area of square is: {area}")
elif shape == 2:
    length = int(input("Enter the length of rectangle:"))
    width = int(input("Enter the width of rectangle:"))
    area = length * width
    print(f"The area of rectangle is: {area}")
elif shape == 3:
    d1 = int(input("Enter the first diagonal of rhombus:"))
    d2 = int(input("Enter the second diagonal of rhombus:"))
    area = (d1 * d2) / 2
    print(f"The area of rhombus is: {area}")
else:
    print("Invalid input")