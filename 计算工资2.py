while True:
    try:
        Hourlypay=input('Please enter your hourly salary:')
        type(float(Hourlypay)) is float
        break
    except ValueError:
        print('Error, please enter numeric input')

#--------
while True:
    try:
        Workinghours = input('Please enter your working hours:')
        type(float(Workinghours)) is float
        break
    except ValueError:
        print('Error, please enter numeric input')

#--------
a =  float(Workinghours)
b =  float(Hourlypay)
if a <= 40:
    Grosspay = b * a
    print('Your gross pay:',Grosspay)
if a > 40:
    Grosspay = (40 * b)+((a - 40)*(b * 1.5)) 
    print('Your gross pay:',Grosspay)