item_ = input("ป้อนชื่อสินค้า: ")
price_ = float(input("ป้อนราคาสินค้าต่อชิ้น: "))
quantity = int(input("ป้อนจํานวนสินค้าที่ต้องซื้อ: "))
total = price_ *quantity
print(f"แสดงชื่อสินค้า: {item_}")
print(f"ราคารวมทั้งหมด : {total:.2f} บาท")
