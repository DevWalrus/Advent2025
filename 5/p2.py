def mergeOverlap(arr):
    n = len(arr)

    arr.sort()
    res = []

    # Checking for all possible overlaps
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]

        # Skipping already merged intervals
        if res and res[-1][1] >= end:
            continue

        # Find the end of the merged range
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
        res.append([start, end])
    
    return res

def main():
  ranges = []
  vals = []
  with open("input.txt") as f:
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

  min_ranges = mergeOverlap(ranges)

  tot_fresh = 0

  for range in min_ranges:
     tot_fresh += range[1] - range[0] + 1

  print(ranges, min_ranges)
  print(tot_fresh)

if __name__ == '__main__':
  main()