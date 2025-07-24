weight_kg = float(input("กรุณาป้อนน้ำหนัก (kg): "))
height_cm = float(input("กรุณาป้อนส่วนสูง (cm): "))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
print("ค่าดัชนีมวลกาย (BMI) ของคุณคือ:", bmi)