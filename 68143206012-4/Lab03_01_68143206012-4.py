weight_kg = float(input("กรุณรุาป้อนน้ำหนัก (kg): "))
height_cm = float(input("กรุณรุาป้อนส่วนสูง (cm): "))
height_m = height_cm / 100
bmi = weight_kg/(height_m**2)
print("ค่าดัชนีมวลกาย (BMI) ของคุณคือ:", bmi)