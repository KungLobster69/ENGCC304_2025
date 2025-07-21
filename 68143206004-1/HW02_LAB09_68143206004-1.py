print("โปรแกรมคำนวณส่วนลด")
print("" * 50 )
price = input("ราคารวมสินค้า :")
price_int = int(price)
if price_int  >= 500:
    discount = price_int * ( 10 / 100)
    discount_int = int(discount) 
    print(f"คุณได้รับส่วนลด 10 % เป็นเงิน :{discount}")
    final_price = price_int - discount_int
    print(f"ราคาสุทธิที่ต้องชำระคือ :{final_price}")
else:
    print(f"ราคาสุทธิที่ต้องชำระคือ :{price_int}")