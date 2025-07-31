Score_input = float(input("้กรอกคะแนนสอบที่ได้ : "))
if Score_input >= 0 and Score_input <=100:
    if Score_input >= 80:
        grade = "A"
    elif Score_input >= 70:
        grade = "B"
    elif Score_input >= 60:
        grade = "C"
    elif Score_input >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"คะแนน : {Score_input} , Grade : {grade}")
else:
    print(f"Error คะแนน '{Score_input}' กรุณากรอกคะแนนให้อยู่ในช่วง 0-100 ")

