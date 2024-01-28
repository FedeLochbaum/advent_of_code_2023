input_path = 'challenges/Day 17: Clumsy Crucible/input0'
from utils import grid_from_file
import copy

RIGHT = (0, 1); LEFT = (0, -1); DOWN = (1, 0); UP = (-1, 0)

left_dir = {
    RIGHT: UP,
    LEFT: DOWN,
    UP: LEFT,
    DOWN: RIGHT
}

right_dir = {
    RIGHT: DOWN,
    LEFT: UP,
    UP: RIGHT,
    DOWN: LEFT
}

graph = grid_from_file(input_path)

rows, cols = len(graph), len(graph[0])
goal = (rows - 1, cols - 1)

move = lambda dir, node: (node[0] + dir[0], node[1] + dir[1])

def turnLeft(dir, node): n_dir = left_dir[dir]; return move(n_dir, node), n_dir
def turnRight(dir, node): n_dir = right_dir[dir]; return move(n_dir, node), n_dir

is_valid = lambda node: node[0] >= 0 and node[0] < rows and node[1] >= 0 and node[1] < cols

def find_min(node, dir, tries, memo, seen):
  if node == goal: return graph[goal[0]][goal[1]]
  
  seen.add(node) ## mark node to seen

  if not node in memo:
    options = [100000000000]
    
    next = move(dir, node)
    left, lDir = turnLeft(dir, node)
    right, rDir = turnRight(dir, node)

    seen_copy = copy.deepcopy(seen)
    
    if tries > 0 and is_valid(next) and not next in seen: options.append(find_min(next, dir, tries - 1, memo, seen) + graph[next[0]][next[1]])

    seen = seen_copy
    if (is_valid(left) and not left in seen): options.append(find_min(left, lDir, 3, memo, seen) + graph[left[0]][left[1]])

    seen = seen_copy
    if (is_valid(right) and not right in seen): options.append(find_min(right, rDir, 3, memo, seen) + graph[right[0]][right[1]])

    # if len(options) == 0: return 100000000000
    memo[node] = min(options)

  return memo[node]

_min = min(find_min((0, 0), RIGHT, 3, {}, set()), find_min((0, 0), DOWN, 3, {}, set()))
print('Part 1:', _min)