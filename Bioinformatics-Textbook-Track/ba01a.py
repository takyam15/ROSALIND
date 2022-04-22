# Compute the Number of Times a Pattern Appears in a Text


def read(file):
    with open(file) as f:
        text = f.readline().strip()
        pattern = f.readline().strip()
    return text, pattern


def count_pattern(text, pattern):
    count = 0
    pattern_len = len(pattern)
    for i in range(len(text)-pattern_len+1):
        subtext = text[i:i+pattern_len]
        if subtext == pattern:
            count += 1
    return count


def main(file, export=True):
    text, pattern = read(f'./dataset/{file}.txt')
    count = count_pattern(text, pattern)
    print(count)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(str(count))


if __name__ == '__main__':
    main('sample_rosalind_ba1a')
    main('rosalind_ba1a')
