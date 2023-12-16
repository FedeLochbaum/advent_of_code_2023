input_path = 'challenges/Day 11: Cosmic Expansion/input'
from utils import grid_from_file

def expand_grid(graph):
  empty_rows = [i for i, row in enumerate(graph) if '#' not in row]
  empty_cols = [j for j in range(len(graph[0])) if all(row[j] != '#' for row in graph)]
  for i in reversed(empty_rows): graph.insert(i, graph[i].copy())
  for j in reversed(empty_cols):
    for row in graph: row.insert(j, row[j])

  return graph

def galaxies(grid):
  res = []; node = 0;
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == '#': res.append((r, c))
      node +=1
  return res

grid = expand_grid(grid_from_file(input_path))

_galaxies = galaxies(grid)

# def valid_point(point):
#   if point[0] < 0 or point[0] >= len(grid): return False
#   if point[1] < 0 or point[1] >= len(grid[0]): return False
#   return True
    
# def compute_mappers(grid): 
#   indexes = {}; _neighbors = {}; current = 0
#   for r in range(len(grid)):
#     for c in range(len(grid[r])):
#       point = (r, c)
#       indexes[str(point)] = current
#       _neighbors[current] = list(filter(valid_point, neighbors(r, c)))
#       current += 1
#   return indexes, _neighbors

# mapper_indexex, mapper_neighbors = compute_mappers(grid) # { point -> index }, { index -> [ point ] }
# distances = floyd_warshall(mapper_indexex, mapper_neighbors)

manhattan_distance = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

_sum = 0
seen = set()
for g1 in _galaxies:
  for g2 in _galaxies:
    if g1 == g2: continue
    if str((g1, g2)) in seen or str((g2, g1)) in seen: continue
    _sum += manhattan_distance(g1, g2)
    seen.add(str((g1, g2)))

print('Part 1: ', _sum)