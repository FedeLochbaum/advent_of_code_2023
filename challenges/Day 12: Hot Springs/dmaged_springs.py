input_path = 'challenges/Day 12: Hot Springs/input'

# operational (.)  damaged (#)  unknown (?)

def arrangements(pieces, constraints, i, j, memo):
  if i == 0 and j == 0: return 1
  if i == 0: return 0

  if not (i, j) in memo:
    if j == 0:
       return int(all(char != '#' for char in pieces[:i]))
    elif pieces[i - 1] == '.':
      result = arrangements(pieces, constraints, i - 1, j, memo)
    else:
      num = constraints[j - 1]
      if num > i or any(char == '.' for char in pieces[i-num:i]): result = 0
      elif i > num and pieces[i - num - 1] == '#': result = 0
      else:
        result = arrangements(pieces, constraints, max( i - num - 1, 0), j - 1, memo)
      if pieces[i - 1] == '?':
        result += arrangements(pieces, constraints, i - 1, j, memo)
    memo[(i, j)] = result

  return memo[(i, j)]

part1, part2 = 0, 0
with open(input_path) as f:
  for line in f:
    pieces, constraints = line[:-1].split(' ')
    constraints = list(map(int, constraints.split(',')))
    pieces2 = '?'.join([pieces] * 5)
    constraints2 = constraints * 5
    part1 += arrangements(pieces, constraints, len(pieces), len(constraints), {})
    part2 += arrangements(pieces2, constraints2, len(pieces2), len(constraints2), {})

print('Part 1: ', part1)
print('Part 2: ', part2)