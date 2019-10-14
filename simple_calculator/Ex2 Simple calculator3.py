keep_asking = True

while keep_asking is True: 

    try:
        first_number = input('Enter first number (or a letter to exit): ')
        first_number_as_int = int(first_number)
    except ValueError:
        print('Wrong number')
        exit()

    try:
        second_number = input('Enter second number (or a letter to exit): ')
        second_number_as_int = int(second_number)
    except ValueError:
        print('Wrong number')
        exit()

    # second_number = input('Enter another number: ')

    sign = input('Enter an operation: ')
    
    if sign == '+':
        second_number_as_int = int(second_number)
        sum = first_number_as_int + second_number_as_int
        sum_as_str = str(sum)
        print('Result: ' + sum_as_str)
    elif sign == '-':
        second_number_as_int = int(second_number)
        difference = first_number_as_int - second_number_as_int
        difference_as_str = str(difference)
        print('Result: ' + difference_as_str)
    elif sign == '*':
        second_number_as_int = int(second_number)
        product = first_number_as_int * second_number_as_int
        product_as_str = str(product)
        print('Result: ' + product_as_str)
    elif sign == '/':
        second_number_as_int = int(second_number)
        try:
            quotient = first_number_as_int / second_number_as_int
        except ZeroDivisionError:
            print('Wrong number')
        
        quotient_as_str = str(quotient)
        print('Result: ' + quotient_as_str)
    


        

