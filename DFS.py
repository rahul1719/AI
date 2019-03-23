def dfs(graph, s):
    visited = [s]
    explored = []
    while visited:
        vertex = visited.pop()
        if vertex not in explored:
            explored.append(vertex)
        neighbours = graph[vertex]
        for neighbour in neighbours:
            if neighbour not in explored:
                visited.append(neighbour)
    return explored

if "__main__" == __name__:
    # Create a new graph
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    adjacency_matrix = {1: [2, 3], 2: [4, 5],
                        3: [5], 4: [6], 5: [6],
                        6: [7], 7: []}

    ans = dfs(graph, 'C')
    print(ans)
    print(dfs(adjacency_matrix, 1))