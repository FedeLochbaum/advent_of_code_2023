input_path = 'challenges/Day 17: Clumsy Crucible/input0'
from utils import grid_from_file
import copy

RIGHT = (0, 1); LEFT = (0, -1); DOWN = (1, 0); UP = (-1, 0)

left_dir = { RIGHT: UP, LEFT: DOWN, UP: LEFT, DOWN: RIGHT }
right_dir = { RIGHT: DOWN, LEFT: UP, UP: RIGHT, DOWN: LEFT }

graph = grid_from_file(input_path)

rows, cols = len(graph), len(graph[0])
goal = (rows - 1, cols - 1)

move = lambda dir, node: (node[0] + dir[0], node[1] + dir[1])

turnLeft = lambda dir, node: [move(left_dir[dir], node), left_dir[dir]]
turnRight = lambda dir, node: [move(right_dir[dir], node), right_dir[dir]]

is_valid = lambda node: node[0] >= 0 and node[0] < rows and node[1] >= 0 and node[1] < cols

too_big = 100000000000

def find_min(node, dir, tries, memo, seen):
  key = (node, tries)

  if node == goal: return 0
  if not is_valid(node): return too_big
  
  seen.add(node) ## mark node to seen

  if not key in memo:
    next = move(dir, node)
    left, lDir = turnLeft(dir, node)
    right, rDir = turnRight(dir, node)

    local_min = too_big

    _seen1 = copy.deepcopy(seen)
    _seen2 = copy.deepcopy(seen)

    if not left in seen: local_min = min(local_min, find_min(left, lDir, 3, memo, seen))
    if tries > 0 and not next in seen: local_min = min(local_min, find_min(next, dir, tries - 1, memo, _seen1))
    if not right in seen: local_min = min(local_min, find_min(right, rDir, 3, memo, _seen2))

    memo[key] = local_min + graph[node[0]][node[1]]

  return memo[key]

print('Part 1:', find_min((0, 0), RIGHT, 3, {}, set()))