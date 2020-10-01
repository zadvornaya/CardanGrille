import random
import numpy as np


def generateGrille(n: int):
    size = n * 2
    grille = np.zeros((size, size), dtype='uint8')

    seq = np.arange(1, n * n + 1)
    random.shuffle(seq)
    quant = random.randint(1, seq.shape[0] // 2)
    print(seq, " ", quant)
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[i, j] = 1
            k += 1

    seq = seq[quant:]
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 0 else 0
    print(seq, " ", quant)
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[j, size - i - 1] = 1
            k += 1

    seq = seq[quant:]
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 0 else 0
    print(seq, " ", quant)
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[size - i - 1, size - j - 1] = 1
            k += 1

    seq = seq[quant:]
    quant = seq.shape[0]
    print(seq, " ", quant)
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[size - j - 1, i] = 1
            k += 1

    print(grille)


def codeCardanGrille(msg: str, n: int):
    pass
    # return codedMsg


if __name__ == '__main__':
    generateGrille(4)
