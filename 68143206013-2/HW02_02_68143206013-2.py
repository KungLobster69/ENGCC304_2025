try:
 product_str = input("ราคาสินค้าต่อชิ้น :")
 productnumber_str = input("จำนวนสิ้นค้าที่ต้องซื้อ :")
 product_float = float(product_str)
 productnumber_int = int(productnumber_str)
 print(product_float,type(product_float))
 print(productnumber_int,type(productnumber_int))
 totalproduct = product_float * productnumber_int
 print(f"ราคารวมทั้งหมด : {totalproduct:.2f} บาท")
except ValueError:
 print("Error")