import random


def dice():
    print('Dice: ')
    
    # Attacker:
    a1 = random.randrange(1, 6)
    a2 = random.randrange(1, 6)
    a3 = random.randrange(1, 6)
    print('     Attacker: ', a1, '-', a2, '-', a3)

    # Defender:
    d1 = random.randrange(1, 6)
    d2 = random.randrange(1, 6)
    print('     Deffender: ', d1, '-', d2)

    x = a1 - d1
    y = a1 - d2

    print('\n Outcome:')
    print('    Attacker: Lost', x, 'unit')
    print('    Defender: Lost', y, 'unit')


dice()
