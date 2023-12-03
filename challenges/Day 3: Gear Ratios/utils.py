neighbors = lambda r, c: [[r, c-1], [r-1, c-1], [r-1, c], [r-1, c+1], [r, c+1], [r+1, c+1], [r+1, c], [r+1, c-1]]

def dict_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([elem for elem in line[:-1]])
  return array