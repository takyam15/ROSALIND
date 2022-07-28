def count_degree(edges, n_nodes):
    counts = [0] * n_nodes
    for edge in edges:
        for node in edge:
            counts[int(node)-1] += 1
    return counts


def count_double_degree(edges, counts):
    neighbors = {}
    for edge in edges:
        if neighbors.get(int(edge[0])):
            neighbors[int(edge[0])].append(int(edge[1]))
        else:
            neighbors[int(edge[0])] = [int(edge[1])]
        if neighbors.get(int(edge[1])):
            neighbors[int(edge[1])].append(int(edge[0]))
        else:
            neighbors[int(edge[1])] = [int(edge[0])]
    double_degrees = [0] * len(counts)
    for vertice in neighbors:
        double_degrees[vertice-1] = sum([counts[neighbor-1] for neighbor in neighbors[vertice]])
    return double_degrees


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_ddeg.txt') as f:
        n, m = f.readline().strip().split(' ')
        edges = [edge.strip().split(' ') for edge in f.read().strip().split('\n')]
    counts = count_degree(edges, int(n))
    double_degrees = count_double_degree(edges, counts)
    answer = ' '.join([str(num) for num in double_degrees])
    print(answer)
    with open('./dataset/rosalind_ddeg.txt') as f:
        n, m = f.readline().strip().split(' ')
        edges = [edge.strip().split(' ') for edge in f.read().strip().split('\n')]
    counts = count_degree(edges, int(n))
    double_degrees = count_double_degree(edges, counts)
    answer = ' '.join([str(num) for num in double_degrees])
    #print(answer)
    with open('./submission/double_degree_array.txt', mode='w') as f:
        f.write(answer)
