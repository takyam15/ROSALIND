from itertools import permutations


def create_strings(strings, n):
    strings = sorted(strings)
    return list(permutations(strings, n))


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_lexf.txt') as f:
        strings = f.readline().strip().split(' ')
        n = f.readline().strip()
    answer_list = sorted([''.join(string) for string in create_strings(strings, int(n))] + [string*2 for string in strings])
    answer = '\n'.join(answer_list)
    print(answer)
    with open('./dataset/rosalind_lexf.txt') as f:
        strings = f.readline().strip().split(' ')
        n = f.readline().strip()
    answer_list = sorted([''.join(string) for string in create_strings(strings, int(n))] + [string*2 for string in strings])
    answer = '\n'.join(answer_list)
    print(answer)
    with open('./submission/enumerating_k_mers_lexicographically.txt', mode='w') as f:
        f.write(answer)
