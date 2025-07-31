import random 
answer = random.randint(1, 100)
while True: 
    guess = int(input("ใส่ตัวเลข"))
    if guess == answer:
        print("ยินดีด้วยคุณเดาถูก") 
        break
    elif guess < answer:
        print("เดาเลขตำไป")
    else :
        print("เดาเลขสูงไป")
