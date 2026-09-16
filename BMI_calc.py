print('''
Enter params in format: height(in metres) weight
''')

height = float(input('Height: '))
weight = float(input('Weight: '))

if height == 0.0:
    raise ValueError('Your params cant be zero')

bmi = weight/(height**2)

if bmi < 18.5:
    print(f'Underweight, your BMI: {bmi}')
elif bmi >= 18.5 and bmi <= 24.9:
    print(f'Normal/Healthy weight, your BMI: {bmi}')
elif bmi >= 25 and bmi <=29.9:
    print(f'Overweight, your BMI: {bmi}')
elif bmi > 30.0:
    print(f'Obesity, your BMI: {bmi}')
else:
    print('Something went wrong')