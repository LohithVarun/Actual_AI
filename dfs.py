def dfs(graph, node):
  print(node)
  visited = set()

  def dfs_recursive(node):
    visited.add(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        print(neighbor)
        dfs_recursive(neighbor)

  dfs_recursive(node)


graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': [],
}

dfs(graph, 'A')
