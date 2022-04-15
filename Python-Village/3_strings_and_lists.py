def extract_strings(input_file_path):
    with open(input_file_path) as f:
        text = f.readline()
        numbers = f.readline().strip().split(' ')
        a, b, c, d = [int(n) for n in numbers]
    return ' '.join([text[a:b+1], text[c:d+1]])


if __name__ == '__main__':
    string = extract_strings('./dataset/sample_rosalind_ini3.txt')
    print(string)
    string = extract_strings('./dataset/rosalind_ini3.txt')
    print(string)
    with open('./submission/strings_and_lists.txt', mode='w') as f:
        f.write(string)
