# Input length and breadth
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

# Calculate area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Compare area and perimeter
if area > perimeter:
    print("Area is greater than perimeter.")
else:
    print("Perimeter is greater than area.")
