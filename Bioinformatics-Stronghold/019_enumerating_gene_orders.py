from itertools import permutations


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_perm.txt') as f:
        n = int(f.read().strip())
    answer = f'{len(list(permutations(range(1, n+1))))}'
    for permutation in permutations(range(1, n+1)):
        permutation_str = [str(n) for n in permutation]
        answer += f'\n{" ".join(permutation_str)}'
    print(answer)
    with open('./dataset/rosalind_perm.txt') as f:
        n = int(f.read().strip())
    answer = f'{len(list(permutations(range(1, n+1))))}'
    for permutation in permutations(range(1, n+1)):
        permutation_str = [str(n) for n in permutation]
        answer += f'\n{" ".join(permutation_str)}'
    print(answer)
    with open('./submission/enumerating_gene_orders.txt', mode='w') as f:
        f.write(answer)
