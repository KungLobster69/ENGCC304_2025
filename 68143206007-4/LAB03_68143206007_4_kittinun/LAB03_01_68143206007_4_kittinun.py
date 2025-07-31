# รับค่าข้อมูล ที่เป็น str และแปลง เป็น float เพื่อหา ค่าของน้ำหนัก  และ ส่วนสูง
weight_kg=float(input("การคำนวนน้ำหนัก(kg):"))
height_cm=float(input("การคำนวนส่วนสูง(cm):"))

# น้ำค่าของ ส่วนสูง มา หาร 100 แลพจะได้ ค่าของ height_m
height_m=height_cm/100

# นำค่า height_m มา
bmi=weight_kg/(height_m **2)

print("ค่าดัชนีมวนกาย (BMI) ของคุณคือ:", bmi)