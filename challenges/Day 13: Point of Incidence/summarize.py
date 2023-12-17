input_path = 'challenges/Day 13: Point of Incidence/input'

part1, part2 = 0, 0
ASH, ROCK = '.', '#'
def transpose_grid(grid): return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

def get_vert_reflect_line(grid):
  n, m = len(grid), len(grid[0])
  lines = []
  for j in range(1, m):
    width = min(j, m - j)
    if all(tuple(grid[i][j - width:j]) == tuple(grid[i][j:j + width][::-1]) for i in range(n)): lines.append(j)
  return lines

def counts(grid):
  _points = []
  for reflex_row in get_vert_reflect_line(grid): _points.append(reflex_row)
  for reflex_col in get_vert_reflect_line(transpose_grid(grid)): _points.append(100 * reflex_col)
  return _points

def points_part2(grid, scoring):
  _points = None
  for row_i in range(len(grid)):
    for col_i in range(len(grid[0])):
      grid[row_i][col_i] = ASH if grid[row_i][col_i] == ROCK else ROCK
      for x in counts(grid):
        if x != scoring: _points = x; break
      if _points is not None: break
      # If doesn't change, revert the smudge try
      grid[row_i][col_i] = ASH if grid[row_i][col_i] == ROCK else ROCK
    if _points is not None: break
  return _points

with open(input_path) as f:
  grid = []
  for line in list(f.readlines()) + ['\n']:
    if line.strip(): grid.append(list(line.strip())); continue
    scoring = counts(grid)[0]
    part1 += scoring
    part2 += points_part2(grid, scoring)
    grid = []

print('Part 1: ', part1)
print('Part 2: ', part2)
