#โปรแกรมคำนวณส่วนลด
price = float(input("ป้อนราคารวมของสินค้า: "))
if price >= 500:
    final_price = price-(price*0.1)
    print(f"คุณได้รับส่วนลด 10% เป็นเงิน {price*0.1} บาท")
else:
    final_price = price
    print("คุณไม่ได้รับส่วนลด")
print(f"ราคาสุทธิที่ต้องชำระคือ: {final_price} บาท")