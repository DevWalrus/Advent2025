from typing import List, Tuple

def add_neighbors(board: List[List[List[Tuple[int, int]]]], row_idx, col_idx):
  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
      if (i, j) == (0, 0) or (len(board) <= row_idx+i) or (row_idx+i < 0) \
                          or (len(board[0]) <= col_idx+j) or (col_idx+j < 0):
        continue
      board[row_idx+i][col_idx+j].append((row_idx, col_idx))

def create_neighbor_board(board: List[List[List[Tuple[int, int]]]]):
  neighbor_board = [[[] for _ in range(len(full_board[0]))] for _ in range(len(board))]
  
  for row_idx in range(len(board)):
    for col_idx in range(len(board)):
      if board[row_idx][col_idx] == '@':
        add_neighbors(neighbor_board, row_idx, col_idx)

  return neighbor_board
  
QUAL_VAL = 4

with open("input.txt") as f:
  full_board = []
  for line in f.readlines():
    full_board.append([cell for cell in line])

  neighbor_board = [[[] for _ in range(len(full_board[0]))] for _ in range(len(full_board))]
  
  for row_idx in range(len(full_board)):
    for col_idx in range(len(full_board)):
      if full_board[row_idx][col_idx] == '.':
        continue
      neighbors = add_neighbors(neighbor_board, row_idx, col_idx)
  
  fnl_cnt = 0

  for row_idx in range(len(neighbor_board)):
    for col_idx in range(len(neighbor_board)):
      if full_board[row_idx][col_idx] == '.':
        print('.', end='')
      else:
        if len(neighbor_board[row_idx][col_idx]) < QUAL_VAL:
          fnl_cnt += 1
        print(len(neighbor_board[row_idx][col_idx]), end='')
    print()
  print(fnl_cnt)