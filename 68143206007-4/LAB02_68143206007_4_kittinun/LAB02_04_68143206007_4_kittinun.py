second = input("วินาที    ")
second= int(second)
minute = second // 60
total_time = second % 60
hours = minute // 60
total_time_hours = minute % 60
print(f"{second} วินาที เท่ากับ {hours} ชั่วโมง {total_time_hours} นาที และ {total_time} วินาที")
