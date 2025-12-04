def max_for_bank(bank):
  bank_ints = [int(x) for x in bank.strip()]
  first_dig = max(bank_ints[:-1])
  second_dig = max(bank_ints[bank_ints.index(first_dig)+1:])
  return (first_dig * 10) + second_dig
  

with open("input.txt") as f:
  total_sum = 0
  for line in f.readlines():
    total_sum += max_for_bank(line)
  print(total_sum)