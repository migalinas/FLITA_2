import graphviz


def read(name_file):
    return [list(map(int, line.strip().split())) for line in open(name_file, 'r')]


def visual(m):
    graph = graphviz.Digraph()
    [graph.node(str(node))
     for node in set(range(1, len(m) + 1)) - set([j + 1 for i in range(len(m))
                                                  for j in range(i + 1, len(m)) if m[i][j] != 0])]
    [graph.edge(str(i + 1), str(j + 1), label=str(abs(m[i][j])),
                dir='forward' if m[i][j] > 0 else 'back') for i in range(len(m)) for j in
     range(len(m)) if m[i][j] != 0]

    graph.view()


# Checking for graph connectivity using the DFS algorithm
def graph_con(matrix):
    nodes = len(matrix)
    visited = [False] * nodes
    stack = [1]
    while stack:
        node = stack.pop()
        visited[node] = True

        for n in range(nodes):
            if matrix[node][n] != 0 and not visited[n]:
                stack.append(n)
    return all(visited)


adj_matrix = read('file.txt')
visual(adj_matrix)
print("Graph is connected!") if graph_con(adj_matrix) else print("Graph is not connected!")
