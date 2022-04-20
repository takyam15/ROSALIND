def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-2) + fib(n-1)


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_fibo.txt') as f:
        n = f.read().strip()
    answer = fib(int(n))
    print(answer)
    with open('./dataset/rosalind_fibo.txt') as f:
        n = f.read().strip()
    answer = fib(int(n))
    print(answer)
    with open('./submission/fibonacci_numbers.txt', mode='w') as f:
        f.write(str(answer))
