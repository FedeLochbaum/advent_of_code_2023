input_path = 'challenges/Day 6: Wait For It/input'

ways = 1
f = open(input_path)
line1 = f.readline()[10:-1]; line2 = f.readline()[10:-1]
time = list(map(int, line1.split('  ')))
distance = list(map(int, line2.split('  ')))

def ways_to_win(race_time, race_dist):
  ways = 0
  for t in range(1, race_time):
    if t * (race_time - t) > race_dist: ways += 1
  return ways

for i in range(len(time)):
  ways *= ways_to_win(time[i], distance[i])

print('Part 1: ', ways)

# Part 2
time = int(line1.replace(' ', ''))
distance = int(line2.replace(' ', ''))
print('Part 2: ', ways_to_win(time, distance))
