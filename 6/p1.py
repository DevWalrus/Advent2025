import math
from typing import List


def main():
  operands = []
  with open("input.txt") as f:
    value_mode = False
    lines = f.readlines()
    for line_num in range(len(lines)):
      line = lines[line_num]
      if line[0] != '*' and line[0] != '+':
        line = [int(x) for x in line.strip().split(' ') if x != '']
        if len(operands) == 0:
          operands = [[] for _ in range(len(line))]
        for operand_idx in range(len(line)):
          operands[operand_idx].append(line[operand_idx])
    
    total_sum = 0
    operators = [x for x in lines[-1].strip().split(' ') if x != '']
    for func_idx in range(len(operands)):
      if operators[func_idx] == '*':
        total_sum += math.prod(operands[func_idx])
      elif operators[func_idx] == '+':
        total_sum += sum(operands[func_idx])
      
    print(total_sum)

if __name__ == '__main__':
  main()