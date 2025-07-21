print("--โปรแกรมทักทายและคำนวณอายุ--")
nickname = input("ชื่อเล่น :")
birth_year_str = int(input("ปีเกิด(พ.ศ) :"))
current_year = 2567
brith_year = current_year - birth_year_str
print(f"สวัสดีครับคุณ {nickname} อายุของคุณตอนนี้ {brith_year}")
