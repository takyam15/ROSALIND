# Find a Profile-most Probable k-mer in a String


def read(file):
    with open(file) as f:
        string = f.readline().strip()
        k = int(f.readline().strip())
        profile_matrix = {
            'A': [float(p) for p in f.readline().strip().split(' ')],
            'C': [float(p) for p in f.readline().strip().split(' ')],
            'G': [float(p) for p in f.readline().strip().split(' ')],
            'T': [float(p) for p in f.readline().strip().split(' ')]
        }
    return string, k, profile_matrix


def compute_prob(pattern, profile_matrix):
    prob = 1
    for i, s in enumerate(pattern):
        prob *= profile_matrix[s][i]
    return prob


def main(file, export=True):
    string, k, profile_matrix = read(f'./dataset/{file}.txt')
    probs = {}
    for i in range(len(string)-k+1):
        pattern = string[i:i+k]
        probs[pattern] = compute_prob(pattern, profile_matrix)
    k_mer = [pattern for pattern in probs if probs[pattern] == max(probs.values())][0]
    print(k_mer)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(k_mer)


if __name__ == '__main__':
    main('sample_rosalind_ba2c')
    main('rosalind_ba2c')
