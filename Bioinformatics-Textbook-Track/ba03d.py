# Construct the De Bruijn Graph of a String


def read(file):
    with open(file) as f:
        k = int(f.readline().strip())
        text = f.readline().strip()
    return k, text


def construct_graph(k, text):
    graph = {}
    for i in range(len(text)-k+1):
        pattern = text[i:i+k-1]
        if pattern in graph:
            graph[pattern] += f',{text[i+1:i+k]}'
        else:
            graph[pattern] = text[i+1:i+k]
    return graph


def main(file, export=True):
    k, text = read(f'./dataset/{file}.txt')
    graph = construct_graph(k, text)
    output = '\n'.join([f'{key} -> {value}' for key, value in graph.items()])
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba3d')
    main('rosalind_ba3d')
