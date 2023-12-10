input_path = 'challenges/Day 9: Mirage Maintenance/input'

def next_below(history):
  below = []
  if len(history) == 1: return history[0]
  for i in range(1, len(history)):
    below.append(history[i] - history[i - 1])
  
  return below
      
def next_value(history, memo):
  if all(map(lambda x: x == 0, history)): return 0

  if (not str(history) in memo):
    below = next_below(history)
    next_before = (next_value(below, memo))
    memo[str(history)] = history[-1] + next_before

  return memo[str(history)]

_sum = 0; memo = {}
with open(input_path) as f:
  for line in f:
    history = list(map(int, line[:-1].split(' ')))
    _sum += next_value(history, memo)

print('Part 1: ', _sum)