#โปรแกรมแปลงวินาทีเป็น ชั่วโมง:นาที:วินาที
seconds = int(input("วินาที: "))
minutes = seconds // 60
remain_seconds = seconds % 60
hours = minutes // 60
remain_minutes = minutes % 60
print(f"{seconds} วินาที เท่ากับ {hours} ชั่วโมง {remain_minutes} นาที {remain_seconds} วินาที")