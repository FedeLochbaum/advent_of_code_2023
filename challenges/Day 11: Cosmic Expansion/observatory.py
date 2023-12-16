input_path = 'challenges/Day 11: Cosmic Expansion/input'
from utils import grid_from_file

def galaxies(grid):
  res = []; node = 0;
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == '#': res.append((r, c))
      node +=1
  return res

def expand(universe):
  expanded_rows, expanded_cols = set(), set()
  for i in range(len(universe)):
    if all(char == '.' for char in universe[i]): expanded_rows.add(i)
  num_cols = len(universe[0])
  for j in range(num_cols):
    if all(row[j] == '.' for row in universe): expanded_cols.add(j)

  return expanded_rows, expanded_cols

grid = grid_from_file(input_path)
expanded_rows, expanded_cols = expand(grid)
_galaxies = galaxies(grid)

manhattan_distance = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def dist_with_expansion(p1, p2, expansion):
  offset = 0
  mini = min(p1[0], p2[0])
  maxi = max(p1[0], p2[0])
  minj = min(p1[1], p2[1])
  maxj = max(p1[1], p2[1])

  for _ in range(mini + 1, maxi):
    if _ in expanded_rows: offset += ( expansion - 1 )
  
  for _ in range(minj + 1, maxj):
    if _ in expanded_cols: offset += ( expansion - 1 )

  return manhattan_distance(p1, p2) + offset

_sum = 0
seen = set()
for g1 in _galaxies:
  for g2 in _galaxies:
    if g1 == g2: continue
    if str((g1, g2)) in seen or str((g2, g1)) in seen: continue
    _sum += dist_with_expansion(g1, g2, 1000000)
    seen.add(str((g1, g2)))

print('Part 2: ', _sum)