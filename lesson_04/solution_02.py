"""
Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести
результат (yes/no) на экран. Палиндром - это слово или фраза, которые одинаково читаются
слева направо и справа налево.
"""

user_string = input("Enter a text: ")

if user_string == user_string[::-1]:
    print("Yes")
else:
    print("No")
