try:
 sec_str = input("กรุณากรอกวินาที: ")

 sec = int(sec_str)

 min =  sec // 60
 sec_ = sec % 60
 hour = min // 60
 min_ = min % 60

 print(f" วินาที {sec} เท่ากับ {hour} ชั่วโมง {min_} นาที {sec_} วินาที")

except ValueError:
 print("กรุณากรอกตัวเลขเท่านั้น")