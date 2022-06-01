"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать также
функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""

import base64

input_string = input("Enter a word for encryption: ")
encryption_key = input("Enter an encryption key: ")


def printable_encrypted_string(string):
    """
    Зашифрованное сообщение не читабельно, т.к. содержит много
    непечатаемых символов таких как табуляция, новая строка и т.д.
    поэтому мы преобразуем это сообщение в строку в кодировке base64
    """
    message_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode("ascii")


def get_key_symbol(key, index):
    """
    Если длина нашего ключа меньше начальной строки
    мы получаем следующий символ с самого начала в цикле
    """
    if index > len(key) - 1:
        return key[index % len(key)]
    return key[index]


def xor_cipher(string, key):
    result = []
    for index, symbol in enumerate(string):
        result.append(chr(ord(symbol) ^ ord(get_key_symbol(key, index))))
    return "".join(result)


encrypted_string = xor_cipher(input_string, encryption_key)
print("Encrypted string: " + printable_encrypted_string(encrypted_string))

decrypted_string = xor_cipher(encrypted_string, encryption_key)
print("Decrypted string: " + decrypted_string)
