empty_tuple = ()
inventory = [("P001", "Keyboard", 50)
             ,("P002", "Mouse", 75)
             ,("P003", "Monitor", 30)]

for i in inventory :
    (Product_id, Name, Stock) = i
    print(f"ID : {Product_id}"  ,  f"   Name : {Name}" , f"   In Stock : {Stock}")