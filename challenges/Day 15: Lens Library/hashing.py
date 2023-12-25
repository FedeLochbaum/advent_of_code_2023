input_path = 'challenges/Day 15: Lens Library/input'
from functools import reduce

hash = lambda _str: reduce(lambda h, c: ((h + ord(c)) * 17) % 256, _str, 0)

sum = 0

f = open(input_path)
line = f.readline()[:-1]
for cmd in line.split(','):
  # var, num = cmd.split('=')
  sum += hash(cmd)
  # print('hash(HASH)', hash(cmd))

print('Part 1: ', sum)