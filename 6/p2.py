import math
from typing import List

def create_operands(rows: List[str], num_funcs: int):
  operands = [[] for _ in range(num_funcs)]
  func_idx = num_funcs - 1

  for idx in range(len(rows[0]) - 1, -1, -1):
    if all([x[idx] == ' ' for x in rows]):
      func_idx -= 1
      continue

    num = ''
    for row in rows:  
      num = num + row[idx]
    operands[func_idx].append(int(num))
  
  return operands

def main():
  op_rows = []
  with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
      if line[0] != '*' and line[0] != '+':
        op_rows.append(line.replace('\n', ''))

  total_sum = 0
  operators = [x for x in lines[-1].strip().split(' ') if x != '']
  operands = create_operands(op_rows, len(operators))

  for func_idx in range(len(operands)):
    if operators[func_idx] == '*':
      total_sum += math.prod(operands[func_idx])
    elif operators[func_idx] == '+':
      total_sum += sum(operands[func_idx])
    
  print(total_sum)

if __name__ == '__main__':
  main()