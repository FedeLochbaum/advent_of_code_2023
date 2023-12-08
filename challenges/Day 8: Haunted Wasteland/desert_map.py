input_path = 'challenges/Day 8: Haunted Wasteland/input'
from functools import reduce
import math

current_pos = []; instructions = None; graph = {}; steps = 0

with open(input_path) as f:
  for line in f:
    if not instructions: instructions = line[:-1]; continue
    if line == '\n': continue
    source, ways = line[:-1].split(' = ')
    left, right = ways[1:-1].split(', ')
    graph[source] = (left, right)
    if source[2] == 'A': current_pos.append(source)

times_to_get_to_goal = []
while(current_pos):
  for dir in instructions:
    steps += 1
    _current_pos = []
    for i in range(len(current_pos)):
      next = graph[current_pos[i]][0] if dir == 'L' else graph[current_pos[i]][1]
      if next[2] == 'Z': times_to_get_to_goal.append(steps)
      else: _current_pos.append(next)
    current_pos = _current_pos

print('Part 2: ', reduce(math.lcm, times_to_get_to_goal))
