input_path = 'challenges/Day 4: Scratchcards/input'

sum = 0

with open(input_path) as f:
  for line in f:
    winning_d = {}
    card_i, nums = line[:-1].split(': ')
    winning, having = nums.split(' | ')
    for winning_num in winning.split(' '): winning_d[winning_num] = False
    
    winners = 0
    for n in having.split(' '):
      if n in winning_d and (not winning_d[n]): winning_d[n] = True; winners += 1
    
    sum += pow(2, winners - 1) if winners > 0 else 0
    
  print('Part 1: ', sum)

