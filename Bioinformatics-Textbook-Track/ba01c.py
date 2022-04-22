# Find the Reverse Complement of a String


def read(file):
    with open(file) as f:
        s = f.read().strip()
    return s


def create_complement_sequence(s):
    complement_dict = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    return ''.join([complement_dict[char] for char in s[::-1]])


def main(file, export=True):
    s = read(f'./dataset/{file}.txt')
    sc = create_complement_sequence(s)
    print(sc)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(sc)


if __name__ == '__main__':
    main('sample_rosalind_ba1c')
    main('rosalind_ba1c')
