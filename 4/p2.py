from typing import List, Tuple

type LayoutBoard = List[List[str]]
type NeighborBoard = List[List[List[Tuple[int, int]]]]

PAPER_ROLL = '@'
EMPTY_CELL = '.'
QUAL_VAL = 4

def add_neighbors(board: NeighborBoard, row_idx: int, col_idx: int) -> None:
  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
      if (i, j) != (0, 0) and 0 <= (row_idx + i) < len(board) \
                          and 0 <= (col_idx + j) < len(board[0]):
        board[row_idx+i][col_idx+j].append((row_idx, col_idx))

def create_neighbor_board(board: LayoutBoard) -> NeighborBoard:
  neighbor_board = [[[] for _ in range(len(board[0]))] for _ in range(len(board))]
  
  for row_idx in range(len(board)):
    for col_idx in range(len(board)):
      if board[row_idx][col_idx] == PAPER_ROLL:
        add_neighbors(neighbor_board, row_idx, col_idx)

  return neighbor_board

def itterate_board(board: LayoutBoard, neighbor_board: NeighborBoard) -> Tuple[int, LayoutBoard]:
  removed_cnt = 0
  new_board = []

  for row_idx in range(len(neighbor_board)):
    new_row = []
    for col_idx in range(len(neighbor_board)):
      if board[row_idx][col_idx] == EMPTY_CELL:
        new_row.append(EMPTY_CELL)
      else:
        if len(neighbor_board[row_idx][col_idx]) < QUAL_VAL:
          removed_cnt += 1
          new_row.append(EMPTY_CELL)
        else:
          new_row.append(PAPER_ROLL)
    new_board.append(new_row)
  
  return (removed_cnt, new_board)

def main():
  with open("input.txt") as f:
    full_board: LayoutBoard = []
    for line in f.readlines():
      full_board.append([cell for cell in line])

    neighbor_board = create_neighbor_board(full_board)
    
    fnl_cnt = 0

    (removed_cnt, full_board) = itterate_board(full_board, neighbor_board)
    while removed_cnt > 0:
      neighbor_board = create_neighbor_board(full_board)
      fnl_cnt += removed_cnt
      (removed_cnt, full_board) = itterate_board(full_board, neighbor_board)

  print(fnl_cnt)

if __name__ == '__main__':
  main()