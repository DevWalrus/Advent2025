STARTING_VAL = 50
COUNT_VAL = 0

ADD_PREFIX = "R"
SUB_PREFIX = "L"

current_val = STARTING_VAL

hits = 0

with open("input.txt") as f:
  for line in f.readlines():
    modifier = int(line[1:])
    this_hits = (modifier // 100)
    if line.startswith(ADD_PREFIX):
      new_val = current_val + (modifier % 100)
    if line.startswith(SUB_PREFIX):
      new_val = current_val - (modifier % 100)

    if not (0 < new_val <= 99) and current_val != 0:
      this_hits += 1

    current_val = new_val % 100

    print("NEW:", new_val, "" if (this_hits <= 0) else f"[HIT x{this_hits}]", f"=> {current_val}")

    hits += this_hits
print("PASSWORD:", hits)