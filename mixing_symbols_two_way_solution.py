"""
Написать программу, которая перемешивает символы исходного
сообщения в блоках по 7 символов и совершает обратное
преобразование.
"""
import random


def shuffle_symbols(text):
    shuffled_text = ""
    block_size = 7
    # Нам нужно создать блоки текста корректного размера, как сказано в условии задачи:
    blocks_correct_size = generate_text_blocks_with_valid_size(block_size, text)
    indexes_array = list(range(len(blocks_correct_size) * block_size))
    # Перемешиваем индексы в случайном порядке. Будет создан новый список с перемешанными индексами:
    shuffled_numbers = random.sample(indexes_array, len(indexes_array))
    # Создаем пустой массив символов для хранения перемешанного текста:
    shuffled_symbols_array = [''] * len(indexes_array)
    # Перебираем все блоки текста:
    index = 0
    for block in blocks_correct_size:
        # Перебираем все символы в блоке:
        for each_symbol in block:
            # Добавляем символ в перемешанное сообщение:
            shuffled_symbols_array[shuffled_numbers[index]] = each_symbol
            index += 1
    # Перебираем все символы в перемешанном тексте:
    for i in range(len(shuffled_symbols_array)):
        # Добавляем символ в перемешанное сообщение:
        shuffled_text += shuffled_symbols_array[i]
    return shuffled_text, indexes_array, shuffled_numbers


def generate_text_blocks_with_valid_size(block_size, text):
    # Создаем список с блоками символов по 7 символов в каждом блоке.
    # Блоки в нашем случае являются маленькими строками
    # Если блоку до нужного размера не хватает символа, то добавляем блоку пробел в его конец:
    blocks_correct_size = []
    # здесь изначально строка текста делится на блоки, но размер последнего блока может быть меньше указанного в задаче
    blocks = [text[i:i + block_size] for i in range(0, len(text), block_size)]
    # Если размер блока меньше 7 - "дописываем" пробел в конец блока,
    # и так, пока количество символов в блоке не станет равным 7
    for block in blocks:
        while len(block) < block_size:
            block += ' '
        blocks_correct_size.append(block)
        # Иначе просто добавляем блок в список
    return blocks_correct_size


def unshuffle_symbols(shuffled, indexes_array, shuffled_numbers):
    unshuffled_text = ""
    index = 0
    # Создаем пустой массив символов для хранения восстановленного текста
    list_unshuffled_symbols = [''] * len(indexes_array)
    # Перебираем все символы в перемешанном тексте:
    for i in range(len(list_unshuffled_symbols)):
        # Вычисляем какой символ в перемешанном тексте соответствует какому символу в исходном
        value_for_list = shuffled[index]
        # Какой индекс в перемешанном тексте соответствует таковому в исходном
        index_for_list = shuffled_numbers.index(index)
        # Добавляем символ в исходный текст в его "законное" место
        list_unshuffled_symbols[index_for_list] = value_for_list
        index += 1
        # Перебираем все символы в исходном тексте
    for i in range(len(list_unshuffled_symbols)):
        # Делаем строку с восстановленным тестом, избавляемся от пробелов в конце строки
        unshuffled_text += list_unshuffled_symbols[i]
    return unshuffled_text.strip()


if __name__ == '__main__':
    text = "Hello, world!"
    print("Исходное сообщение:", text)
    shuffled, indexes, shuffled_numbers = shuffle_symbols(text)
    print("Перемешанное сообщение:", shuffled)
    original = unshuffle_symbols(shuffled, indexes, shuffled_numbers)
    print("Восстановленное сообщение:", original)
    print(text == original)
