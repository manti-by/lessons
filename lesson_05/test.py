import random


def secret_santa(*names):
    names = list(names)
    pairs = {}
    while names:
        person_1 = random.choice(names)
        names.remove(person_1)
        person_2 = random.choice(names)
        names.remove(person_2)
        pairs[person_1] = person_2
    return pairs

print(secret_santa("Denis", "Ira", "Dima", "Oleg", "Olya", "Sasha"))
