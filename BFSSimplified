# Graph search using BFS
import queue


def bfs(graph, start):
    visited = [start]
    queue = [start]
    level = {start: 0}
    while queue:
        vertex = queue.pop()
        # get all neighbours
        neighbours = graph[vertex]
        for neighbour in neighbours:
            while neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                level[neighbour] = level[vertex] + 1
    print(level)
    return visited


graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}
if __name__ == "__main__":
    ans = bfs(graph, 'A')
    print(ans)
