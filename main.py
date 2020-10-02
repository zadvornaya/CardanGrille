import random
import string

import numpy as np


def generateGrille(n: int):
    size = n * 2
    grille = np.zeros((size, size), dtype='uint8')

    seq = np.arange(1, n * n + 1)
    random.shuffle(seq)
    quant = random.randint(1, seq.shape[0] // 2)
    # print(seq, " ", quant)
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[i, j] = 1
            k += 1

    seq = seq[quant:]
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 0 else 0
    # print(seq, " ", quant)
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[j, size - i - 1] = 1
            k += 1

    seq = seq[quant:]
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 0 else 0
    # print(seq, " ", quant)
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[size - i - 1, size - j - 1] = 1
            k += 1

    seq = seq[quant:]
    quant = seq.shape[0]
    # print(seq, " ", quant)
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[size - j - 1, i] = 1
            k += 1

    # print(grille)
    return grille


def codeByCardanGrille(msg: str, n: int):
    grille = generateGrille(n)
    codedGrl = np.zeros(grille.shape, 'U1')
    size = n * 2

    # Прямой обход (0)
    for i in range(size):
        for j in range(size):
            if grille[i, j] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(string.ascii_letters)
                codedGrl[i, j] = letter

    print(codedGrl)

    # Обход при повороте 90
    for i in range(size):
        for j in range(size):
            if grille[j, size - i - 1] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(string.ascii_letters)
                codedGrl[j, size - i - 1] = letter
    print(codedGrl)
    # Обход при повороте 180
    for i in range(size):
        for j in range(size):
            if grille[size - i - 1, size - j - 1] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(string.ascii_letters)
                codedGrl[size - i - 1, size - j - 1] = letter
    print(codedGrl)
    # Обход при повороте 270
    for i in range(size):
        for j in range(size):
            if grille[size - j - 1, i] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(string.ascii_letters)
                codedGrl[size - j - 1, i] = letter

    # return [str(codedGrl), str(grille)]
    return [codedGrl, grille]


if __name__ == '__main__':
    print(codeByCardanGrille("This string", 3))
