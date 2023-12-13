input_path = 'challenges/Day 10: Pipe Maze/input'
from utils import graph_from_file, grid_from_file, neighbors_by_key
from collections import deque

rows, cols, graph, S = graph_from_file(input_path)
grid = grid_from_file(input_path)

def are_connected(nexts, me):
  for point in nexts:
    if not point in graph or (me != graph[point][0] and me != graph[point][1]): return False

  return True 

def farthest_point_with_bfs(initial):
  queue = deque([(initial, 0)])
  visited = set()
  max_distance = 0

  while queue:
    current, distance = queue.popleft()
    visited.add(current)
    max_distance = max(max_distance, distance)

    for ri, ci in graph[current]:
      if (ri, ci) not in graph: continue
      if (ri, ci) in visited: continue
      queue.append(((ri, ci), distance + 1))

  return max_distance, visited

def is_inside(pos, loop):
  crosses = 0
  for j in range(pos[1] + 1, cols + 1):
    new_pos = (pos[0], j)
    last_pos = (pos[0], j-1)
    if new_pos in loop and last_pos in loop and new_pos in graph[last_pos]: continue
    if last_pos in loop:
      exited = last_pos
      edge_up = False
      edge_down = False
      for r, c in [entered, exited]:
        if (r-1, c) in graph[(r, c)]: edge_up = True
        if (r+1, c) in graph[(r, c)]: edge_down = True
      if edge_up and edge_down: crosses += 1
    if new_pos in loop: entered = new_pos
  return (crosses % 2) == 1

for move in neighbors_by_key.keys():
  nexts = neighbors_by_key[move](S[0], S[1])
  if are_connected(nexts, S):
    graph[S] = nexts
    distance, cycle = farthest_point_with_bfs(S); total = 0
    print('Part 1: ', distance)
    for r in range(len(grid)):
      for c in range(len(grid[r])):
        if (r, c) in cycle: continue
        total += is_inside((r, c), cycle)
    print('Part 2: ', total)
