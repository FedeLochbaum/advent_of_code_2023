input_path = 'Day 7: Camel Cards/input0'

is_five = lambda cluster: 5 in cluster.values()
is_four = lambda cluster: 4 in cluster.values()
full_house = lambda cluster: 3 in cluster.values() and 2 in cluster.values()
three_of_kind = lambda cluster: 3 in cluster.values()
two_pair = lambda cluster: list(cluster.values()).count(2) == 2
one_pair = lambda cluster: list(cluster.values()).count(2) == 1

types = [(is_five, 86000), (is_four, 75000), (full_house, 640000), (three_of_kind, 530000), (two_pair, 420000), (one_pair, 310000)]

def clusterize(hand):
  clusters = {}
  for card in hand:
    if not card in clusters: clusters[card] = 0
    clusters[card] += 1
  return clusters

card_value = {
  'A': 500, 'K': 400, 'Q': 300, 'J': 200, 'T': 100, '9': 9,
  '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
}

def value_of_hand(hand):
  value = 0
  for i in range(len(hand)):
    value += card_value[hand[i]] + pow(2, len(hand) - i)
  return value

def value_of_type(hand):
  for f, val in types:
    if f(clusterize(hand)): return val
  return 0

def  poker_points(hand):
  type_value = value_of_type(hand[0]) + value_of_hand(hand[0])
  return type_value

sum = 0; hands = []; 
with open(input_path) as f:
  for line in f:
    hands.append(line[:-1].split(' '))

hands = sorted(hands, key =  poker_points)

for i in range(len(hands)):
  sum += (i + 1) * int(hands[i][1])

print('Part 1: ', sum)