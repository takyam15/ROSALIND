# Construct the Overlap Graph of a Collection of k-mers


def read(file):
    with open(file) as f:
        patterns = f.read().strip().split('\n')
    return patterns


def construct_overlap_graph(patterns):
    graph = []
    for pattern in patterns:
        k = len(pattern)
        suffix = pattern[-k+1:]
        for string in patterns:
            prefix = string[:k-1]
            if suffix == prefix:
                graph.append([pattern, string])
    return graph


def main(file, export=True):
    patterns = read(f'./dataset/{file}.txt')
    graph = construct_overlap_graph(patterns)
    output = '\n'.join([f'{pair[0]} -> {pair[1]}' for pair in graph])
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba3c')
    main('rosalind_ba3c')
