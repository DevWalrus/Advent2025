STARTING_VAL = 50
COUNT_VAL = 0

ADD_PREFIX = "R"
SUB_PREFIX = "L"

current_val = STARTING_VAL

hits = 0

with open("sample.txt") as f:
  for line in f.readlines():
    if line.startswith(ADD_PREFIX):
      current_val = (current_val + int(line[1:])) % 100
    if line.startswith(SUB_PREFIX):
      current_val = (current_val - int(line[1:])) % 100
    if current_val == 0:
      hits += 1
print(hits)