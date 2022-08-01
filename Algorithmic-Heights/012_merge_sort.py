def merge_sort(numbers):
    
    if len(numbers) <= 1:
        return numbers
    
    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]
    
    merge_sort(left)
    merge_sort(right)
    
    i = j = k = 0
    while i < len(left) and j < len(right):
        
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1

        k += 1
        
    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1
        
    return numbers


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_ms.txt') as f:
        n = f.readline().strip()
        array = [int(num) for num in f.readline().strip().split(' ')]
    sorted_array = merge_sort(array)
    answer = ' '.join([str(num) for num in sorted_array])
    print(answer)
    with open('./dataset/rosalind_ms.txt') as f:
        n = f.readline().strip()
        array = [int(num) for num in f.readline().strip().split(' ')]
    sorted_array = merge_sort(array)
    answer = ' '.join([str(num) for num in sorted_array])
    #print(answer)
    with open('./submission/merge_sort.txt', mode='w') as f:
        f.write(answer)
