# Construct the De Bruijn Graph of a Collection of k-mers


def read(file):
    with open(file) as f:
        patterns = f.read().strip().split('\n')
    return patterns


def construct_graph(patterns):
    graph = {}
    for pattern in patterns:
        k = len(pattern)
        prefix = pattern[:k-1]
        suffix = pattern[-k+1:]
        if prefix in graph:
            graph[prefix] += f',{suffix}'
        else:
            graph[prefix] = suffix
    return graph


def main(file, export=True):
    patterns = read(f'./dataset/{file}.txt')
    graph = construct_graph(patterns)
    output = '\n'.join([f'{k} -> {v}' for k, v in graph.items()])
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba3e')
    main('rosalind_ba3e')
