age=int(input("กรุณาป้อนอายุของคุณ: "))
is_child = age <= 12
#boolean Ture = 1 // False = 0 เมื่อคำนวน
price = (not is_child)*100 + is_child * 50
print("ราคาตั๋วของคุณคือ", int(price), "บาท")