def has_cycle(graph):
    visited = [False] * (len(graph) + 1)
    for node in range(1, len(graph)):
        if not visited[node]:
            if bfs(node, None, visited, graph):
                return True
    return False


def bfs(v, parent, visited, graph):
    queue = []
    queue.append((v, parent))

    while queue:
        current_node, parent = queue.pop(0)
        visited[current_node] = True
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                queue.append((neighbor, current_node))
            elif neighbor != parent:
                return True

    return False


def read_graph(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    graph = {}
    for line in lines:
        node, edges = line.strip().split(':')
        graph[int(node)] = list(map(int, edges.split()))
    return graph


def write_output(file_name, output):
    with open(file_name, 'w') as file:
        file.write(str(output))


graph = read_graph("input.txt")
output = has_cycle(graph)
write_output('output.txt', output)
