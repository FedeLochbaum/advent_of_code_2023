input_path = 'challenges/Day 1: Trebuchet/input'

# Part 1
sum = 0
with open(input_path) as f:
  for line in f:
    nums = list(filter(lambda x: x.isdigit(), line[:-1]))
    sum += int(nums[0] + nums[-1])

print('Part 1: ', sum)

# Part 2
sum = 0
digits = {
  'one': '1', 'two': '2', 'three': '3',
  'four': '4', 'five': '5', 'six': '6',
  'seven': '7', 'eight': '8', 'nine': '9'
}

def line_digits(line):
  nums = []
  for i in range(len(line)):
    if line[i].isdigit(): nums.append(line[i]); continue

    for k, v in digits.items():
      if i + len(k) >= len(line): continue
      if k == line[i: i + len(k)]: nums.append(v); continue
  return nums

with open(input_path) as f:
  for line in f:
    nums = line_digits(line)
    sum += int(nums[0] + nums[-1])

print('Part 2: ', sum)
