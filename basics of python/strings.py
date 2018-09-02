__author__ = "dev"
age = 24
print('my age is ' + str(age)) #changed number to string
print('my age is {0} age'.format(age) )
print('there are {0} days in {1}, {2}, {3}, {4}'.format(31, 'jan', 'march', 'may', 'july'))

# old format of doing with python 2
print('my age is %d' % age)
print('my age is %d %s, %d %s' % (age , 'years', 6, 'months'))

for i in range(1, 12):
    print('current number %d and multiply is %d' % (i , i * i))

print('Pi is appx is %12.50f' % (22/7))


# doing in python 3
for i in range(1, 12):
    print('current number {0:2} and multiply is {1}'.format(i , i * i)) # replacement:allowcastion

print('Pi is appx is {0}'.format(22/7))

