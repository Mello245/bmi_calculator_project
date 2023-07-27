# Program to calculate Body Mass Index (BMI) for users. 

#Define the variables needed for the calculation 

weight = float(input('Please enter your weight in kilograms:'))
height = float(input('Please enter your height in meters:'))

#BMI = weight(kg)/(heightxheight)


#Print out users BMI 
BMI = (float(weight/(height*height)))
print('Your BMI is' + ' ' + (str(BMI)))


#Print out which "category" the user fall into on the BMI scale. 
if BMI >0:
    if BMI <16: 
        print('You are severley underweight')
    elif BMI <17:
        print('You are moderatley underweight')
    elif BMI <18.5:
        print('You are underweight')
    elif BMI<25:
        print('You are in the healthy weight range')
    elif BMI<30:
        print('You are overweight')
    elif BMI<35:
        print('You are moderatley obese')
    elif BMI<40:
        print('You are severly obese')
    elif BMI>40:
        print('You are morbidly obese')
else:
    print('The information you have put in is incorrect. ')