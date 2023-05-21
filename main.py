import graphviz


def read_graph_from_file(filename):
    adjacency_matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            adjacency_matrix.append(row)
    return adjacency_matrix


def visualize_graph(adjacency_matrix):
    graph = graphviz.Digraph()

    num_nodes = len(adjacency_matrix)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if adjacency_matrix[i][j] != 0:
                weight = str(abs(adjacency_matrix[i][j]))
                graph.edge(str(i + 1), str(j + 1), label=f'{weight}',
                           dir='forward' if adjacency_matrix[i][j] > 0 else 'back')

    graph.view()


adj_matrix = read_graph_from_file('file.txt')
visualize_graph(adj_matrix)
