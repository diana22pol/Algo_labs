from collections import defaultdict


def dfs(graph, node, visited, result):
    stack = [node]
    while stack:
        node = stack[-1]
        visited.add(node)
        unvisited_neighbors = [neighbor for neighbor in graph[node] if neighbor not in visited]
        if unvisited_neighbors:
            stack.extend(unvisited_neighbors)
        else:
            stack.pop()
            result.append(node)


def topological_sort(graph):
    visited = set()
    result = []

    for node in list(graph):
        if node not in visited:
            dfs(graph, node, visited, result)

    return result


input_file_path = '../govern.in'
with open(input_file_path, 'r') as f:
    dependencies = [line.strip().split() for line in f]

graph = defaultdict(list)

for tokens in dependencies:
    node = tokens[0]
    neighbors = tokens[1:]
    graph[node].extend(neighbors)

result = topological_sort(graph)

output_file_path = '../govern.out'
with open(output_file_path, 'w') as f:
    for doc in result:
        f.write(doc + '\n')
