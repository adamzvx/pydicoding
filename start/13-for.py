for letter in 'Python':  # First Example
    print('Current Letter: {}'.format(letter))
fruits = ['banana', 'apple', 'mango']

for fruit in fruits:  # Second Example
    print('Current fruit: {}'.format(fruit))

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('Current fruit: {}'.format(fruits[index]))

count = 0
while (count < 5):
    print('The count is: {}'.format(count))
    count = count + 1

#triangle....
for i in range(0, 5):
    for j in range(0, 5 - i):
        print('*', end='')
    print('->')