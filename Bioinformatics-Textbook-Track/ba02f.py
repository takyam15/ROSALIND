# Implement RandomizedMotifSearch


import numpy as np


def read(file):
    with open(file) as f:
        k, t = [int(n) for n in f.readline().strip().split(' ')]
        strings = f.read().strip().split('\n')
    return k, t, strings


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


def get_motifs(profile_matrix, strings):
    motifs = []
    k = len(profile_matrix)
    for string in strings:
        probs = {}
        for i in range(len(string)-k+1):
            pattern = string[i:i+k]
            probs[pattern] = np.prod([profile_matrix[n][pattern[n]] for n in range(len(pattern))])
        motifs.append([motif for motif in probs if probs[motif]==max(probs.values())][0])
    return motifs


def hamming_distance(string1, string2):
    distance = 0
    for s1, s2 in zip(string1, string2):
        if s1 != s2:
            distance += 1
    return distance


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


def score(motifs):
    pattern = generate_motif(motifs)
    distance = 0
    for motif in motifs:
        distance += hamming_distance(pattern, motif)
    return distance


def main(file, export=True, n_iter=1000):
    k, t, strings = read(f'./dataset/{file}.txt')
    motif_scores = {}
    for _ in range(n_iter):
        motifs = []
        for string in strings:
            i = np.random.randint(len(string)-k+1)
            motifs.append(string[i:i+k])
        best_motifs = motifs
        while True:
            profile_matrix = get_profile(motifs)
            motifs = get_motifs(profile_matrix, strings)
            if score(motifs) < score(best_motifs):
                best_motifs = motifs
            else:
                break
        motif_scores['\n'.join(best_motifs)] = score(best_motifs)
    output = [
        selected_motifs for selected_motifs in motif_scores if motif_scores[selected_motifs]==min(motif_scores.values())
    ][0]
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    #main('sample_rosalind_ba2f', n_iter=1000)
    main('rosalind_ba2f')
