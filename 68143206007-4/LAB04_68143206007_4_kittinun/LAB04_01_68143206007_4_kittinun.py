# START
# PRINT "Enter score for Math:"
# READ  math_score

# PRINT "Enter score for Science:"
# READ  science_score

# PRINT "Enter score for English:"
# READ  english_score

# scm_score = math_score + science_score + english_score
# average_score = scm_score / 3

# PRINT "The average score is: , average_score"
# END

# รับคะแนนท้ั้ง 3 วิชา
math_score = float(input("Enter score for Math"))
science_score = float(input("Enter score for Science"))
english_score = float(input("Enter score for English"))

#คำนวนผลรวมและค่าเฉลี่ย
sum_score = math_score + science_score + english_score
average_score = sum_score / 3

#แสดงผลลัพธ์
print("The average is:" , average_score)