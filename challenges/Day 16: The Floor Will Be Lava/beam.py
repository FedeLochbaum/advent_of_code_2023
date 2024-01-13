input_path = 'challenges/Day 16: The Floor Will Be Lava/input0'
import copy
from utils import grid_from_file, DIRS, SPLIT, MIRRORS

is_valid = lambda r, c, grid: r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
it_must_split = lambda cur, dir: cur in SPLIT and dir in SPLIT[cur]
new_direction = lambda cur, dir: MIRRORS[cur][dir] if cur in MIRRORS else dir

def split(grid, r, c, dir):
  beams = []
  if not dir in SPLIT[grid[r][c]]: return []

  for n_dir in SPLIT[grid[r][c]][dir]:
    n_r, n_c = r + n_dir[0], c + n_dir[1]
    if is_valid(n_r, n_c, grid): beams.append((n_r, n_c, n_dir))

  return beams

def run_until_stop(grid, beams, energized):
  prev = len(energized)
  beams, energized = iteration(grid, beams, energized)
  current = len(energized)
  print('beams: ', beams, ' energized: ', energized, ' prev: ', prev, ' current: ', current)
  
  while(prev != current):
    beams, energized = iteration(grid, beams, energized)
    prev = current
    current = len(energized)
  return current

def iteration(grid, beams, old_energized):
  energized = copy.deepcopy(old_energized)
  n_beams = []
  print('beams: ', beams)
  for beam in beams:
    r, c, dir = beam
    print('VAMOS POR LA POS: ', r, c, dir)
    
    energized.add((r, c)) # energize cell
    print('energized: ', energized)

    n_r, n_c = r + dir[0], c + dir[1]
    if not is_valid(n_r, n_c, grid): continue

    if grid[n_r][n_c] in MIRRORS or grid[n_r][n_c] in SPLIT: energized.add((n_r, n_c))

    if it_must_split(grid[n_r][n_c], dir): n_beams += split(grid, n_r, n_c, dir); print('n_beams: ', n_beams); continue # split must check if are valid pos

    n_dir = new_direction(grid[n_r][n_c], dir)
    n_beams.append([n_r, n_c, n_dir])

  return n_beams, energized

grid = grid_from_file(input_path)

print('Part 1: ', run_until_stop(grid, [(0, 0, DIRS['RIGHT'])], set()))
