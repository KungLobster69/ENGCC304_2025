#โปรแกรมสร้างรหัสผ่านแนะนํา
pet_name = input("ป้อนชื่อสัตว์แลี้ยง: ")
phone_digit = input("ป้อนเบอร์โทรศัพท์: ")
password = pet_name[0:4] + phone_digit[8:10] + "X@!"
print("รหัสผ่านที่แนะนำสำหรับคุณคือ: ", password)