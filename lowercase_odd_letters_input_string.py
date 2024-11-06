import re
# Как найти длину введенной строки?
#len("Hello")

# Задача 1. Во введённой строчными английскими буквами строке заменить
# нечётные буквы слов в верхний регистр.
# При выполнении задания сделайте комментарии, поясняющие алгоритм
# Учитывать индекс символа в введённой строке или номер буквы в алфавите по ascii?

# Результат: пришлите в чат ваше решение
def lowercase_odd_letters(string: str) -> str:
    """
    Replace odd letters in string with uppercase.
    :param string:
    :return:
    """
    result_string = ""
    for symbol in string:
        symbol_index_order = string.index(symbol)
        if symbol_index_order % 2 != 0:
            result_string += symbol.upper()
        else:
            result_string += symbol
        # symbol_order_number = ord(symbol)
        # if symbol_order_number % 2 != 0:
        #     result_string += symbol.upper()
        # else:
        #     result_string += symbol
    return result_string

if __name__ == '__main__':
    """
    Main function
    -checking input string matches pattern
    - if it does - calling lowercase_odd_letters
    - if not - output 
    "Wrong input. Input should be a string of lowercase English letters."
    """
    input_string = input("Input string: ")
    pattern = r"[a-z]+"
    if re.fullmatch(pattern, input_string):
        result_str = lowercase_odd_letters(input_string)
        print(result_str)
    else:
         print("Wrong input. Input should be a string of lowercase English letters.")



