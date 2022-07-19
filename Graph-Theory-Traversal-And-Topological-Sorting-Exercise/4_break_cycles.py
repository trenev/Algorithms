def dfs(node, visited, graph):
    if node in visited:
        return
    
    visited.add(node)

    for child in graph[node]:
        dfs(child, visited, graph)


def path_to_destination(source, destination, graph):
    visited = set()

    dfs(source, visited, graph)

    return destination in visited


node_count = int(input())

graph = {}
edges = []
edges_to_remove = []

for _ in range(node_count):
    node, children_str = input().split(' -> ')
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_to_destination(source, destination, graph):
        edges_to_remove.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(edges_to_remove)}')
[print(f'{x[0]} - {x[1]}') for x in edges_to_remove]
