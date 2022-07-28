def insertion_sort(numbers):
    n_swaps = 0
    for i in range(len(numbers)-1):
        if numbers[i+1] < numbers[i]:
            idx = i + 1
            num = numbers[idx]
            while idx >= 1 and num < numbers[idx-1]:
                numbers[idx] = numbers[idx-1]
                n_swaps += 1
                idx -= 1
            numbers[idx] = num
    return numbers, n_swaps


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_ins.txt') as f:
        n = f.readline().strip()
        numbers = [int(number) for number in f.readline().strip().split(' ')]
    _, n_swaps = insertion_sort(numbers)
    print(n_swaps)
    with open('./dataset/rosalind_ins.txt') as f:
        n = f.readline().strip()
        numbers = [int(number) for number in f.readline().strip().split(' ')]
    _, n_swaps = insertion_sort(numbers)
    print(n_swaps)
    with open('./submission/insertion_sort.txt', mode='w') as f:
        f.write(str(n_swaps))
