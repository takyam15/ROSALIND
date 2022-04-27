# Implement GreedyMotifSearch


def read(file):
    with open(file) as f:
        k, t = [int(n) for n in f.readline().strip().split(' ')]
        strings = f.read().strip().split('\n')
    return k, t, strings


def generate_motif(motifs):
    length = len(motifs[0])
    pattern = ''
    for i in range(length):
        counts = {}
        for motif in motifs:
            s = motif[i]
            counts[s] = counts.get(s, 0) + 1
        pattern += [s for s in counts if counts[s]==max(counts.values())][0]
    return pattern


def hamming_distance(string1, string2):
    distance = 0
    for s1, s2 in zip(string1, string2):
        if s1 != s2:
            distance += 1
    return distance


def generate_profile_matrix(motifs):
    k = len(motifs[0])
    t = len(motifs)
    profile_matrix = []
    for i in range(k):
        profile_matrix.append({})
        for motif in motifs:
            profile_matrix[i][motif[i]] = profile_matrix[i].get(motif[i], 0) + 1 / t
    return profile_matrix


def find_most_probable_k_mer(string, profile_matrix):
    k = len(profile_matrix)
    probs = {}
    for i in range(len(string)-k+1):
        substring = string[i:i+k]
        probs[substring] = 1
        for j, s in enumerate(substring):
            probs[substring] *= profile_matrix[j].get(s, 0)
    return [pattern for pattern in probs if probs[pattern]==max(probs.values())][0]


def score(motifs):
    pattern = generate_motif(motifs)
    total = 0
    for motif in motifs:
        d = hamming_distance(pattern, motif)
        total += d
    return total


def main(file, export=True):
    k, t, strings = read(f'./dataset/{file}.txt')
    best_motifs = [string[:k] for string in strings]
    best_score = score(best_motifs)
    for i in range(len(strings[0])-k+1):
        motif0 = strings[0][i:i+k]
        motifs = [motif0]
        for j in range(1, t):
            profile_matrix = generate_profile_matrix(motifs)
            motifs.append(find_most_probable_k_mer(strings[j], profile_matrix))
        if score(motifs) < best_score:
            best_score = score(motifs)
            best_motifs = motifs
    output = '\n'.join(best_motifs)
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba2d')
    main('rosalind_ba2d')
