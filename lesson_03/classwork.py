x = 17 / 2 % 2 * 3
print(x)

x = 17 / 2 % (2 * 3)
print(x)


olga = 33
maxim = 29
roman = 36

print(olga + maxim + roman)
print((olga + maxim + roman) / 3)


my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
my_set = set(my_list)
print(len(my_list) - len(my_set))


my_slice = my_list[3:6]
print(my_slice[::-1])


size = 13
print([size * 4, size ** 2, size * size, (size ** 2 * 2) ** 0.5])

import math
print([size * 4, size ** 2, size * size, math.sqrt(size ** 2 * 2)])

