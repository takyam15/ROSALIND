def find_majority_element(array):
    counts = {}
    for element in array:
        if element not in counts:
            count = array.count(element)
            if count > len(array) / 2:
                return element
            counts[element] = count
    return -1


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_maj.txt') as f:
        k, n = f.readline().strip().split(' ')
        arrays = [array.split(' ') for array in f.read().strip().split('\n')]
    majority_elements = [find_majority_element(array) for array in arrays]
    answer = ' '.join([str(n) for n in majority_elements])
    print(answer)
    with open('./dataset/rosalind_maj.txt') as f:
        k, n = f.readline().strip().split(' ')
        arrays = [array.split(' ') for array in f.read().strip().split('\n')]
    majority_elements = [find_majority_element(array) for array in arrays]
    answer = ' '.join([str(n) for n in majority_elements])
    #print(answer)
    with open('./submission/majority_element.txt', mode='w') as f:
        f.write(answer)
