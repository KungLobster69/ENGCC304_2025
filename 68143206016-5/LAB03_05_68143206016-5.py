first_name = input("ป้อนชื่อจริง (ภาษาอังกฤษ): ")
birth_year = input("ป้อนปีเกิด (ค.ศ.): ")

name_part = first_name[0:3].lower()
year_part = birth_year[2:4]
username = name_part + year_part
print(f"ชื่อผู้ใช้ที่แนะนำสำหรับคุณคือ: {username}")