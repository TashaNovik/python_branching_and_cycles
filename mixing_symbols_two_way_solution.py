import random



def shuffle_symbols(string):
    shuffled_string = ''
    # Разделить строку на 128 блоков. Если блоку не хватает 128 символов до его
    # конца, дополнить его пробелами или плюсами, чтобы было видно на дебаге, до 128 символов
    blocks_each_128_symbols = generate_symbol_blocks_from_string(string)
    origin_index_and_symbol_list = generate_list_symbols_and_their_places_in_origin_text(blocks_each_128_symbols)
   # var = len(origin_index_and_symbol_list)
    array_of_indexes = list(range(len(origin_index_and_symbol_list)))
    # Перемешиваем индексы
    random.shuffle(array_of_indexes)
    for index in array_of_indexes:
        shuffled_string += origin_index_and_symbol_list[index][1]

    return shuffled_string, origin_index_and_symbol_list


def generate_list_symbols_and_their_places_in_origin_text(blocks_each_128_symbols):
    current_symbol_index = 0
    origin_index_and_symbol_list = []
    for block in blocks_each_128_symbols:
        for symbol in block:
            origin_index_and_symbol_list.append((current_symbol_index, symbol))
            current_symbol_index += 1

    return origin_index_and_symbol_list


def generate_symbol_blocks_from_string(string):
    blocks_with_correct_size = []
    block_size = 128
    blocks = [string[i:i + block_size] for i in range(0, len(string), block_size)]
    # Лист блоков по 128 символов.
    # Нужно проверить, все ли блоки размером по 128
    # Если не все - Дополнить строку в листе пробелами до 128
    for each_block in blocks:
        each_block_len = len(each_block)
        while len(each_block) < block_size:
            each_block += ' '
        blocks_with_correct_size.append(each_block)
    return blocks_with_correct_size


def unshuffle_symbols(string_after_shuffle, origin_index_and_symbol_list):
    size = len(string_after_shuffle)
    array_of_chars = [""] * size
    correct_index = 0
    for each_symbol in string_after_shuffle:
       for index, symbol in origin_index_and_symbol_list:
            if each_symbol == symbol:
                correct_index = index
                break
       if array_of_chars[correct_index] != '':
           continue
       array_of_chars[correct_index] = each_symbol
    unshuffled_string = "".join(array_of_chars)
    return unshuffled_string


if __name__ == '__main__':
    string_for_shuffle = "Попробуем снова перемешать символы" * 8
    print("Исходное сообщение:", string_for_shuffle)
    string_after_shuffle, origin_index_and_symbol_list = shuffle_symbols(string_for_shuffle)
    print("Перемешанное сообщение:", string_after_shuffle)
    # test :print(len(string_for_shuffle)==len(string_after_shuffle))
    unshuffled_string = unshuffle_symbols(string_after_shuffle, origin_index_and_symbol_list)
    print("Восстановленное сообщение:", unshuffled_string )