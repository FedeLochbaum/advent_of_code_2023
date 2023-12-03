input_path = 'challenges/Day 3: Gear Ratios/input'
from utils import neighbors, dict_from_file

sum, gear_ratio_sum = 0, 0

graph = dict_from_file(input_path)
seen = set()

def get_number(row, col):
  while(col >= 0 and graph[row][col].isdigit()): col -= 1
  col += 1; init_col = col; number = ''

  while(col < len(graph[row]) and graph[row][col].isdigit()):
    number += graph[row][col]
    col += 1

  return (row, init_col), int(number)

for row in range(len(graph)):
  for col in range(len(graph[row])):
    char = graph[row][col]
    if char != '.' and not char.isdigit():
      adjacent_numbers, local_ratio = 0, 1
      for _r, _c in neighbors(row, col):
        if graph[_r][_c].isdigit():
          start_p, number = get_number(_r, _c)
          if not start_p in seen:
            adjacent_numbers += 1; local_ratio *= number
            sum += number; seen.add(start_p)
      if char == '*' and adjacent_numbers == 2: gear_ratio_sum += local_ratio
      
print('Part 1: ', sum)
print('Part 2: ', gear_ratio_sum)
