import random


def risk():
    print("Dice:")
    # attacker  
    v1 = random.randrange(1, 6)
    v2 = random.randrange(1, 6)
    v3 = random.randrange(1, 6)
    print("    Attacker:", v1, "-", v2, "-", v3)

    # defender =
    v4 = random.randrange(1, 6)
    v5 = random.randrange(1, 6)
    print("    Defender:", v4, "-", v5)


risk()