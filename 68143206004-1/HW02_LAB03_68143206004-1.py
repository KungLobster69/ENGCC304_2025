print("โปรแกรมสร้างชื่อเล่นเท่ๆ")
print("-" * 50)
first_name = input("ชื่อจริง :")
birth_month = input("เดือนเกิด (เช่น มกราคม) :")
name_part = first_name.upper().strip()[0:3]
month_part = len(birth_month)
cool_nickname = name_part + str(month_part)
print("" * 50)
print(f"ชื่อเล่นสุดเท่ของคุณคือ :{cool_nickname}")