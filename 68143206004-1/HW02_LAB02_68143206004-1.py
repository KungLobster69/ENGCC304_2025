print("โปรแกรมคำนวณค่าอาหาร")
total_cost_str = input("ราคารวมของอาหาร : ")
tip_pct_str = input("เปอร์เซ็นต์ทิป ที่ต้องการให้ : ")
num_people_str = input("จำนวนคนที่จะหาร : ")

tip_pct = int(tip_pct_str)
total_cost = int(total_cost_str)
num_people = int(num_people_str)

tip_amount = total_cost * (tip_pct / 100)
print(f"ทิป {tip_pct}%: {tip_amount} บาท")

final_bill = total_cost+tip_amount
print(f"ยอดรวมสุทธิ: {final_bill:.2f} บาท")

cost_per_person = final_bill/num_people
print(f"จ่ายคนละ: {cost_per_person:.2f} บาท")
