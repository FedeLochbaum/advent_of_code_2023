input_path = 'challenges/Day 17: Clumsy Crucible/input0'
from utils import grid_from_file
from queue import PriorityQueue

RIGHT = (0, 1); LEFT = (0, -1); DOWN = (1, 0); UP = (-1, 0)
DIRS = [ RIGHT, LEFT, DOWN, UP ]

left_dir = { RIGHT: UP, LEFT: DOWN, UP: LEFT, DOWN: RIGHT }
right_dir = { RIGHT: DOWN, LEFT: UP, UP: RIGHT, DOWN: LEFT }

graph = grid_from_file(input_path)

rows, cols = len(graph), len(graph[0])
goal = (rows - 1, cols - 1)

move = lambda dir, node: (node[0] + dir[0], node[1] + dir[1])

turnLeft = lambda dir, node: [move(left_dir[dir], node), left_dir[dir]]
turnRight = lambda dir, node: [move(right_dir[dir], node), right_dir[dir]]

is_valid = lambda node: node[0] >= 0 and node[0] < rows and node[1] >= 0 and node[1] < cols

def next(state, min_chain, max_chain):
  pos, dir, chain_length = state
  for delta in DIRS:
    if dir is not None:
      if delta == (-dir[0], -dir[1]): continue
      if delta == dir and chain_length == max_chain: continue
      if delta not in [(-dir[0], -dir[1]), dir] and chain_length < min_chain: continue
    new_pos = pos + delta
    if not (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols): continue
    new_dir = delta
    if new_dir != dir: new_chain_length = 1
    else: new_chain_length = chain_length + 1
    yield new_pos, new_dir, new_chain_length

h = lambda state: abs(state[0][0] - goal[0]) + abs(state[0][1] - goal[1])

def a_star(initial_state, goal, min_chain, max_chain):
  queue = PriorityQueue()
  dist = { initial_state: 0 }
  queue.put((dist[initial_state] + h(initial_state), initial_state))

  while not queue.empty():
    f_dist, current_state = queue.get()
    if current_state[0] == goal and current_state[2] >= min_chain: return dist[current_state]

    if f_dist > dist[current_state] + h(current_state): continue

    for nbr_state in next(current_state, min_chain, max_chain):
      g_dist = dist[current_state] + graph[nbr_state[0][0]][nbr_state[0][1]]

      if nbr_state in dist and dist[nbr_state] <= g_dist: continue
      
      dist[nbr_state] = g_dist
      queue.put((dist[nbr_state] + h(nbr_state), nbr_state))

print('Part 1:', a_star(((0, 0), None, 1), goal, 0, 3))
print('Part 2:', a_star(((0, 0), None, 1), goal, 4, 10))