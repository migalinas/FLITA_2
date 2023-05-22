import graphviz


def read(name_file):
    return [list(map(int, line.strip().split())) for line in open(name_file, 'r')]


def visual(m):
    graph = graphviz.Graph()
    [graph.node(str(node))
     for node in set(range(1, len(m) + 1)) - set([j + 1 for i in range(len(m))
                                                  for j in range(i + 1, len(m)) if m[i][j] != 0])]
    unique_edges = set()
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] != 0:
                edge = (min(i + 1, j + 1), max(i + 1, j + 1))
                if edge not in unique_edges:
                    unique_edges.add(edge)
                    if i == j:
                        graph.edge(str(i + 1), str(j + 1), label=str(m[i][j]), dir='none')
                    else:
                        graph.edge(str(i + 1), str(j + 1), label=str(m[i][j]))
    graph.view()


def visual1(m):
    graph = graphviz.Digraph()
    [graph.node(str(node))
     for node in set(range(1, len(m) + 1)) - set([j + 1 for i in range(len(m))
                                                  for j in range(i + 1, len(m)) if m[i][j] != 0])]
    [graph.edge(str(i + 1), str(j + 1), label=str(abs(m[i][j])),
                dir='forward' if m[i][j] > 0 else 'back') for i in range(len(m)) for j in
     range(len(m)) if m[i][j] != 0]

    graph.view()


def graph_con_th(m):
    return len(m) > 1 and len([(i, j) for i in range(len(m))
                               for j in range(i + 1, len(m)) if m[i][j] != 0]) >= (len(m) - 1) * (len(m) - 2) // 2


def graph_con_dfs(matrix):
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


def add_edge(matrix, v1, v2, weight):
    matrix[v1 - 1][v2 - 1] = weight
    matrix[v2 - 1][v1 - 1] = weight
    matrix[v2 - 1][v1 - 1] = 0


def main():
    while True:
        print("Select option:\n1. Directed graph\n2. Non-directed graph\n")
        choice = int(input("Enter number:"))
        adj_matrix = read('file.txt')
        if choice == 1:
            visual1(adj_matrix)
            print("Connected!") if graph_con_dfs(adj_matrix) else print("Not connected!")
            while True:
                print("Select option:\n1. Add edge\n2. Exit\n")
                ch = int(input("Enter number:"))
                if ch == 1:
                    v1 = int(input("Enter number of first:"))
                    v2 = int(input("Enter number of second:"))
                    weight = int(input("Enter weight of this edge:"))
                    add_edge(adj_matrix, v1, v2, weight)
                    visual1(adj_matrix)
                elif ch == 2:
                    print("Exit...")
                    break
                else:
                    print("Try again!")
            break
        elif choice == 2:
            visual(adj_matrix)
            print("Connected!") if graph_con_th(adj_matrix) else print("Not connected!")
            while True:
                print("Select option:\n1. Add edge\n2. Exit\n")
                ch = int(input("Enter number:"))
                if ch == 1:
                    v1 = int(input("Enter number of first:"))
                    v2 = int(input("Enter number of second:"))
                    weight = int(input("Enter weight of this edge:"))
                    add_edge(adj_matrix, v1, v2, weight)
                    visual(adj_matrix)
                elif ch == 2:
                    print("Exit...")
                    break
                else:
                    print("Try again!")
            break
        else:
            print("Incorrect option!")
            break


if __name__ == '__main__':
    main()
