#โปรแกรมทักทายและคํานวณอายุ
nick_name = input('ชื่อเล่น: ')

birth_year_str = input('ปีเกิด(พ.ศ.): ') #input รับปีเกิดผู้ใช้
birth_year = int(birth_year_str) #แปลงปีเกิดที่รับมาเป็น int

current_year = int(input('ปีปัจจุบัน(พ.ศ.): ')) #รับปีปัจจุบันพร้อมแปลง str เป็น int

age = current_year-birth_year #คำนวณอายุ (ปีปัจจุบัน ลบ ปีเกิด)

print(f'สวัสดีครับผมชื่อ {nick_name} อายุ {age} ครับ')

