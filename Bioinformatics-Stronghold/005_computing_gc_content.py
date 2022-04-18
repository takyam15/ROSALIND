def compute_gc_content(s):
    return (s.count('G') + s.count('C')) * 100 / len(s)


def get_dnas(file_path):
    dnas = {}
    with open(file_path) as f:
       for line in f:
            if line.startswith('>'):
                label = line.strip().replace('>', '')
                dnas[label] = ''
            else:
                dnas[label] += line.strip()
    return dnas


if __name__ == '__main__':
    dnas = get_dnas('./dataset/sample_rosalind_gc.txt')
    gc_dnas = {}
    for dna in dnas:
        gc_dnas[dna] = compute_gc_content(dnas[dna])
    dnas_max_gc = [dna for dna in gc_dnas.items() if dna[1] == max(gc_dnas.values())]
    answer = ''
    for dna in dnas_max_gc:
        answer += f'{dna[0]}\n{dna[1]}\n'
    print(answer)
    dnas = get_dnas('./dataset/rosalind_gc.txt')
    gc_dnas = {}
    for dna in dnas:
        gc_dnas[dna] = compute_gc_content(dnas[dna])
    dnas_max_gc = [dna for dna in gc_dnas.items() if dna[1] == max(gc_dnas.values())]
    answer = ''
    for dna in dnas_max_gc:
        answer += f'{dna[0]}\n{dna[1]}\n'
    print(answer)
    with open('./dataset/computing_gc_content.txt', mode='w') as f:
        f.write(answer)
