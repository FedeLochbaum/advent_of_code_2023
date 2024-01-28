def grid_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([int(elem) for elem in line[:-1]])
  return array
  