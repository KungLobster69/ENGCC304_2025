User_input = (" Flim_dOg")
text = User_input.strip().lower().replace(' ','_')

print(f"ข้อความที่ปรับปรุงแล้ว {text}")

user_name = len(text)

if 5 <= user_name <= 20:
    print("สถานะ User นี้ใช้ไม่ได้")
else:
    print(f"สถานะ user  {user_name}")
    print("-" * 40)
    input("กด enter เพื่อทำ workshop")