number_of_prints_str = input("How many numbers of fibonacci sequence jou want? ")
number_of_prints = int(number_of_prints_str)

k = 0
j = 1
fib = 0
i = 1
list_of_prints = [0]
list_of_ids = [1]

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


# this works:
# for x in list_of_prints:
#     print(x)

# print(list_of_ids)

# for id in range(30):
#     id += 1
#     fibo_number = list_of_prints[0]
#     print(format(id, '4d'), end='')
#     for x in list_of_prints:
#         print(x)

for x, line in enumerate(list_of_prints):
    print(f'{format(x+1)} {line}')
