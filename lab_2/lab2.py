from lab_1 import lab1
import random


def print_table(table: list):
    """
        Выводим таблицу
    """
    for row in table:
        print(row)


def shifr_table(msg: str = None):
    """
        Простая перестановка без ключа - один из самых простых методов шифрования, 
        смысл которого заключается в последовательном вписывании букв сообщения в ячейки таблицы, 
        соответственно количество ячеек таблицы не должно быть меньше длины сообщения.
        Ключ: размер таблицы и порядок считывания символов
    """

    # Размер строки в таблице
    size = 20

    if msg is None:
        raise Exception('msg is NoneType')

    # Длина сообщения
    msg_len = len(msg)

    # Генерация таблицы
    table = [['0' for _ in range(size)] for _ in range(size)]

    msg_len_sqrt = int(pow(msg_len, 0.5)) + 1

    char_pos = 0

    for i in range(msg_len_sqrt):
        for j in range(msg_len_sqrt):
            if char_pos < msg_len:
                table[i][j] = msg[char_pos]
                char_pos += 1
            else:
                break

    # print_table(table)

    # Транспонируем полученную матрицу
    shifr_table = [[table[j][i]
                    for j in range(msg_len_sqrt)] for i in range(msg_len_sqrt)]
    print('Зашифрованная таблица:')
    print_table(shifr_table)

    print('\n')
    print('Расшифрованная таблица:')
    deshifr_table = [[shifr_table[j][i]
                      for j in range(msg_len_sqrt)] for i in range(msg_len_sqrt)]

    deshifr_string = ''
    for i in range(msg_len_sqrt):
        for j in range(msg_len_sqrt):
            str_item = deshifr_table[i][j]
            if str_item != '0':
                deshifr_string += deshifr_table[i][j]

    print(f'Строка: {deshifr_string}')


def RSA(M, P, Q, Ko):
    """
        Алгоритм RSA
        :param M - сообщение, которое нужно зашифровать
        :param P - очень большое простое число
        :param Q - очень большое простое число
        :param Ko - Ko и N объявляются открытыми ключами и пересылаются отправителю
    """
    N = P * Q
    m = (P - 1) * (Q - 1)  # функция Эйлера
    if Ko is None or lab1.find_nod(Ko, m) != 1:
        Ko = random.randint(1, m)
    # пока наибольший общий делитель чисел К0 и m не равен 1,
    while lab1.find_nod(Ko, m) != 1:
        Ko = random.randint(1, m)  # продолжаем искать число
    print('открытый ключ Ko =', Ko)
    print('открытый ключ N =', N)
    # находим значение Кс, решив линейное сравнение (лаба 1)
    Kc = lab1.solve_linear_congruence(Ko, 1, m)
    C = pow(M, Ko) % N
    print('Зашифрованное сообщение: ', C)
    M = pow(C, Kc) % N
    print('Расшифрованное сообщение: ', M)
