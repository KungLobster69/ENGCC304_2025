score = int(input("กรุณาป้อนคะแนน: "))
homework_submitted = True
is_eligible = (score > 80) and (homework_submitted == True)
print("มีสิทธิ์ได้รับรางวัล:", is_eligible)