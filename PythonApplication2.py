from collections import deque

#  (DFS) function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

#  (BFS) function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Sample graph 
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Testing DFS and BFS
print("DFS traversal starting from node A:")
dfs(graph, 'A')
print("\nBFS traversal starting from node A:")
bfs(graph, 'A')
