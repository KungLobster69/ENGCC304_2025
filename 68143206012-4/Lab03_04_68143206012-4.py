item_name = input("ชื่อสินค้า: ")
price = float(input("ราคาสินค้าต่อชิ้น: "))
quantity = int(input("จำนวน: "))

total = price*quantity

print(f"\n---ใบเสร็จอย่างย่อ---")
print(f"รายการ: {item_name} {quantity} ชิ้น")
print(f"ยอดรวมสุทธิ: {total:.2f} บาท")