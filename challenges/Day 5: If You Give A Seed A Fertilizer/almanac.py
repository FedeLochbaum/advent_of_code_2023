input_path = 'challenges/Day 5: If You Give A Seed A Fertilizer/input'

# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.
lower_location_nummber = float('inf')
i = 0

def map_source(_map, s):
  for dest, _s, range in _map:
    if s >= _s and s <= _s + range:
      return s + (dest - _s)

  return s
with open(input_path) as f:
  sources = None; is_mapping = False; _map = []; destination = None
  for line in f:
    if sources == None:
      _, seeds = line[:-1].split('seeds: ')
      sources = list(map(int, seeds.split(' ')))
      continue
    
    if line == '\n':
      is_mapping = False;
      sources = list(map(lambda s: map_source(_map, s), sources))
      if destination == 'location': lower_location_nummber = min(sources)
      _map = []
      continue
    
    if not is_mapping: _, destination = line[:-6].split('-to-'); is_mapping = True; continue

    if is_mapping: _map.append(list(map(int, line[:-1].split(' '))))



print('Part 1: ', lower_location_nummber)
