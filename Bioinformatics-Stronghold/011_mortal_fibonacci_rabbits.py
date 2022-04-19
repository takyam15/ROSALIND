def mortal_fibonacci(n, m):
    if n < 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return mortal_fibonacci(n-2, m) + mortal_fibonacci(n-1, m) - mortal_fibonacci(n-m, m)


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_fibd.txt') as f:
        n, m = f.read().strip().split(' ')
    rabbits = mortal_fibonacci(int(n), int(m))
    print(rabbits)
