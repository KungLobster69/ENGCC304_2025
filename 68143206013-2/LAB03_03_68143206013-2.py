age = int(input("ป้อนอายุของคุณ: "))
number_ = int(input("ป้อนจํานวนคน: "))
if age <= 12:
    print("ราคาบัตร50บาท")
    x = 50 * number_
    print("ราคารวมทั้งหมด:",x,"บาท") 
else:
    print("ราคาบัตร100บาท")
    y = 100 * number_
    print("ราคารวมทั้งหมด:",y,"บาท")

