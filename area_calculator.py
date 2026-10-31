def calculate_room_area(length, width):
    area_sqft = length * width
    area_sqm = area_sqft * 0.092903
    perimeter = 2 * (length + width)

    return area_sqft, area_sqm, perimeter


print("================================")
print(" SRH ARCHITECTURAL AREA CALCULATOR")
print("================================")

length = float(input("Enter room length (feet): "))
width = float(input("Enter room width (feet): "))

area_sqft, area_sqm, perimeter = calculate_room_area(
    length, width
)

print("\n--- CALCULATION RESULTS ---")
print(f"Room Length: {length} ft")
print(f"Room Width: {width} ft")
print(f"Total Area: {area_sqft:.2f} sq.ft")
print(f"Total Area: {area_sqm:.2f} sq.m")
print(f"Room Perimeter: {perimeter:.2f} ft")

print("\nDeveloped by SRH Architects & Designs")
