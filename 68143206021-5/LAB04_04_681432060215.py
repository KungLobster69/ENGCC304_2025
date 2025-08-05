""" ---โปรแกรมหาผลรวม 1 ถึง N---
START
  INPUT N_value
  SET total = 0
  SET counter = 1
  FOR i FROM 1 + N_value + 1
    result total = total + i
  PRINT "Sum is:, toal"
  ENDFOR
END   """

try:
    N_value = int(input('Enter Number: '))
    total = 0
    counter = 1
    for i in range (1, N_value + 1):
        total = total + i
    print('Sum is:', total)
except ValueError:
    print(f'Error!! ป้อนตัวเท่านั้น')