def extract_even_numbered_lines(input_file_path):
    exported_text = ''
    with open(input_file_path) as f:
        for i, line in enumerate(f):
            if i % 2 == 1:
                exported_text += line
    return exported_text


if __name__ == '__main__':
    text = extract_even_numbered_lines('./dataset/sample_rosalind_ini5.txt')
    print(text)
    text = extract_even_numbered_lines('./dataset/rosalind_ini5.txt')
    print(text)
    with open('./submission/working_with_files.txt', mode='w') as f:
        f.write(text)
