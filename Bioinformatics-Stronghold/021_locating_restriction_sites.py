complements = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}


def read_fasta(file_path):
    fasta_dict = {}
    with open(file_path) as f:
        for line in f:
            if line.strip().startswith('>'):
                label = line.strip().replace('>', '')
                fasta_dict[label] = ''
            else:
                fasta_dict[label] += line.strip()
    return fasta_dict


def check_palindrome(s, min_len=4):
    if len(s) < min_len:
        return False
    for i in range(len(s)):
        if s[i] != complements[s[-i-1]]:
            return False
    return True


def find_palindrome(s):
    idxs = []
    sequences = []
    for i in range(len(s)):
        length = 4
        while length <= 12 and i+length<=len(s):
            strings = s[i:i+length]
            if check_palindrome(strings):
                idxs.append(i+1)
                sequences.append(strings)
            length += 1
    return idxs, sequences


if __name__ == '__main__':
    fasta_dict = read_fasta('./dataset/sample_rosalind_revp.txt')
    answer = ''
    for s in fasta_dict.values():
        idxs, sequences = find_palindrome(s)
        answer_list = [f'{idx} {len(sequence)}' for idx, sequence in zip(idxs, sequences)]
        answer += '\n'.join(answer_list)
    print(answer)
    fasta_dict = read_fasta('./dataset/rosalind_revp.txt')
    answer = ''
    for s in fasta_dict.values():
        idxs, sequences = find_palindrome(s)
        answer_list = [f'{idx} {len(sequence)}' for idx, sequence in zip(idxs, sequences)]
        answer += '\n'.join(answer_list)
    print(answer)
    with open('./submission/locating_restriction_sites.txt', mode='w') as f:
        f.write(answer)
