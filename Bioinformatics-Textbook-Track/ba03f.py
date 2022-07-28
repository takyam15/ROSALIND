# Find an Eulerian Cycle in a Graph


def read(file):
    with open(file) as f:
        graph = f.read().strip().split('\n')
    adjacency_list_raw = [
        adjacency.split('->') for adjacency in graph
    ]
    adjacency_list = []
    for adjacency in adjacency_list_raw:
        if ',' in adjacency[1]:
            nodes = adjacency[1].split(',')
            adjacency_list.extend(
                [(adjacency[0].strip(), node.strip()) for node in nodes]
            )
        else:
            adjacency_list.append(
                (adjacency[0].strip(), adjacency[1].strip())
            )
    return adjacency_list


def add_edge(cycle, adjacency):
    if cycle[-1] == adjacency[0]:
        cycle.append(adjacency[1])
        return cycle


def find_cycle(cycle, adjacency_list):
    if len(adjacency_list) == 1:
        if cycle[-1] == adjacency_list[0][1]:
            return cycle + adjacency_list[-1]
    else:
        candidates = [
            adj for adj in adjacency_list if adj[0] == cycle[-1]
        ]
        if candidates:
            for candidate in candidates:
                cycle = find_cycle(cycle.append(candidate[1]), adjacency_list.remove(candidate))
                if cycle:
                    return cycle


def form_cycle(adjacency_list):
    for adjacency in adjacency_list:
        adjacency_list_loop = adjacency_list.copy()
        cycle = '->'.join(adjacency)
        #print(cycle)
        adjacency_list_loop.remove(adjacency)
        previous_adjacency = adjacency
        #print(adjacency_list)
        while len(adjacency_list_loop):
            next_adjacency = [
                edge for edge in adjacency_list_loop if edge[0] == previous_adjacency[1]
            ]
            if next_adjacency:  # TODO: ここをどうするか
                cycle_tmp = cycle
                adjacency_list_tmp = adjacency_list_loop.copy()
                for adj in next_adjacency:
                    cycle_tmp += '->' + adj[1]
                    #print(cycle)
                    previous_adjacency = adj
                    adjacency_list_tmp.remove(adj)
                    #print(adjacency_list)
            else:
                break
        if not len(adjacency_list_loop):
            return cycle


def main(file, export=True):
    adjacency_list = read(f'./dataset/{file}.txt')
    #print(adjacency_list)
    #cycle = form_cycle(adjacency_list)
    for adj in adjacency_list:
        start = adj
        cycle = find_cycle(start, )
    cycle = find_cycle([], adjacency_list)
    output = '->'.join(cycle)
    print(output)
    if export:
        with open(f'./submission/{file}.txt', mode='w') as f:
            f.write(output)


if __name__ == '__main__':
    main('sample_rosalind_ba3f')
    main('rosalind_ba3f')
