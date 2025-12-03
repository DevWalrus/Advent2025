def id_checker(id):
  id_mid = len(id)//2
  [first_half, second_half] = [id[:id_mid], id[id_mid:]]
  return first_half == second_half

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