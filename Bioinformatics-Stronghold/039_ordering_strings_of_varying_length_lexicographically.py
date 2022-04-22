from itertools import permutations


def string_order(strings):
    return min([strings.index(s) for s in strings])


def ordering_strings(s, n):
    strings = s * n
    string_list = []
    for i in range(n):
        string_tuples = permutations(strings, i+1)
        string_list += [''.join(tpl) for tpl in string_tuples]
    return sorted(list(set(string_list)), key=string_order)


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_lexv.txt') as f:
        strings = f.readline().strip().split(' ')
        n = f.readline().strip()
    string_list = ordering_strings(strings, int(n))
    answer = '\n'.join(string_list)
    print(answer)
    with open('./dataset/rosalind_lexv.txt') as f:
        strings = f.readline().strip().split(' ')
        n = f.readline().strip()
    string_list = ordering_strings(strings, int(n))
    answer = '\n'.join(string_list)
    #print(answer)
    with open('./submission/ordering_strings_of_varying_length_lexicographically.txt', mode='w') as f:
        f.write(answer)
