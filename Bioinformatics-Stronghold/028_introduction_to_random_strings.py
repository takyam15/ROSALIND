import numpy as np


def calc_prob(s, gc):
    nucreotide_probs = {
        'A': (1 - gc) / 2,
        'C': gc / 2,
        'G': gc / 2,
        'T': (1 - gc) / 2
    }
    prob = 1
    for char in s:
        prob *= nucreotide_probs[char]
    return np.log10(prob)


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_prob.txt') as f:
        s = f.readline().strip()
        gc_contents = f.readline().strip().split(' ')
    probs = []
    for gc in gc_contents:
        probs.append(calc_prob(s, float(gc)))
    answer = ' '.join([str(prob) for prob in probs])
    print(answer)
    with open('./dataset/rosalind_prob.txt') as f:
        s = f.readline().strip()
        gc_contents = f.readline().strip().split(' ')
    probs = []
    for gc in gc_contents:
        probs.append(calc_prob(s, float(gc)))
    answer = ' '.join([str(prob) for prob in probs])
    print(answer)
    with open('./submission/introduction_to_random_strings.txt', mode='w') as f:
        f.write(answer)
