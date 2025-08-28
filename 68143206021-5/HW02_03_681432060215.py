#โปรแกรมสร้างชื่อเล่นเท่ๆ
first_name = input('ป้อนชื่อจริง:')
birth_month = input('ป้อนเดือนเกิด(เช่น มกราคม):')

name_part = first_name[0:3].upper()
month_part = str(len(birth_month))


cool_nickname = name_part +" "+ month_part
print(cool_nickname)