input_path = 'challenges/Day 10: Pipe Maze/input'
from utils import graph_from_file, neighbors_by_key
from collections import deque

rows, cols, graph, S = graph_from_file(input_path)

def are_connected(nexts, me):
  for point in nexts:
    if not point in graph: return False
    first, second = graph[point]
    if me != first and me != second:
      return False
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

  return max_distance

_max = 0
for move in neighbors_by_key.keys():
  nexts = neighbors_by_key[move](S[0], S[1])
  if are_connected(nexts, S):
    graph[S] = nexts
    print('farthest_point_with_bfs(S): ', farthest_point_with_bfs(S))
    _max = max(_max, farthest_point_with_bfs(S))

print('Part 1: ', _max)