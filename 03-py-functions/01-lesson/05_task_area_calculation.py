def calculate_area(width, height):
    area = width * height
    return area


tot_area = calculate_area(12, 33)
tot_area += calculate_area(28, 14)
tot_area += calculate_area(55, 72)

print(f"Total area: {tot_area}")


total_area = 0

for width in range(2, 5):
    for height in range(2, 5):
        area = calculate_area(width, height)
        print(f"Area is {area}")
        total_area += area

print(f"Total area: {total_area}")
