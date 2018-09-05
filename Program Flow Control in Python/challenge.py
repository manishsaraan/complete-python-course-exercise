# write a program which ask for person age and name
# when both value entered the check if person can go for 18-30 holiday
# if yes then print enjoy your holiday
# otherwise print a polite message

name = input('please enter your name ')
age = int(input('please enter your age'))

if not(name) and not(age):
    print('please enter your name and age')
else:
    if(age >= 18) and (age <= 30):
        print('enjoy your holiday')
    else:
        print('you are not old enough')
