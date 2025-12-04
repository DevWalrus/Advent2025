STR_LEN = 12

def max_for_bank(bank):
  bank_ints = [int(x) for x in bank.strip()]
  bank_len = len(bank_ints)

  val = 0

  min_pos = 0
  for i in range(STR_LEN - 1, -1, -1):
    dig = max(bank_ints[min_pos:bank_len-i])
    min_pos = bank_ints[min_pos:].index(dig)+1+min_pos
    val += dig * (10 ** i)
  return val
  

with open("input.txt") as f:
  total_sum = 0
  for line in f.readlines():
    total_sum += max_for_bank(line)
  print(total_sum)