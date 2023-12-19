input_path = 'challenges/Day 14: Parabolic Reflector Dish/input'

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