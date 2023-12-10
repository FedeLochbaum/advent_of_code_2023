input_path = 'challenges/Day 9: Mirage Maintenance/input'

part1 = 0; part2 = 0; memo1 = {}; memo2 = {}

def next_below(history):
  below = []
  if len(history) == 1: return history[0]
  for i in range(1, len(history)):
    below.append(history[i] - history[i - 1])
  
  return below

def before_value(history, memo):
  if all(map(lambda x: x == 0, history)): return 0
  
  if (not str(history) in memo):
    below = next_below(history)
    before_before = before_value(below, memo)
    memo[str(history)] = history[0] - before_before

  return memo[str(history)]

def next_value(history, memo):
  if all(map(lambda x: x == 0, history)): return 0

  if (not str(history) in memo):
    below = next_below(history)
    next_before = next_value(below, memo)
    memo[str(history)] = history[-1] + next_before

  return memo[str(history)]

with open(input_path) as f:
  for line in f:
    history = list(map(int, line[:-1].split(' ')))
    part1 += next_value(history, memo1)
    part2 += before_value(history, memo2)

print('Part 1: ', part1)
print('Part 2: ', part2)
