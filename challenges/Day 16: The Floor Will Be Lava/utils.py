DIRS = { 'RIGHT': (0, 1), 'LEFT': (0, -1), 'UP': (-1, 0), 'DOWN': (1, 0) }

SPLIT = {
  '|': {
    DIRS['RIGHT']: [ DIRS['UP'], DIRS['DOWN'] ],
    DIRS['LEFT']: [ DIRS['UP'], DIRS['DOWN'] ],
  },
  '-': {
    DIRS['UP']: [ DIRS['RIGHT'], DIRS['LEFT'] ],
    DIRS['DOWN']: [ DIRS['RIGHT'], DIRS['LEFT'] ],
  }
}

MIRRORS = {
  '/': {
    DIRS['RIGHT']: DIRS['UP'],
    DIRS['LEFT']: DIRS['DOWN'],
    DIRS['UP']: DIRS['RIGHT'],
    DIRS['DOWN']: DIRS['LEFT']
  },
  '\\': {
    DIRS['RIGHT']: DIRS['DOWN'],
    DIRS['LEFT']: DIRS['UP'],
    DIRS['UP']: DIRS['LEFT'],
    DIRS['DOWN']: DIRS['RIGHT']
  }
}

def grid_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([elem for elem in line[:-1]])
  return array