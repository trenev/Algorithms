def dfc(node, graph, visited, path):
    if node in path:
        raise Exception
    if node in visited:
        return

    visited.add(node)
    path.add(node)

    for child in graph[node]:
        dfc(child, graph, visited, path)

    path.remove(node)


graph = {}
visited = set()

while True:
    line = input()
    if line == 'End':
        break

    node, child = line.split('-')

    if node not in graph:
        graph[node] = []
    if child not in graph:
        graph[child] = []

    graph[node].append(child)

try:
    for node in graph:
        dfc(node, graph, visited, set())

    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
