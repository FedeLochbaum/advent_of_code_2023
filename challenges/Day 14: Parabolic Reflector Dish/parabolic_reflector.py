input_path = 'challenges/Day 14: Parabolic Reflector Dish/input'
import functools
import copy

is_movable = lambda x: x == 'O'

def next_row_for_rock(stack):
  if len(columns[col]) == 0: return 0
  top = stack.pop(); stack.append(top)
  return top[0] + 1

columns, rows = [], []
with open(input_path) as f:
  row = 0
  for line in f:
    rows.append([])
    for col in range(len(line[:-1])):
      if row == 0: columns.append([])
      if line[col] == '#': columns[col].append((row, '#'))
      if line[col] == 'O':
        columns[col].append((next_row_for_rock(columns[col]), 'O'))
      rows[-1].append(line[col]) # graph by default
    row += 1

part1 = 0
for columm_i in range(len(columns)):
  while(columns[columm_i]):
    row, rock = columns[columm_i].pop()
    if rock == 'O':
      part1 += (len(rows) - row)

print('Part 1: ', part1)

def move(coor):
  def f(rows):
    for r in range(len(rows)):
      for c in range(len(rows[r])):
        if rows[r][c] == 'O':
          _r, _c = r, c
          while(_r > 0 and rows[_r][_c] == '.'): _r, _c = coor(_r, _c)
          rows[r][c] = '.'
          rows[_r][_c] = 'O'
    return rows
  return f

NORTH = lambda r, c: [r - 1, c]
WEST = lambda r, c: [r, c - 1]
SOUTH = lambda r, c: [r + 1, c]
EAST = lambda r, c: [r, c + 1]

def simulate(rows):
  _rows = copy.deepcopy(rows)
  return functools.reduce(lambda x, f: f(x), [move(NORTH), move(WEST), move(SOUTH), move(EAST)], _rows)

def sum_values(rows):
  _sum = 0
  for r in range(len(rows)):
    for c in range(len(rows[r])):
      if rows[r][c] == 'O': _sum += (len(rows) - r)
  return _sum

for _ in range(1000000001):
  _rows = simulate(rows)
  if _rows == rows: print('Part 2: ', sum_values(rows)); break
  rows = _rows
