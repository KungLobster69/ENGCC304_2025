""" โปรแกรมหาค่าเฉลี่ย
START
   READ math_score
   READ scince_score
   READ english_score
   CALCULATE sum = math_score + scince_score + english_score/3
   PRINT "คะแนนเฉลี่ย"
END """

try:
  math = float(input('Enter MathScore: '))
  scince = float(input('Enter ScinceScore: '))
  english = float(input('Enter EnglishScore: '))

  means_score = (math + scince + english)/3

  print(f'คะแนนเฉลี่ย: {means_score:2f} คะแนน')
except ValueError:
    print('กรุณาป้อนตัวเลขเท่านั้น!!')  