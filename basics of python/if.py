__author__ = 'dev'


# name = input('please enter your name')
# age  = input('how old are you ? {0}'.format(name))
# print(age)
#
# if int(age) >= 18:
#     print('you are old enough to vote')
#     print('please put x in box')
# else:
#     print('Please come after {0} years'.format(18 - int(age)))

print('Please give a number between 1- 10')
guess = int(input())

if guess < 5:
    print('please guess higher')
    guess = int(input())
    if guess == 5:
        print('well done you guessed it')
    else:
        print('sorry you have not guessed correctly')
elif guess > 5:
    print('please guess lower')
    guess = int(input())
    if guess == 5:
        print('well done, you guessed it')

    else:
        print('sorry, you have not guessed it')
else:
    print('you get it first time')