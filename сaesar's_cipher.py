"""
Написать программу, которая заменяет каждый символ введённой
строки на 5 позиций вперёд или назад по алфавиту (шифр Цезаря)
При выполнении задания сделайте комментарии, поясняющие алгоритм
и действия каждой строки

Результат: напишите в чате, что у вас получилось
Символы строки должны быть английского алфавита?
В каком регистре должны быть символы?
"""
import re


def caesar_cipher(string: str, shift: int) -> str:
    """
    Caesar's cipher function
    :param string:
    :param shift:
    :return:
    """
    result_string = ""
    for symbol in string:
        symbol_order_number = ord(symbol)
        if symbol_order_number + shift > 122:
            result_string += chr(symbol_order_number + shift - 26)
        else:
            result_string += chr(symbol_order_number + shift)
    return result_string

if __name__ == '__main__':
    """
    Main function
    -checking input string matches pattern
    - if it does - calling caesar_cipher
    - if not - output 
    "Wrong input. Input should be a string of lowercase English letters."
    """
    input_string = input("Input string: ")
    if re.fullmatch(r"[a-z]+", input_string):
        result_str = caesar_cipher(input_string, 5)
        print(result_str)
    else:
        print("Wrong input. Input should be a string of lowercase English letters.")
