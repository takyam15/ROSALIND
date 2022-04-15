def add_odd_numbers(start, end):
    if start % 2 == 0:
        start += 1
    if end % 2 != 0:
        end += 1
    return sum(list(range(start, end, 2)))


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_ini4.txt') as f:
        start, end = f.readline().strip().split(' ')
    total = add_odd_numbers(int(start), int(end))
    print(total)
    with open('./dataset/rosalind_ini4.txt') as f:
        start, end = f.readline().strip().split(' ')
    total = add_odd_numbers(int(start), int(end))
    print(total)
    with open('./submission/loops_and_conditions.txt', mode='w') as f:
        f.write(str(total))
