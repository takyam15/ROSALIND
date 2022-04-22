# Find the Most Frequent Words in a String


def read(file):
    with open(file) as f:
        string = f.readline().strip()
        k = int(f.readline().strip())
    return string, k


def find_frequent_words(string, k):
    words = {}
    for i in range(len(string)-k+1):
        substring = string[i:i+k]
        words[substring] = words.get(substring, 0) + 1
    frequent_words = [
        word for word in words if words[word] == max(words.values())
    ]
    return frequent_words


def main(file, export_file=True):
    string, k = read(f'./dataset/{file}.txt')
    frequent_words = find_frequent_words(string, k)
    output = ' '.join(frequent_words)
    print(output)
    if export_file:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba1b')
    main('rosalind_ba1b')
