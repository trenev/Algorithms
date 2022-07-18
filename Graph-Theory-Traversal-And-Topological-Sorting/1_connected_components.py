def dfs(node, visited, graph, component):
    if visited[node]:
        return
    
    visited[node] = True

    for child in graph[node]:
        dfs(child, visited, graph, component)

    component.append(node)


nodes_count = int(input())
graph = []
visited = [False] * nodes_count

for _ in range(nodes_count):
    line = input()
    if line:
        graph.append([int(x) for x in line.split(' ')])
    else:
        graph.append([])

for node in range(nodes_count):
    component = []
    dfs(node, visited, graph, component)
    if component:
        print(f"Connected component: {' '.join([str(x) for x in component])}")
