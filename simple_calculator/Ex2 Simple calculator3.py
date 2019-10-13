keep_asking = True

while keep_asking is True: 

    try:
        first_number = input('Enter a number (or a letter to exit): ')
        first_number_as_int = int(first_number)
    except ValueError:
        exit()

    second_number = input('Enter another number: ')

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
        quotient = first_number_as_int / second_number_as_int
        quotient_as_str = str(quotient)
        print('Result: ' + quotient_as_str)
    


        

