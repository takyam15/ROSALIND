def mortal_fibonacci(n, m=3):
    living = [1, 1]
    for i in range(2, n):
        if i < m:
            living += [living[-2] + living[-1]]
        elif i == m:
            living += [living[-2] + living[-1] - 1]
        else:
            living += [living[-2] + living[-1] - living[-m-1]]
    return living[n-1]


def mortal_fibonacci_recursive(n, m=3):
    if n < 0:
        return 0
    elif n <= 2:
        return 1
    return mortal_fibonacci(n-2, m) + mortal_fibonacci(n-1, m) - mortal_fibonacci(n-m-1, m)


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_fibd.txt') as f:
        n, m = f.read().strip().split(' ')
    rabbits = mortal_fibonacci(int(n), int(m))
    print(rabbits)
    with open('./dataset/rosalind_fibd.txt') as f:
        n, m = f.read().strip().split(' ')
    rabbits = mortal_fibonacci(int(n), int(m))
    print(rabbits)
    with open('./submission/mortal_fibonacci_rabbits.txt', mode='w') as f:
        f.write(str(rabbits))
