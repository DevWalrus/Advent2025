import math
from typing import List

EMPTY_CELL = '.'
START_CELL = 'S'
SPLIT_CELL = '^'
BEAM_CELL =  '|'

def print_board(board: List[List[str]]):
  print('┏', '━'*len(board[0]), '┓', sep='')
  for row in board:
    print('┃', end='')
    for cell in row:
      print(cell, end='')
    print('┃')
  print('┗', '━'*len(board[0]), '┛', sep='')

def set_cell(board, row, col, value):
  if 0 <= row < len(board) and 0 <= col < len(board[0]):
    board[row][col] = value

def main():
  board = []
  with open("sample.txt") as f:
    lines = f.readlines()
    for line in lines:
      board.append([cell for cell in line.strip()])

  print()
  print_board(board)

  split_cnt = 0
  
  for row_idx in range(1, len(board)):
    for col_idx in range(len(board[0])):
      if board[row_idx][col_idx] == BEAM_CELL:
        continue # A prior split already set this, move on
      elif board[row_idx][col_idx] == EMPTY_CELL:
        if board[row_idx-1][col_idx] == START_CELL:
          set_cell(board, row_idx, col_idx, BEAM_CELL)
        elif board[row_idx-1][col_idx] == BEAM_CELL:
          set_cell(board, row_idx, col_idx, BEAM_CELL)
        elif board[row_idx-1][col_idx] == SPLIT_CELL:
          set_cell(board, row_idx, col_idx, EMPTY_CELL)
        elif board[row_idx-1][col_idx] == EMPTY_CELL:
          set_cell(board, row_idx, col_idx, EMPTY_CELL)
      elif board[row_idx][col_idx] == SPLIT_CELL:
        if board[row_idx-1][col_idx] == START_CELL:
          set_cell(board, row_idx, col_idx - 1, BEAM_CELL)
          set_cell(board, row_idx, col_idx + 1, BEAM_CELL)
        elif board[row_idx-1][col_idx] == BEAM_CELL:
          split_cnt += 1
          set_cell(board, row_idx, col_idx - 1, BEAM_CELL)
          set_cell(board, row_idx, col_idx + 1, BEAM_CELL)
        elif board[row_idx-1][col_idx] == SPLIT_CELL:
          set_cell(board, row_idx, col_idx, EMPTY_CELL)
        elif board[row_idx-1][col_idx] == EMPTY_CELL:
          set_cell(board, row_idx, col_idx, EMPTY_CELL)
  
  print_board(board)
  print(split_cnt)

if __name__ == '__main__':
  main()