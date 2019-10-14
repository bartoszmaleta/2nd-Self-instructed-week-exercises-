# TODO appending to list!!!!
# output is: all 3-digits numbers which are divisable by 7 or 9
# can't make: adding numbers to list!
# ____________________

# Don't know why it is not working in this repository
# In different repository, exactly the same code works!
# "bash: syntax error near unexpected token '('
# ____________________
# works in "python folder"
# ____________________

list_of_3digits_numbers = []


def nextline():
    print()


def result(N):
    for number in range(N):
        # 208 is the number of 25 results!! just change N -> 208
        if number % 7 == 0 or number % 9 == 0:
            number_str = str(number)
            number_length = len(str(number))
            number_length_int = int(number_length)
            if number_length_int == 3:
                print(number_str + ' ', end='')

                # list_of_3digits_numbers.append(str(number))
                # number_str = str(number)
                # print(str(number) + ' ', end='')
                
        else:
            pass

        
nextline()
N = int(input('Range? '))
nextline()

print('Your range is: ', N)
print(len(str((N))))
nextline()

print('Numbers divisible by 7 or 9 are: ')
print(list_of_3digits_numbers)

for counter, value in enumerate(list_of_3digits_numbers):
    print(counter, value)

for p in list_of_3digits_numbers:
    print(p)


result(N)

nextline()
nextline()


