# Find a Position in a Genome Minimizing the Skew


def read(file):
    with open(file) as f:
        genome = f.read().strip()
    return genome


def compute_skew(genome):
    skew = [0]
    for s in genome:
        if s == 'C':
            skew.append(skew[-1]-1)
        elif s == 'G':
            skew.append(skew[-1]+1)
        else:
            skew.append(skew[-1])
    return skew


def main(file, export=True):
    genome = read(f'./dataset/{file}.txt')
    skew = compute_skew(genome)
    output = ' '.join([str(i) for i, n in enumerate(skew) if n == min(skew)])
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba1f')
    main('rosalind_ba1f')
