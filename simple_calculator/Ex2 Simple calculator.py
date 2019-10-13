first_number = input('Enter a number (or a letter to exit): ')

second_number = input('Enter another number: ')

sign = input('Enter an operation: ')

if sign == '+':
    first_number_as_str = str(first_number)
    second_number_as_str = str(second_number)
    first_number_as_int = int(first_number)
    second_number_as_int = int(second_number)
    print('Result: ' + first_number_as_int + second_number_as_int)