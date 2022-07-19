def dfs(node, graph, salaries):
    if salaries[node]:
        return salaries[node]
    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1

    salary = 0

    for child in graph[node]:
        salary += dfs(child, graph, salaries)

    salaries[node] = salary
    return salary


n = int(input())
graph = []
salaries = [None] * n

for _ in range(n):
    children = [x[0] for x in enumerate(list(input())) if x[1] == 'Y']
    graph.append(children)
    
for node in range(n):
    dfs(node, graph, salaries)

print(sum(salaries))
