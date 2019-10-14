number_of_prints_str = input("How many numbers of fibonacci sequence you want? ")
number_of_prints = int(number_of_prints_str)

k = 0
j = 1
fib = 0
i = 1
list_of_prints = [0]


if number_of_prints <= 0:
    print('Enter positive int')
elif number_of_prints == 1:
    print('Fibonacci sequence upto: ', number_of_prints, ':')
    print(k)
else:
    while i < number_of_prints: 
        # print(k)  # print(k, end='\n') ---> to get specific ending
        fib = k + j
        k = j
        j = fib
        list_of_prints.append(k)
        i += 1


# this works: (just prints list)
# for x in list_of_prints:
#     print(x)

# TODO: add function for below loop

for x, value in enumerate(list_of_prints):
    if (x + 1) < 10:
        print(str(x + 1) + ':', '{:>40}'.format(value))
    elif int(x + 1) == 10:
        print(str(x + 1) + ':', '{:>39}'.format(value))
    elif int(x + 1) > 10 and int(x + 1) < 100:
        print(str(x + 1) + ':', '{:>39}'.format(value))
    elif int(x + 1) == 100:
        print(str(x + 1) + ':', '{:>38}'.format(value))
    elif int(x + 1) > 100:
        print(str(x + 1) + ':', '{:>38}'.format(value))
    # else:
    #     print('too much')
    
    # for line in list_of_prints:
    #     print('{:>8}'.format(line))
    # print(end=':')
    # print(f'{x+1} {value}')  # end=':')
    # print('{}{}'.format)
