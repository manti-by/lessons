"""
Пользователь делает вклад в размере 2130 рублей сроком на 5 лет под 10% годовых (каждый год размер его вклада
увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
Рассчитать сумму на счету пользователя по окончании вклада и вывести на печать, если в конце каждого года ему
начисляется бонус в размере 120 рублей.
"""

money = 2130
period = 5
tax = 0.1
bonus = 120


# Линейный вариант решения
result = money
result += result * tax + bonus  # 1-й год
result += result * tax + bonus  # 2-й год
result += result * tax + bonus  # 3-й год
result += result * tax + bonus  # 4-й год
result += result * tax + bonus  # 5-й год

print(result)


# С использованием циклов
result = money
while period > 0:
    result += result * tax + bonus
    period -= 1

print(result)
