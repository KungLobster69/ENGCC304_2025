score = float(input("Enter Score:"))
if score >= 0 and score <= 100:
    grade = ""
    if score >= 80:
      grade = "A"
    elif score >= 70:
      grade = "B"
    elif score >= 60:
      grade = "C"
    elif score >= 50:
      grade = "D"
    else:
      grade = "F"
      print(f"Score:", score, "grade:", grade)     

else:
  print(f"Error คะแนน {score} ไม่ถูกต้อง")