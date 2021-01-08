height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI_1 = float(weight / height ** 2)

BMI = (round(BMI_1, 2))

print(BMI)

if BMI <= 18.5:
    print(f'Your BMI is : {BMI}' + ',' + " You are underweight.")
elif BMI <= 25:
    print(f'Your BMI is : {BMI}' + ',' + " You have a normal weight.")
elif BMI <= 30:
    print(f'Your BMI is : {BMI}' + ',' + " You are slightly overweight.")
elif BMI <= 35:
    print(f'Your BMI is : {BMI}' + ',' + " You are obese.")
elif BMI > 35:
    print(f'Your BMI is : {BMI}' + ',' + " You are clinically obese.")
