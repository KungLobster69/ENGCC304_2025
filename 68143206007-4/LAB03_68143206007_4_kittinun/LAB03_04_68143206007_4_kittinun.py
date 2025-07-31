item_name = input("ชื่อสินค่า:")
price = float(input("ราคาสินค่า:"))
quantity = int(input("จำนวนสินค่า:"))
total = price * quantity
print(f"\n ------ใบเสร็จ------")
print(f"รายการสินค่า:{item_name}")
print(f"ยอดรวมสิทธ์:{total:.2f}บาท")