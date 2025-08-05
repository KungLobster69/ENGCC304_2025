"""โปรแกรมตรวจสอบสิทธิ์เลือกตั้งสําหรับหน่วยเลือกตั้ง---
START
  INPUT age
  IF age >= 18 THEN
    PRINT "ท่านมีสิทธิ์เลือกตั้ง"
  ELSE
    PRINT "ท่านไม่มีสิทธิ์เลือกตั้ง"
  ENDIF  
END """

try:
    age = int(input('Enter your age: '))
    if age >= 18:
        print('ท่านมีสิทธิ์เลือกตั้ง')
    else:
        print('ท่านไม่มีสิทธิ์เลือกตั้ง')
except ValueError:
    print(f'กรุณาป้อนตัวเลขเท่านั้น!!')            