input_path = 'challenges/Day 15: Lens Library/input'
from functools import reduce

hash = lambda _str: reduce(lambda h, c: ((h + ord(c)) * 17) % 256, _str, 0)

part1, part2, hash_map = 0, 0, [{} for _ in range(256)]

def remove_cmd(cmd):
  label = cmd[:-1]
  box = hash_map[hash(label)]
  if label in box: box.pop(label)

def add_cmd(cmd):
  label, focal_length = cmd.split('=')
  box = hash_map[hash(label)]
  box[label] = int(focal_length)

f = open(input_path)
line = f.readline()[:-1]
for cmd in line.split(','):
  part1 += hash(cmd)
  (remove_cmd if '-' in cmd else add_cmd)(cmd)

for i, box in enumerate(hash_map):
  for j, lens in enumerate(box.items()):
    part2 += ((i+1) * (j+1) * lens[1])

print('Part 1: ', part1)
print('Part 2: ', part2)