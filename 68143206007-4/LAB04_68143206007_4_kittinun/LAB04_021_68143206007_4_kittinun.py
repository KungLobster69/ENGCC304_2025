# START
# PRINT "Please entet your age:"
# READ  age

# IF age >= 18 THEN
# PRINT "You are eligible to vote."
# ELSE
# years_left = 18 - age
# PRINT "You are not eligible to vote."
# PRINT "You are not eligible in" , years_left, "years."
# ENDIF
# END

# รับอายุจากผู้ใช้
age_str = input("Please enter your age: ")
age = int(age_str)
# ตรวจสอบเงื่อนไขตามที่กำหนด
if age >= 18:
    print("You are eligible to vote.")
else:
    years_left = 18 -age
    print("You are not eligible to vote.")
    print("You are not eligible to in.", years_left, "years.")
