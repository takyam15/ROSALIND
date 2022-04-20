from scipy.special import perm


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_pper.txt') as f:
        n, k = f.read().strip().split(' ')
    answer = perm(int(n), int(k), exact=True) % 1000000
    print(answer)
    with open('./dataset/rosalind_pper.txt') as f:
        n, k = f.read().strip().split(' ')
    answer = perm(int(n), int(k), exact=True) % 1000000
    print(answer)
    with open('./submission/partial_permutations.txt', mode='w') as f:
        f.write(str(answer))
