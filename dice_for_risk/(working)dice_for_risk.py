import random

# Don't know why it is not working in this repository
# In different repository, exactly the same code works!
# "bash: syntax error near unexpected token '('
# So this is working version, without variation 2 --> questions added, but doesn't have relation with result
# To work properly, You should input attackers = 3 and deffenders = 2
# Input is working, but units are added even when one player has 2 dices and the other 1
# TODO Make a relation between number_of_attackers/deffenders and compared results
# ____________________
# works in "python folder"
# ____________________


def dice():
    number_of_attackers = int(input('How many attackers will play? '))
    number_of_deffenders = int(input('How many deffenders will play? '))

    print()
    print('-----------------------------------')
    print('| Dice: ')
    
    # Attacker:
    a1 = random.randrange(1, 6)
    a2 = random.randrange(1, 6)
    a3 = random.randrange(1, 6)
    if number_of_attackers == 3:
        print('|      Attacker: ', a1, '-', a2, '-', a3)
    elif number_of_attackers == 2:
        print('|      Attacker: ', a1, '-', a2)
    elif number_of_attackers == 1:
        print('|      Attacker: ', a1)
    else:
        exit()

    # Defender:
    d1 = random.randrange(1, 6)
    d2 = random.randrange(1, 6)
    if number_of_deffenders == 2:
        print('|      Deffender: ', d1, '-', d2)
    elif number_of_deffenders == 1:
        print('|      Deffender: ', d1)
    else:
        exit()
    # print('|      Deffender: ', d1, '-', d2)
    print('|')
    
    # x = 1
    # y = 1
    attacker_units = 0
    deffender_units = 0
    attacker_units_first_dice = 0
    deffender_units_first_dice = 0
    attacker_units_second_dice = 0
    deffender_units_second_dice = 0
    attacker_units_total = 0
    deffender_units_total = 0

    x = a1 - d1
    y = a2 - d2
   
    if x == 0:
        attacker_units = attacker_units
        deffender_units = deffender_units
    
    if y == 0:
        attacker_units = attacker_units
        deffender_units = deffender_units
    
    if x > 0:
        deffender_units_first_dice = deffender_units + 1
    
    if x < 0:
        deffender_units_first_dice = deffender_units + 1
    
    if y > 0:
        attacker_units_second_dice = attacker_units + 1
    
    if y < 0:
        deffender_units_second_dice = deffender_units + 1
    
    attacker_units_total = attacker_units_first_dice + attacker_units_second_dice
    deffender_units_total = deffender_units_first_dice + deffender_units_second_dice
       
    print('-----------------------------------')
    print('|\n|  Outcome:')
    print('|     Attacker: Lost', attacker_units_total, 'unit')
    print('|      Defender: Lost', deffender_units_total, 'unit')
    print('-----------------------------------')
    print()


dice()