#โปรแกรมสลับชื่อ-นามสกุล
full_name = input("ป้อนชื่อ-สกุล: ")
name_part = full_name.split()
first_name = name_part[0]
last_name = name_part[1]
formatted_name = last_name + " " +first_name
print(f"ชื่อในรูปแบบ 'นามสกุล ชื่อ' คือ: {formatted_name}")