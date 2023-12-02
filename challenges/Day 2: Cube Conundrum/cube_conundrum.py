import numpy
input_path = 'challenges/Day 2: Cube Conundrum/input'

_max = { 'red': 12, 'green': 13, 'blue': 14 }
sum = 0

# Part 1
def is_possible(set):
  for ball in set.split(', '):
    count, color = ball.split(' ')
    if int(count) > _max[color]: return False

  return True

def is_possible_game(sets):
  for set in sets:
    if not is_possible(set): return False
  return True

with open(input_path) as f:
  for line in f:
    id, sets = line[5: -1].split(':')
    sets = sets[1:].split('; ')
    sum += int(id) if is_possible_game(sets) else 0

print('Part 1: ', sum)

# Part 2
sum = 0

def minimum_per_game(sets):
  res = { 'red': 0, 'green': 0, 'blue': 0 }
  for set in sets:
    for ball in set.split(', '):
      count, color = ball.split(' ')
      res[color] = max(int(count), res[color])

  return list(res.values())

with open(input_path) as f:
  for line in f:
    id, sets = line[5: -1].split(':')
    sets = sets[1:].split('; ')
    sum += numpy.prod(minimum_per_game(sets))

print('Part 2: ', sum)