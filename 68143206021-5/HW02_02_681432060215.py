#โปรแกรมคำนวณค่าอาหาร (หารเท่ากัน) 
total_cost = float(input('ราคารวมของอาหาร: '))
tip_pct = float(input('เปอร์เซ็นทิปที่ต้องให้: '))
num_people = int(input('จำนวนคนที่จะหาร: '))

tip_amount = tip_pct*total_cost/100 #เก็บจำนวนเงินทิป
final_bill = total_cost+tip_amount #ยอดรวมสุทธิ
cost_per_person = final_bill/num_people

print(f'ยอดที่แต่ละคนต้องจ่าย+ทิป: {cost_per_person} บาท')