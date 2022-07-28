def count_degree(edges, n_nodes):
    counts = [0] * n_nodes
    for edge in edges:
        for node in edge:
            counts[int(node)-1] += 1
    return counts


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_deg.txt') as f:
        n, m = f.readline().strip().split(' ')
        edges = [edge.strip().split(' ') for edge in f.read().strip().split('\n')]
    counts = count_degree(edges, int(n))
    answer = ' '.join([str(count) for count in counts])
    print(answer)
    with open('./dataset/rosalind_deg.txt') as f:
        n, m = f.readline().strip().split(' ')
        edges = [edge.strip().split(' ') for edge in f.read().strip().split('\n')]
    counts = count_degree(edges, int(n))
    answer = ' '.join([str(count) for count in counts])
    #print(answer)
    with open('./submission/degree_array.txt', mode='w') as f:
        f.write(answer)
