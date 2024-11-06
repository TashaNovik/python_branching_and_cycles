"""
Написать программу, которая перемешивает символы исходного
сообщения в блоках по 128 символов и совершает обратное
преобразование.
При выполнении задания сделайте комментарии, поясняющие алгоритм.

"""
import random


def shuffle_blocks(message: str) -> str:
    block_size = 128
    blocks = [message[i:i + block_size] for i in range(0, len(message), block_size)]

    shuffled_message = ""
    shuffle_indices = []
    shuffled_block = ''

    for block in blocks:
        if len(block) < block_size:
            # Дополняем блок до 128 символов, если нужно
            block = block.ljust(block_size)

        # Создаём список индексов и перемешиваем их
        indices = list(range(len(block)))
        random.shuffle(indices)
        shuffle_indices.append(indices)

        # Перемешиваем блок по перемешанным индексам
        shuffled_block = shuffled_block.join(block[i] for i in indices)
        shuffled_message += shuffled_block

    # Сохраняем индексы для обратного преобразования
    # (здесь просто возвращаем их, но в реальной задаче сохраним в файл или иным образом)
    return shuffled_message, shuffle_indices


def unshuffle_blocks(shuffled_message: str, shuffle_indices) -> str:
    block_size = 128
    blocks = [shuffled_message[i:i + block_size] for i in range(0, len(shuffled_message), block_size)]

    original_message = ""

    for block, indices in zip(blocks, shuffle_indices):
        # Создаём список исходной длины для перекодирования
        unshuffled_block = [''] * len(block)

        # Восстанавливаем порядок символов
        for original_index, shuffled_index in enumerate(indices):
            unshuffled_block[shuffled_index] = block[original_index]

        original_message += ''.join(unshuffled_block)

    return original_message.strip()

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


def caesar_decipher(ciphertext: str, shift: int) -> str:
    deciphered_text = ""

    for symbol in ciphertext:
        # Работает только со строчными английскими буквами
        if 'a' <= symbol <= 'z':
            # Вычисление новой позиции символа
            shifted_position = ord(symbol) - shift

            # Корректировка сдвига, если доходит до 'a'
            if shifted_position < ord('a'):
                shifted_position += 26

            decrypted_symbol = chr(shifted_position)
        else:
            # Если символ не является строчной буквой, оставляем его без изменений
            decrypted_symbol = symbol

        deciphered_text += decrypted_symbol

    return deciphered_text


message = "Это пример сообщения для перемешивания. " * 5
len_message = len(message)# Длинное сообщение для проверки
caesar_cipher_string = caesar_cipher(message, 5)
shuffled, indices = shuffle_blocks(message)
print("Перемешанное сообщение:", shuffled)

original = unshuffle_blocks(shuffled, indices)
string_without_caesar_cipher = caesar_decipher(original, 5)
print("Восстановленное сообщение:", original)



