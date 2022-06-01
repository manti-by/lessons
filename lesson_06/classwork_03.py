"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
где на первом месте номинал карты номинал (6 - 10, J, D, K, A),
а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""
import random


n = ("6", "7", "8", "9", "10", "J", "D", "K", "A")
m = ("H", "D", "C", "S")


def get_random_card():
    random_n = random.choice(n)
    random_m = random.choice(m)
    return random_n, random_m


for _ in range(5):
    print(get_random_card())
