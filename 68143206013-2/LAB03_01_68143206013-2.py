weight_kg = float(input("ป้อนน้ําหนักของคุณ (kg): "))
height_m = float(input("ป้อนส่วนสูงของคุณ (cm): "))
h_m = height_m / 100
bmi = (weight_kg / (h_m **2))

print(f"ค่า BMI ของคุณคือ {bmi:.2f}")