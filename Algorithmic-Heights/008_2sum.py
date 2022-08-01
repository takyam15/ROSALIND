def find_negative(array):
    array = [int(n) for n in array]
    for i, n in enumerate(array):
        if -1*n in array[i+1:]:
            return [str(array.index(n)+1), str(array[i+1:].index(-1*n)+i+1+1)]
    return ['-1']


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_2sum.txt') as f:
        k, n = f.readline().strip().split(' ')
        arrays = [array.split(' ') for array in f.read().strip().split('\n')]
    indices = []
    for array in arrays:
        indices.append(find_negative(array))
    indices_str = [' '.join(i) for i in indices]
    answer = '\n'.join([' '.join(i) for i in indices])
    print(answer)
    with open('./dataset/rosalind_2sum.txt') as f:
        k, n = f.readline().strip().split(' ')
        arrays = [array.split(' ') for array in f.read().strip().split('\n')]
    indices = []
    for array in arrays:
        indices.append(find_negative(array))
    indices_str = [' '.join(i) for i in indices]
    answer = '\n'.join([' '.join(i) for i in indices])
    #print(answer)
    with open('submission/2sum.txt', mode='w') as f:
        f.write(answer)
