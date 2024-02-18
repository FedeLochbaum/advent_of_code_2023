import functools
input_path = 'challenges/Day 19: Aplenty/input'

# To start, each part is rated in each of four categories:
  # x: Extremely cool looking
  # m: Musical (it makes a noise when you hit it)
  # a: Aerodynamic
  # s: Shiny

# Each workflow has a name and contains a list of rules;

# Each rule specifies a condition and where to send the part if the condition is true
# The last rule in each workflow has no condition and always applies if reached

accepted_workflow = 'A'
rejected_workflow = 'R'
end_workflows = [ accepted_workflow, rejected_workflow ]

total_sum = 0

def next_workflow(part, workflow):
  for rule in workflow[0]:
    cond, dest = rule
    part_value = part[cond[0]]
    if eval(cond.replace(cond[0], str(part_value))): return dest

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
  workflows = {}
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


