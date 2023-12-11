neighbors_by_key = {
  '|': lambda r, c: [(r - 1, c), (r + 1, c)],
  '-': lambda r, c: [(r, c - 1), (r, c + 1)],
  'L': lambda r, c: [(r - 1, c), (r, c + 1)],
  'J': lambda r, c: [(r - 1, c), (r, c - 1)],
  'F': lambda r, c: [(r, c + 1), (r + 1, c)],
  '7': lambda r, c: [(r, c - 1), (r + 1, c)],
  # 'S': lambda r, c: [[r, c-1], [r-1, c-1], [r-1, c], [r-1, c+1], [r, c+1], [r+1, c+1], [r+1, c], [r+1, c-1]],
}

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def graph_from_file(input_path):
  graph = {}; r = 0; S = None; cols = 0
  with open(input_path) as f:
    for line in f:
      cols = len(line[:-1])
      for c in range(cols):
        if line[c] == '.': continue
        if line[c] == 'S': S = (r, c); continue
        graph[(r, c)] = neighbors_by_key[line[c]](r, c)
      r += 1
  return r, cols, graph, S

