# START
# PRINT "Please entet your age:"
# READ  age

# IF age >= 18 THEN
# PRINT "You are eligible to vote."
# ELSE
# PRINT "You are not eligible to vote."
# ENDIF
# END

# รับอายุจากผู้ใช้
age_str = input("Please enter your age: ")
age = int(age_str)
# ตรวจสอบเงื่อนไขตามที่กำหนด
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
