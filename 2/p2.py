FACTORS = {
  1: [],
  2: [1],
  3: [1],
  4: [1, 2],
  5: [1],
  6: [1, 2, 3],
  7: [1],
  8: [1, 2, 4],
  9: [1, 3],
  10: [1, 2, 5],
  11: [1],
  12: [1, 2, 3, 4, 6],
  13: [1],
  14: [1, 2, 7],
  15: [1, 3, 5],
  16: [1, 2, 4, 8],
  17: [1],
  18: [1, 2, 3, 6, 9],
  19: [1],
  20: [1, 2, 4, 5, 10],
  21: [1, 3, 7],
  22: [1, 2, 11],
  23: [1],
  24: [1, 2, 3, 4, 6, 8, 12],
  25: [1, 5],
  26: [1, 2, 13],
  27: [1, 3, 9],
  28: [1, 2, 4, 7, 14],
  29: [1],
  30: [1, 2, 3, 5, 6, 10, 15],
  31: [1],
  32: [1, 2, 4, 8, 16],
  33: [1, 3, 11],
  34: [1, 2, 17],
  35: [1, 5, 7],
  36: [1, 2, 3, 4, 6, 9, 12, 18],
  37: [1],
  38: [1, 2, 19],
  39: [1, 3, 13],
  40: [1, 2, 4, 5, 8, 10, 20],
  41: [1],
  42: [1, 2, 3, 6, 7, 14, 21],
  43: [1],
  44: [1, 2, 4, 11, 22],
  45: [1, 3, 5, 9, 15],
  46: [1, 2, 23],
  47: [1],
  48: [1, 2, 3, 4, 6, 8, 12, 16, 24],
  49: [1, 7],
  50: [1, 2, 5, 10, 250]
}

def id_checker(id):
  for num_of_parts in FACTORS[len(id)]:
    parts = set([id[i:i+num_of_parts] for i in range(0, len(id), num_of_parts)])
    if len(parts) == 1:
      return True
  return False

def range_checker(bound_one, bound_two):
  invalid_sum = 0
  lower = min(int(bound_one), int(bound_two))
  upper = max(int(bound_one), int(bound_two))
  for id in range(lower, upper + 1):
    if id_checker(str(id)):
      invalid_sum += id
  return invalid_sum

with open("input.txt") as f:
  total_sum = 0
  for line in f.read().split(','):
    [b1, b2] = line.split("-")
    total_sum += range_checker(b1, b2)
  print(total_sum)