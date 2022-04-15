def add_squares(numbers):
    return sum([int(n) ** 2 for n in numbers])


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_ini2.txt') as f:
        numbers = f.read().strip().split(' ')
    total_squares = add_squares(numbers)
    print(total_squares)
    with open('./dataset/rosalind_ini2.txt') as f:
        numbers = f.read().strip().split(' ')
    total_squares = add_squares(numbers)
    print(total_squares)
    with open('./submission/variables_and_some_arithmetic.txt', mode='w') as f:
        f.write(str(total_squares))
