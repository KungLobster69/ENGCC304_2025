try:
    Product_price = input("ราคาสินค้า")
    Number_of_products = input ("จำนวนสินค้าที่ต้องการซื่อ")


    Product_price_float= float(Product_price)
    Number_of_products_float= float(Number_of_products)

    Product_price_in= int(Product_price)
    Number_of_products_in= int(Number_of_products)

    print("แสดง int")
    print(Product_price_in,int(Product_price))
    print(Number_of_products_in,int(Number_of_products))

    print("แสดง float")
    print(Product_price_float,float(Product_price))
    print(Number_of_products_float,float(Number_of_products))

    print("แสดง type")
    print(Product_price,type(Product_price_in))
    print(Number_of_products,type(Number_of_products_in))


    together = Product_price_in * Number_of_products_in
    print(f"จะได้ราคา {together} บาท")
except ValueError:
    print("ใส่อะไรมา โปรดใส่เป็นตัวเลขด้วยครับ")
else:
    print("ผลรับที่ได้")
    print(f"{together}")




