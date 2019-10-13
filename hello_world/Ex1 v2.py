list_of_guests = []
keep_asking = True

while keep_asking is True:      # w poradniku było boolean "==", ale best practice mówi, żeby używać "is" zamiast "=="
    name = input('What is your name? ')
    if name == '':
        print('Hello world')
        keep_asking = False
    else:
        if name not in list_of_guests:
            list_of_guests.append(name)
            print('Hello ' + name)
        else:
            print('Hello again ' + name)
