try:
 x_str = input("กรอกตัวเลขที่ 1: ")
 y_str = input("กรอกตัวเลขที่ 2: ")
 x = float(x_str)
 y = int(y_str)
 sum_ = x/y
 print(f"ผลรวม = {sum_:.2f}")
except ValueError:
 print("กรุณากรอกตัวเลขเท่านั้น")
except ZeroDivisionError:
 print("ไม่สามารถหารด้วย 0 ได้")