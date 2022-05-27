"""
Вывести в порядке возрастания все простые числа, расположенные между n и m
(включая сами числа n и m), а также количество x этих чисел.
"""

n = int(input("Enter N:"))
m = int(input("Enter M:"))

# Генерируем элементы с N по M (включая)
my_count = 0
for element in range(n, m + 1):
    # Проверяем текущий элемент, что он простое число
    # Для этого пробуем делить текущий элемент на все предыдущие по очереди
    is_prime = True
    for divider in range(2, element):
        # Если текущий элемент делится без остатка на текущий делитель
        # то этот элемент не является простым числом
        if divider > 1 and element % divider == 0:
            is_prime = False
            break

    # Текущий элемент - простое число
    if is_prime:
        print(element)
        my_count += 1

print("Total count of prime numbers")
print(my_count)
