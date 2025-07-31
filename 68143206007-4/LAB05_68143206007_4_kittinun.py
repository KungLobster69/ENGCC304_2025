# ใส่คะแนน ของคุณที่ได้
score = input("ใส่คะแนนที่ได้: ")

# แปลงค่าจ่างตัวหนังสือ เป็นตัวเลข
score_in = int(score)

# คำนวนคะแนนที่ได้ตามเกรด
# ถ้าคะแนนอยู่ที่ 0 หรือมากกว่า 100 ให้หาค่าไม่ได้
if score_in >= 0 and score_in <= 100 :
    grandn = " "


    if score_in > 80 :
         grand = "A"
    elif score_in > 70 :
        grand = "B"
    elif score_in > 60 :
        grand = "c"
    elif score_in > 50 :
        grand = "D"
    else:
        grand = "F"

# แสดงผลข้อมูล คะแนนที่ได้ และ ระบุ เกรดที่ได้
    print (f"ขอแสดงความยินดีด้วยคุณได้, {score_in} เกรด{grand}")

# แสดงผลการทำงานที่ตั้วไว้
else:
    print (f"ใส่อะไรมา")