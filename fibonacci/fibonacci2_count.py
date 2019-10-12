number_of_prints_str = input("How many numbers of fibonacci sequence you want? ")
number_of_prints = int(number_of_prints_str)

x = 0
y = 1
# or:
# x, y = 0, 1

z = 0
count = 0

if number_of_prints <= 0:
    print('Enter positive int')
elif number_of_prints == 1:
    print('Fibonacci sequence upto: ', number_of_prints, ':')
    print(x)
else:
    while count < number_of_prints: 
        # if number_of_prints changed here to 30, it will show
        # first 30 fibonacci sequences
        print(x)  # print(x, end='\n') ---> to get specific ending
        z = x + y
        x = y
        y = z
        count += 1


