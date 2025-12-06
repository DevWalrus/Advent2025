def main():
  ranges = []
  vals = []
  with open("sample.txt") as f:
    value_mode = False
    for line in f.readlines():
      if line.strip() == '':
        value_mode = True
        continue
      if value_mode:
        val = int(line.strip())
        vals.append(val)
      else:
        c_range = tuple([int(val) for val in line.strip().split('-')])
        ranges.append(c_range)

  fresh_cnt = 0

  for val in vals:
    for range in ranges:
      if range[0] <= val <= range[1]:
        fresh_cnt += 1
        break
  print(fresh_cnt)

if __name__ == '__main__':
  main()