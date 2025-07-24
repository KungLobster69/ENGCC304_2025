#โปรแกรมคํานวณค่าอาหาร
total_cost = float(input("ราคาอาหารรวม: "))
tip_pct = int(input("เปอร์เซ็นต์ทิปที่ให้: "))
num_people = int(input("จํานวนคน: "))
tip_amount = total_cost*tip_pct/100
final_bill = total_cost+tip_amount
cost_per_person = final_bill / num_people
print(f"ราคารวม: {total_cost} บาท\n\
ทิป {tip_pct}%: {tip_amount} บาท\n\
ยอดรวมสุทธิ: {final_bill} บาท\n\
จ่ายคนละ: {cost_per_person} บาท")