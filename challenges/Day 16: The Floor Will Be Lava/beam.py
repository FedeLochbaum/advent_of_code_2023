input_path = 'challenges/Day 16: The Floor Will Be Lava/input'
from utils import grid_from_file, DIRS, SPLIT, MIRRORS

is_valid = lambda r, c, grid: r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
it_must_split = lambda elem, dir: elem in SPLIT and dir in SPLIT[elem]
new_direction = lambda elem, dir: MIRRORS[elem][dir] if elem in MIRRORS else dir

def energized_row(r, grid, energized):
  res = []
  for c in range(len(grid[r])):
    res.append('#' if (r, c) in energized else grid[r][c])
  return res

def show_grid(grid, energized):
  print('show_grid')
  for r in range(len(grid)):
    print(''.join(energized_row(r, grid, energized)))
      
  print('\n')

def split(grid, r, c, dir): return list(map( lambda n_dir: (r + n_dir[0], c + n_dir[1], n_dir), SPLIT[grid[r][c]][dir]))

def run_until_stop(grid, beams, visited, bound):
  prev = len(visited)
  beams, visited = move_beams(grid, beams, visited)
  
  current = len(visited)
  
  while(bound > 0):
    if prev == current: bound-=1
    beams, visited = move_beams(grid, beams, visited)

    prev = current
    current = len(visited)

  return current

def move_beams(grid, beams, visited):
  _beams = []
  for beam in beams:
    r, c, dir = beam

    if not is_valid(r, c, grid): continue

    visited.add((r, c))

    if it_must_split(grid[r][c], dir): _beams += split(grid, r, c, dir); continue

    dir = new_direction(grid[r][c], dir)
    
    n_r, n_c = r + dir[0], c + dir[1]
    _beams.append([n_r, n_c, dir])

  return _beams, visited

grid = grid_from_file(input_path)

print('Part 1: ', run_until_stop(grid, [(0, 0, DIRS['RIGHT'])], set(), 20))

# Part 2