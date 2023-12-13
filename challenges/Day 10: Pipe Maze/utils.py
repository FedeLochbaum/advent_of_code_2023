neighbors_by_key = {
  '|': lambda r, c: [(r - 1, c), (r + 1, c)],
  '-': lambda r, c: [(r, c - 1), (r, c + 1)],
  'L': lambda r, c: [(r - 1, c), (r, c + 1)],
  'J': lambda r, c: [(r - 1, c), (r, c - 1)],
  'F': lambda r, c: [(r, c + 1), (r + 1, c)],
  '7': lambda r, c: [(r, c - 1), (r + 1, c)],
}

def grid_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([elem for elem in line[:-1]])
  return array

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

