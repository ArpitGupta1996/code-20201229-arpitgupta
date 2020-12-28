def BMI(height,weight):
    bmi=weight/(height**2)
    return bmi
height=float(int(input(“Enter the height: “))
weight= float(int(input(“Enter the height: “))
bmi=BMI(height, weight)
print(“The BMI is”, format(bmi), “so”, end=’’)
if(bmi < 18.5):
              print(“underweight”)
elif(bmi>=18.5 and bmi<24.9):
              print(“Normal Weight”)
elif(bmi>=25 and bmi < 29.9):
              print(“overweight”)
elif(bmi>=30 and bmi<=34.9):
              print(“Moderately obese”)
elif(bmi>=35 and bmi<=39.9):
              print(“High Risk”)
else:
              print(“Very severely obese”)
