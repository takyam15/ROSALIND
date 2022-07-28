def binary_search(numbers, value):
    left, right = 0, len(numbers) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if numbers[middle] == value:
            return middle + 1
        elif numbers[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def search(numbers, value):

    if value in numbers:
        return numbers.index(value) + 1
    else:
        return -1


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_bins.txt') as f:
        n = f.readline().strip()
        m = f.readline().strip()
        sorted_array = f.readline().strip().split(' ')
        target_array = f.readline().strip().split(' ')
    answer = ' '.join([str(search(sorted_array, value)) for value in target_array])
    print(answer)
    with open('./dataset/rosalind_bins.txt') as f:
        n = f.readline().strip()
        m = f.readline().strip()
        sorted_array = f.readline().strip().split(' ')
        target_array = f.readline().strip().split(' ')
    answer = ' '.join([str(search(sorted_array, value)) for value in target_array])
    #print(answer)
    with open('./submission/binary_search.txt', mode='w') as f:
        f.write(answer)
