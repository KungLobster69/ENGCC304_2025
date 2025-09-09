def calculate_circle_area(radius):
    circle_area = 3.14159 * (radius**2)
    return float(circle_area)

def calculate_triangle_area(base,height):
    triangle_area = 0.5 * base * height
    return float(triangle_area)

R = float(input("กรุณากรอกค่ารัศมี: "))
print(calculate_circle_area(R))

B = float(input("กรุณากรอกความยาวฐาน: "))
H = float(input("กรุณากรอกความสูง: "))
print(calculate_triangle_area(B,H))