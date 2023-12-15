neighbors = lambda r, c: [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
# neighbors = lambda r, c: [[r, c-1], [r-1, c-1], [r-1, c], [r-1, c+1], [r, c+1], [r+1, c+1], [r+1, c], [r+1, c-1]]

def grid_from_file(input_path):
  array = []; r = 0; node = 0
  with open(input_path) as f:
    for line in f: 
      row = []
      for c in range(len(line[:-1])):
        row.append(line[c])
        node += 1
      array.append(row); r += 1
  return array

def floyd_warshall(mapper_indexex, mapper_neighbors):
  n = len(mapper_indexex)
  distances = [[float('inf')] * n for _ in range(n)]

  for i in range(n): distances[i][i] = 0

  for node, neighbors in mapper_neighbors.items():
    for neighbor in neighbors:
      distances[node][mapper_indexex[str(neighbor)]] = 1

  for k in range(n):
    for i in range(n):
      for j in range(n):
        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

  return distances