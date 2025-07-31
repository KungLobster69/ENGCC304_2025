# ใส่ข้อมูล และแปลงเป็น ตัวเลข
age=int(input("กรอกอายุ"))
# กำหนดค่าให้ อายุ น้อยดว่า 12
is_child = age <= 12
price=(not is_child)*25000 + is_child *10000
print("ราคาตั๋วของคุณคือ:", int(price),"บาท")