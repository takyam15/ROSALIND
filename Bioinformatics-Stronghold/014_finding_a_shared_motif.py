def get_dna(file_path):
    dna_dict = {}
    with open(file_path) as f:
        for line in f:
            if line.startswith('>'):
                label = line.strip()
                dna_dict[label] = ''
            else:
                dna_dict[label] += line.strip()
    return dna_dict


def find_shared_motif(strings):
    lengths = {}
    for string in strings:
        lengths[string] = len(string)
    short_str, min_len = [dna for dna in lengths.items() if dna[1] == min(lengths.values())][0]
    other_strings = list(strings)
    other_strings.remove(short_str)
    length = min_len
    while length > 0:
        start = 0
        end = length
        while end < min_len + 1:
            substring = short_str[start:end]
            if all([substring in string for string in other_strings]):
                return substring
            start += 1
            end += 1
        length -= 1


if __name__ == '__main__':
    dna_dict = get_dna('./dataset/sample_rosalind_lcsm.txt')
    strings = dna_dict.values()
    shared_motif = find_shared_motif(strings)
    print(shared_motif)
    dna_dict = get_dna('./dataset/rosalind_lcsm.txt')
    strings = dna_dict.values()
    shared_motif = find_shared_motif(strings)
    print(shared_motif)
    with open('./submission/finding_a_shared_motif.txt', mode='w') as f:
        f.write(shared_motif)
