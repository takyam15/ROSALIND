def count_words(s):
    words = s.split(' ')
    word_counts = {}
    for word in words:
        word = word.strip()
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_ini6.txt') as f:
        s = f.read()
    word_counts = count_words(s)
    for word, count in word_counts.items():
        print(word, count)
    with open('./dataset/rosalind_ini6.txt') as f:
        s = f.read()
    word_counts = count_words(s)
    with open('./submission/dictionaries.txt', mode='w') as f:
        for word, count in word_counts.items():
            print(word, count)
            f.write(f'{word} {count}\n')
