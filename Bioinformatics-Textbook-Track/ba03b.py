# Reconstruct a String from its Genome Path


def read(file):
    with open(file) as f:
        patterns = f.read().strip().split('\n')
    return patterns


def reconstruct_string(patterns):
    text = patterns[0]
    for i in range(1, len(patterns)):
        text += patterns[i][-1]
    return text


def main(file, export=True):
    patterns = read(f'./dataset/{file}.txt')
    text = reconstruct_string(patterns)
    print(text)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(text)


if __name__ == '__main__':
    main('sample_rosalind_ba3b')
    main('rosalind_ba3b')
