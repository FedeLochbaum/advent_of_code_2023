input_path = 'challenges/Day 8: Haunted Wasteland/input'

initial = 'AAA'; goal = 'ZZZ'

instructions = None; graph = {}; steps = 0

with open(input_path) as f:
  for line in f:
    if not instructions: instructions = line[:-1]; continue
    if line == '\n': continue
    source, ways = line[:-1].split(' = ')
    left, right = ways[1:-1].split(', ')
    graph[source] = (left, right)

current = initial
while(current != goal):
  for dir in instructions:
    steps += 1
    current = graph[current][0] if dir == 'L' else graph[current][1]
    if current == goal: print('Part 1: ', steps); break

