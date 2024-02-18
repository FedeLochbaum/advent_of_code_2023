import functools
input_path = 'challenges/Day 19: Aplenty/input'

accepted_workflow = 'A'
rejected_workflow = 'R'
end_workflows = [ accepted_workflow, rejected_workflow ]

total_sum = 0
workflows = {}

def calculate_combinations():
  # Max flow ?
  return 0

def next_workflow(part, workflow):
  for rule in workflow[0]:
    cond, dest = rule
    if eval(cond.replace(cond[0], str(part[cond[0]]))):
      return dest

  return workflow[1]

def is_accepted(part, workflows):
  current = 'in'
  while(not current in end_workflows):
    current = next_workflow(part, workflows[current])

  return current == accepted_workflow

def add_assignment(part, assignment):
  key, val = assignment.split('=')
  part[key] = int(val)
  return part

with open(input_path) as f:
  read_parts = False
  for line in f:
    if line == '\n': read_parts = True; continue

    if read_parts:
      part = functools.reduce(add_assignment, line[1:-2].split(','), {})
      if (is_accepted(part, workflows)): total_sum += sum(part.values())
    else:
      origin, conditions = line[:-2].split('{')
      default = conditions.split(',')[-1]
      workflows[origin] = ([], default) # workflow => (rules, default), rules => [(cond, dest)]

      for cond in conditions.split(',')[:-1]:
        rule, dest = cond.split(':')
        workflows[origin][0].append((rule, dest))

print('Part 1: ', total_sum)
print('Part 2: ', calculate_combinations())
