import random
answer = random.randint(1,100)
attemps = 0
while True:
   player = int(input("Enter number:"))
   attemps += 1
   if answer < player:
      print("มากไป")
   elif answer > player:   
      print("น้อยไป")
   else:
      print(f"ถูกต้องละค้าบบบบ! คุณทายไปทั้งหมด {attemps} ครั้ง")
      break
