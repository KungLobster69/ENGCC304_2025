#START
#PRINT "Enter score for Math:"
#READ math_ score
#PRINT "Enter score for Science:"
#READ science_score
#PRINT "Enter score for English:"
#READ english_score
#sum score = math_score + science_score + english_score
#average_score = sum_score / 3
#PRINT "The average score is:", average_score
#END

Math_score = float(input ("ป้อนคะแนนสอบ Math : "))
Sci_score = float(input ("ป้อนคะแนนสอบ Sci : "))
English_score = float(input ("ป้อนคะแนนสอบ Eng : "))

Average = Math_score + Sci_score + English_score
Average_Score = Average / 3
print(f"คะแนนเฉลี่ย คือ: {Average_Score}")