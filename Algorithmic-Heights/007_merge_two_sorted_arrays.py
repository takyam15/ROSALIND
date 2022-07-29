if __name__ == '__main__':
    with open('./dataset/sample_rosalind_mer.txt') as f:
        n = f.readline().strip()
        a = [int(n) for n in f.readline().strip().split(' ')]
        m = f.readline().strip()
        b = [int(n) for n in f.readline().strip().split(' ')]
    merged_array = a + b
    merged_array.sort()
    answer = ' '.join([str(n) for n in merged_array])
    print(answer)
    with open('./dataset/rosalind_mer.txt') as f:
        n = f.readline().strip()
        a = [int(n) for n in f.readline().strip().split(' ')]
        m = f.readline().strip()
        b = [int(n) for n in f.readline().strip().split(' ')]
    merged_array = a + b
    merged_array.sort()
    answer = ' '.join([str(n) for n in merged_array])
    #print(answer)
    with open('./submission/merge_two_sorted_arrays.txt', mode='w') as f:
        f.write(answer)
