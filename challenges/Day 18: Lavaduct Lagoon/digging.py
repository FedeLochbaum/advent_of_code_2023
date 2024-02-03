input_path = 'challenges/Day 18: Lavaduct Lagoon/input'

RIGHT = (0, 1); LEFT = (0, -1); DOWN = (1, 0); UP = (-1, 0)

DIR = { 'R': RIGHT, 'L': LEFT, 'U': UP, 'D': DOWN }

HEX_DIR = { '0': 'R', '1': 'D', '2': 'L', '3': 'U' }

pos1, pos2 = (0, 0), (0, 0)
boundary1, boundary2 = [pos1], [pos2]
perimeter1, perimeter2 = 0, 0

with open(input_path) as f:
  for line in f.readlines():
    _dir, times, colour = line.strip().split()

    dir = DIR[_dir]
    delta = (dir[0] * int(times), dir[1] * int(times))
    pos1 = (pos1[0] + delta[0], pos1[1] + delta[1])
    boundary1.append(pos1)
    perimeter1 += int(times)

    hex_code = colour[2:-1]
    times2 = int(hex_code[:5], base=16)
    _dir2 = HEX_DIR[hex_code[-1]]
    dir2 = DIR[_dir2]
    delta = (dir2[0] * times2, dir2[1] * times2)
    pos2 = (pos2[0] + delta[0], pos2[1] + delta[1])
    boundary2.append(pos2)
    perimeter2 += times2

def shoelace(boundary):
  det = 0
  for i in range(len(boundary) - 1):
    p1, p2 = boundary[i], boundary[i + 1]
    det += (p1[0] * p2[1] - p2[0] * p1[1])

  return abs(det // 2)

print('Part 1:', shoelace(boundary1) + perimeter1 // 2 + 1)
print('Part 2: ', shoelace(boundary2) + perimeter2 // 2 + 1)