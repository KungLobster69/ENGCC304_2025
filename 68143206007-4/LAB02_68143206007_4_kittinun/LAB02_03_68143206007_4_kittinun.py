5
try:
    number_f = input("ตัวเลขตัวที่1   ")
    number_t = input("ตัวเลขตัวที่2   ")
    a= int(number_f)
    b= int(number_t)
    number_e = a / b
except ValueError:
    print("ใส่ ตัวอักศร มาทำแปะอะไร")
except (ZeroDivisionError , TypeError) as e:
    print(f"ใส่ 0 มาทำแปะ อะไร: {e}")
else:
    print("ผลรับที่ได้")
    print(f"{number_e}")



