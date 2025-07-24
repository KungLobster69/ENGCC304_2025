#โปรแกรมสร้างชื่อเล่นเท่ๆ
first_name=input("ชื่อจริง: ")
birth_month=input("เดือนเกิด: ")

name_part = first_name[0:3].upper()
month_part = str(len(birth_month))
cool_nickname = name_part + month_part

print("ชื่อเล่นสุดเท่ของคุณคือ: ", cool_nickname)