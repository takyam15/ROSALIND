def fib(n, k):
    if n >= 3:
        return k * fib(n-2, k) + fib(n-1, k)
    elif n == 1 or n == 2:
        return 1


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_fib.txt') as f:
        n, k = f.read().split(' ')
    answer = fib(int(n), int(k))
    print(answer)
    with open('./dataset/rosalind_fib.txt') as f:
        n, k = f.read().split(' ')
    answer = fib(int(n), int(k))
    print(answer)
    with open('./submission/rabbits_and_recurrence_relations.txt', mode='w') as f:
        f.write(str(answer))
