input_path = 'challenges/Day 5: If You Give A Seed A Fertilizer/input'

lower_location_nummber = float('inf'); i = 0

def there_intersection(r1, r2): return not (r2[0] > r1[1] or r2[1] < r1[0])

def intersection(r1, r2):
  i, e = max(r1[0], r2[0]), min(r1[1], r2[1])
  limits = []
  if i > r1[0]: limits.append((r1[0], i))
  if e < r1[1]: limits.append((e, r1[1]))

  return (i + r2[2], e + r2[2]), limits

def map_source(_map, source_range):
  
  for map_range in _map:
    if source_range[0] == map_range[1] or source_range[1] == map_range[0]: continue
    if there_intersection(source_range, map_range):
      inter, limits = intersection(source_range, map_range)
      res = [inter]
      for limit in limits: res += map_source(_map, limit)
      return res

  return [source_range]

def min_range_value(sources):
  _min = float('inf')
  for init, _ in sources:
    _min = min(_min, init)

  return _min

with open(input_path) as f:
  sources = None; is_mapping = False; _map = []; destination = None
  for line in f:
    if sources == None:
      sources = []
      _, seeds = line[:-1].split('seeds: ')
      seeds = list(map(int, seeds.split(' ')))
      for i in range(len(seeds)):
        if i % 2 == 0: sources.append((seeds[i], seeds[i] + seeds[i + 1]))
      continue
    
    if line == '\n':
      is_mapping = False;
      _sources = []
      for source in sources:
        res = map_source(_map, source) 
        _sources += res
      sources = _sources;
      _map = []

      if destination == 'location': lower_location_nummber = min_range_value(sources)
      continue
    
    if not is_mapping: _, destination = line[:-6].split('-to-'); is_mapping = True; continue

    if is_mapping:
      dest, origin, delta = list(map(int, line[:-1].split(' ')))
      _map.append((origin, origin + delta, dest - origin))

print('Part 2: ', lower_location_nummber)