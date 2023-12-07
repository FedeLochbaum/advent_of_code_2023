from functools import cmp_to_key
input_path = 'Day 7: Camel Cards/input'

is_five = lambda cluster: 5 in cluster.values()
is_four = lambda cluster: 4 in cluster.values()
full_house = lambda cluster: 3 in cluster.values() and 2 in cluster.values()
three_of_kind = lambda cluster: 3 in cluster.values()
two_pair = lambda cluster: list(cluster.values()).count(2) == 2
one_pair = lambda cluster: list(cluster.values()).count(2) == 1

types = [(is_five, 6000), (is_four, 5000), (full_house, 4000), (three_of_kind, 3000), (two_pair, 2000), (one_pair, 1000)]

def clusterize(hand):
  clusters = {}
  for card in hand:
    if not card in clusters: clusters[card] = 0
    clusters[card] += 1
  return clusters

card_value = {
  'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
  '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
}

def value_of_type(hand):
  for f, val in types:
    if f(clusterize(hand)): return val
  return 0

def hand_value_compare(hand1, hand2):
  for i in range(len(hand1[0])):
    if card_value[hand1[0][i]] == card_value[hand2[0][i]]: continue
    return -1 if card_value[hand1[0][i]] < card_value[hand2[0][i]] else 1

  return 0

def hand_type_compare(hand1, hand2):
  type1, type2 = value_of_type(hand1[0]), value_of_type(hand2[0])
  if type1 == type2: return hand_value_compare(hand1, hand2)

  return -1 if type1 < type2 else 1

sum = 0; hands = []; 
with open(input_path) as f:
  for line in f:
    hands.append(line[:-1].split(' '))

hands = sorted(hands, key = cmp_to_key(hand_type_compare))

for i in range(len(hands)): sum += (i + 1) * int(hands[i][1])

print('Part 1: ', sum)