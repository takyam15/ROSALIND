import numpy as np


def calc_prob(k, n):
    array = np.random.binomial(k, 0.5, 10000)
    return (array>=n).sum() / 10000


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_lia.txt') as f:
        k, n = f.read().strip().split(' ')
    p = calc_prob(int(k), int(n))
    print(p)
