def get_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 0
            result[child] += 1

    return result


def find_node_without_dependencies(dependencies):
    for node, _ in dependencies.items():
        if dependencies[node] == 0:
            return node
    return


nodes_count = int(input())
graph = {}
has_cycles = False
sorted_nodes = []

for _ in range(nodes_count):
    node, children = input().split(' ->')
    if children.strip():
        graph[node] = children.strip().split(', ')
    else:
        graph[node] = []

dependencies = get_dependencies(graph)

while dependencies:
    node_to_remove = find_node_without_dependencies(dependencies)

    if not node_to_remove:
        has_cycles = True
        break

    del dependencies[node_to_remove]
    sorted_nodes.append(node_to_remove)

    for node in graph[node_to_remove]:
        dependencies[node] -= 1

if has_cycles:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")
