# for i in range(1, 10):
#     print('current i is {0}'.format(i))
#
# number = "9,55,5558,52,55"
# cleanNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanNumber = cleanNumber + number[i]
#
# newNumber = int(cleanNumber)
# print('number is {0}'.format(newNumber))

number  = "9,55,5558,52,55"
cleanNumber = ''

for char in number:
    if char in '0123456789':
        cleanNumber = cleanNumber + char

newNumber = int(cleanNumber)
print(newNumber)

# adding steps in for loop
for i in range(0, 100, 5): # add 5 steps
    print('i is {0}'.format(i))

for i in range(1, 11):
    for j in range(1, 11):
        print('{0} multiply by {1} is {2}'.format(i,j, i*j))
    print('========')