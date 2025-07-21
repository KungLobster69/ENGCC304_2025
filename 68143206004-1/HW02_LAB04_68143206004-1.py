print("โปรแกรมแปลงวินาทีเป็น H:M:S")
print("" * 30)
total_seconds_str = input("จำนวนวินาทีทั้งหมด(เป็นตัวเลข)")
total_seconds = int(total_seconds_str)
minutes = total_seconds // 60
seconds = total_seconds % 60
hours   = minutes // 60
remaining_seconds = minutes % 60
print("" * 30)
print(f"{hours}ชัวโมง {remaining_seconds}นาที {seconds}วินาที")