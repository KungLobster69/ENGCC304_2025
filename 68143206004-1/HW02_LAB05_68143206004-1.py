print("โปรแกรมตรวจสอบคะแนนสอบ")
print("" * 50 )
score_input = input("คะแนนสอบ :")

try  :
    score = float(score_input)
    is_passed = score >= 50
    print("ผลการสอบ (ผ่าน/ไม่ผ่าน) :", is_passed)
except ValueError:
    print("กรุณากรอกตัวเลขเท่านั้น")