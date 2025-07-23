UserName = input("กรอกชื่อ :")
FixUser = UserName.strip().lower().replace('_','')
dflen = len(FixUser)

if   5 <= dflen <= 20:
    print(f"ใช้ได้ {FixUser}")
else:
    print("ชื่อต้องมีความยาวระหว่าง 5-20 ตัวอักษร")
    input("กด enter เพื่อปิดโปรแกรม :")