weight = float(print("Enter weight (kg): "))
height = float(print("Enter weight (m): "))
bmi = weight / (height ** 2)
print("Your BMI is:" , bmi)
if bmi < 18.5:
    print("Result: Underweight")
elif bmi < 23:
    print("Result: Normal weight")
elif bmi < 25:
    print("Result: Overweight")
else:
    print("Result: Obesity")