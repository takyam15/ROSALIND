def count_point_mutations(s, t):
    hamm = 0
    for chars in zip(s, t):
        if chars[0] != chars[1]:
            hamm += 1
    return hamm


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_hamm.txt') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    hamm = count_point_mutations(s, t)
    print(hamm)
    with open('./dataset/rosalind_hamm.txt') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    hamm = count_point_mutations(s, t)
    print(hamm)
    with open('./submission/counting_point_mutations.txt', mode='w') as f:
        f.write(str(hamm))
