"""---โปรแกรมคำนวณ BMI---
START
  GET weight(kg)
  GET height(cm)
  
  CALCULATE BMI = weight/(height*height)
  PRINT "BMI"

  IF BMI < 18.5 THEN
    PRINT "น้ำหนักน้อยกว่าเกณฑ์"
  ELIF BMI < 23 THEN
    PRINT "น้ำหนักปกติ"
  ELSE BMI < 25 THEN
    PRINT "น้ำหนักเกิน"
  ENDIF
END """

try:
  weight = float(input('Enter your weight(kg): '))
  height_cm = float(input('Enter your height(cm): '))
  
  height_m = height_cm/100
  BMI = weight/(height_m**2)
  print(f'Your bmi is: {BMI}')
  
  if BMI < 18.5:
    print('น้ำหนักน้อยกว่าเกณฑ์')
  elif BMI < 23:
    print('น้ำหนักปกติ')
  else:
    print('น้ำหนักเกิน')
except ValueError:
    print(f'Error!! ป้อนตัวเท่านั้น')