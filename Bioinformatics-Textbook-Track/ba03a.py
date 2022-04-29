# Generate the k-mer Composition of a String


def read(file):
    with open(file) as f:
        k = int(f.readline().strip())
        text = f.readline().strip()
    return k, text


def generate_compositions(k, text):
    compositions = [text[i:i+k] for i in range(len(text)-k+1)]
    return sorted(compositions)


def main(file, export=True):
    k, text = read(f'./dataset/{file}.txt')
    compositions = generate_compositions(k, text)
    output = '\n'.join(compositions)
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba3a')
    main('rosalind_ba3a')
