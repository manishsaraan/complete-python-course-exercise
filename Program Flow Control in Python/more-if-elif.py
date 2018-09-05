age = int(input('how old are you?'))
#
# # if (age >= 16) and (age <= 65):
# # if 16 <= age <=65:
# #     print('have a good day at work')
#
# if (age < 16) or (age > 65):
#     print('enjoy your free time')
# else :
#     print('have a good day at work')

print(not False)
print(not True)

if not(age < 18):
    print('please put vote in box')
else :
    print('please come after {0} years'.format(18 -age))