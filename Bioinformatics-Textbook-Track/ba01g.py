# Compute the Hamming Distance Between Two Strings


def read(file):
    with open(file) as f:
        s = f.readline().strip()
        t = f.readline().strip()
    return s, t


def compute_hamming_distance(s, t):
    distance = 0
    for char1, char2 in zip(s, t):
        if char1 != char2:
            distance += 1
    return distance


def main(file, export=True):
    s, t = read(f'./dataset/{file}.txt')
    distance = compute_hamming_distance(s, t)
    print(distance)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(str(distance))


if __name__ == '__main__':
    main('sample_rosalind_ba1g')
    main('rosalind_ba1g')
