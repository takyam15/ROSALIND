# Implement GibbsSampler


def read(file):
    with open(file) as f:
        k, t, n = f.readline().strip().split(' ')
        strings = f.read().strip().split('\n')
    return int(k), int(t), int(n), strings


def get_profile(motifs):
    k = len(motifs[0])
    t = len(motifs) + 4
    profile_matrix = []
    for i in range(k):
        profile_matrix.append({
            'A': 1 / t,
            'C': 1 / t,
            'G': 1 / t,
            'T': 1 / t
        })
        for j in range(len(motifs)):
            profile_matrix[i][motifs[j][i]] += 1 / t
    return profile_matrix


def main(file, export=True):
    k, t, n, strings = read(f'./dataset/{file}.txt')


if __name__ == '__main__':
    main('sample_rosalind_ba2g')
    #main('rosalind_ba2g')
