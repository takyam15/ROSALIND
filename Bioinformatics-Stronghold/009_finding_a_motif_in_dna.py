def find_motif(s, t):
    length = len(t)
    idxs = []
    for i in range(len(s)-length+1):
        if s[i:i+length] == t:
            idxs.append(str(i+1))
    return idxs


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_subs.txt') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    idxs = find_motif(s, t)
    answer = ' '.join(idxs)
    print(answer)
    with open('./dataset/rosalind_subs.txt') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    idxs = find_motif(s, t)
    answer = ' '.join(idxs)
    print(answer)
    with open('./submission/finding_a_motif_in_dna.txt', mode='w') as f:
        f.write(answer)
