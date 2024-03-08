def is_safe(graph, color, v, assigned):

  for neighbor in range(len(graph[v])):
    if graph[v][neighbor] == 1 and assigned[neighbor] == color:
      return False
  return True

def solve_map_coloring(graph, colors, m, assigned, v):

  if v == len(graph):
    return True
  for c in range(m):
    if is_safe(graph, colors[c], v, assigned):
      assigned[v] = colors[c]

      if solve_map_coloring(graph, colors, m, assigned, v + 1):
        return True
      assigned[v] = 0

  return False

graph = [
  [0, 1, 1, 1],
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [1, 0, 1, 0]
]


colors = ["Red", "Green", "Blue", "Yellow"]

m = len(colors)

assigned = [0] * len(graph)

if solve_map_coloring(graph, colors, m, assigned, 0):

  for i in range(len(assigned)):
    print(f"Vertex {i} colored with {assigned[i]}")
else:
  print("No solution found")
