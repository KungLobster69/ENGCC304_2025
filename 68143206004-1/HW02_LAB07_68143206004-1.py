print("โปรแกรมสร้างรหัสผ่านแนะนำ")
print("" * 50 )
pet_name = input("ชื่อสัตว์เลี้ยง :")
phone_digits = input("เลข 2 ตัวท้ายของเบอร์โทรศัพท์ :")
pet_name_str = str(pet_name)[:4]
phone_digits_str = str(phone_digits)
password = pet_name_str + phone_digits_str + "_x"
print(f"รหัสผ่านที่แนะนำสำหรับคุณคือ:{password}")