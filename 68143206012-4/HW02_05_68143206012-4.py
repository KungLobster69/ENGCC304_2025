#โปรแกรมตรวจสอบคะแนนสอบ
score_input = input("ป้อนคะแนนสอบ: ")
try:
    score = float(score_input)
    is_passed = score >= 50
    print("คะแนนของคุณคือ: ", score)
    print("ผลการสอบ (ผ่าน/ไม่ผ่าน): ", is_passed)
except ValueError:
    print("กรุณาใส่ตัวเลขเท่านั้น")