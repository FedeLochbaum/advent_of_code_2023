input_path = 'challenges/Day 4: Scratchcards/input'

_sum, cards, matches = 0, [], []

with open(input_path) as f:
  for line in f:
    winning_d = {}
    cards.append(1)
    card_i, nums = line[:-1].split(': ')
    winning, having = nums.split(' | ')
    for winning_num in winning.split(' '): winning_d[winning_num] = False
    
    winners = 0
    for n in having.split(' '):
      if n in winning_d and (not winning_d[n]): winning_d[n] = True; winners += 1
    
    _sum += pow(2, winners - 1) if winners > 0 else 0
    matches.append(winners)

for i in range(len(matches)):
  for j in range(i + 1, min(len(matches), i + 1 + matches[i])): cards[j] += cards[i]

print('Part 1: ', _sum)
print('Part 2:', sum(cards))


