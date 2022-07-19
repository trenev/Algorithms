def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)

nodes_count = int(input())
edges_count = int(input())

graph = []
edges = set()
important_streets = []

[graph.append([]) for _ in range(nodes_count)]

for _ in range(edges_count):
    first, second = [int(x) for x in input().split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    edges.add((min(first, second), max(first, second)))

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * nodes_count

    dfs(0, graph, visited)

    if not all(visited):
        important_streets.append((first, second))

    graph[first].append(second)
    graph[second].append(first)

print('Important streets:')
[print(*x) for x in important_streets]