import math
import random
import string

import numpy as np


# class CardanGrille():

def arrayToString(array):
    return "".join(s for s in np.array_str(array) if s not in "[ ]'" and s.isprintable())


def _generateGrille(n: int):
    size = n * 2
    grille = np.zeros((size, size), dtype='uint8')

    # Прямой обход (0)
    seq = np.arange(1, n * n + 1)
    random.shuffle(seq)
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 1 else 0
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[i, j] = 1
            k += 1

    # Обход при повороте 90
    seq = seq[quant:]
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 1 else 0
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[j, size - i - 1] = 1
            k += 1

    # Обход при повороте 180
    seq = seq[quant:]
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 1 else 0
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[size - i - 1, size - j - 1] = 1
            k += 1

    # Обход при повороте 270
    seq = seq[quant:]
    quant = seq.shape[0]
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[size - j - 1, i] = 1
            k += 1

    return grille


def codeByCardanGrille(msg: str, n: int):
    msg = msg.replace(' ', '_')
    grille = _generateGrille(n)
    codedGrl = np.zeros(grille.shape, 'U1')
    size = n * 2
    symbols = string.ascii_letters + string.digits + "_.,!?"

    # Прямой обход (0)
    for i in range(size):
        for j in range(size):
            if grille[i, j] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(symbols)
                codedGrl[i, j] = letter

    # Обход при повороте 90
    for i in range(size):
        for j in range(size):
            if grille[j, size - i - 1] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(symbols)
                codedGrl[i, j] = letter

    # Обход при повороте 180
    for i in range(size):
        for j in range(size):
            if grille[size - i - 1, size - j - 1] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(symbols)
                codedGrl[i, j] = letter

    # Обход при повороте 270
    for i in range(size):
        for j in range(size):
            if grille[size - j - 1, i] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(symbols)
                codedGrl[i, j] = letter

    return [codedGrl, grille]


def decodeByCardanGrille(codedMsg, key):
    codedGrl = np.array(list(codedMsg), dtype='U1')
    codedGrl = codedGrl.reshape((int(math.sqrt(codedGrl.shape[0])), -1))
    grille = np.array(list(key), dtype='uint8')
    grille = grille.reshape((int(math.sqrt(grille.shape[0])), -1))

    size = grille.shape[0]
    decodedMsg = ""

    # Прямой обход (0)
    for i in range(size):
        for j in range(size):
            if grille[i, j] == 1:
                decodedMsg += codedGrl[i, j]

    # Обход при повороте 90
    for i in range(size):
        for j in range(size):
            if grille[j, size - i - 1] == 1:
                decodedMsg += codedGrl[i, j]

    # Обход при повороте 180
    for i in range(size):
        for j in range(size):
            if grille[size - i - 1, size - j - 1] == 1:
                decodedMsg += codedGrl[i, j]

    # Обход при повороте 270
    for i in range(size):
        for j in range(size):
            if grille[size - j - 1, i] == 1:
                decodedMsg += codedGrl[i, j]

    decodedMsg = decodedMsg.replace('_', ' ')
    return [decodedMsg, size]

# if __name__ == '__main__':
#     print("Введите исходный текст:")
#     msg = input()
#     print("Введите размер малой решетки Кардано:")
#     n = int(input())
#
#     codedRes = codeByCardanGrille(msg, n)
#
#     # print(codedRes[0])
#     # print(codedRes[1])
#
#     codedMsg = arrayToString(codedRes[0])
#     key = arrayToString(codedRes[1])
#
#     print("Закодированное сообщение:")
#     print(codedMsg)
#     print("Ключ:")
#     print(key)
#
#     decodedMsg = decodeByCardanGrille(codedMsg, key)
#
#     print("Раскодированное сообщение:")
#     print(decodedMsg)
