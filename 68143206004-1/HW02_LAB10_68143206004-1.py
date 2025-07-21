print("โปรแกรมสลับชื่อ - นามสกุล")
print("" * 50 )
full_name = input("ชื่อ-นามสกุล(คั่นด้วยเว้นวรรค) :")
name_parts = full_name.split()
first_name = name_parts[0]
last_name = name_parts[1]
formatted_name = f"{last_name} {first_name}"
print(f"ชื่อในรูปแบบ นามสกุล - ชื่อ คือ:{formatted_name}")