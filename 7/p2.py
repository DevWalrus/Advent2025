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

def set_cell(board, c_board, row, col, value):
  if 0 <= row < len(board) and 0 <= col < len(board[0]):
    if type(value) == str:
      board[row][col] = value
    if type(value) == int:
      board[row][col] = BEAM_CELL
      c_board[row][col] += value

def main():
  board = []
  c_board = []
  with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
      board.append([cell for cell in line.strip()])
      c_board.append([(cell if cell != EMPTY_CELL else 0) for cell in line.strip()])

  print_board(board)
  
  for row_idx in range(1, len(board)):
    for col_idx in range(len(board[0])):
      if board[row_idx][col_idx] == BEAM_CELL:
          set_cell(board, c_board, row_idx, col_idx, c_board[row_idx-1][col_idx])
      elif board[row_idx][col_idx] == EMPTY_CELL:
        if board[row_idx-1][col_idx] == START_CELL:
          set_cell(board, c_board, row_idx, col_idx, 1)
        elif board[row_idx-1][col_idx] == BEAM_CELL:
          set_cell(board, c_board, row_idx, col_idx, c_board[row_idx-1][col_idx])
        elif board[row_idx-1][col_idx] == SPLIT_CELL:
          set_cell(board, c_board, row_idx, col_idx, EMPTY_CELL)
        elif board[row_idx-1][col_idx] == EMPTY_CELL:
          set_cell(board, c_board, row_idx, col_idx, EMPTY_CELL)
      elif board[row_idx][col_idx] == SPLIT_CELL:
        if board[row_idx-1][col_idx] == START_CELL:
          set_cell(board, c_board, row_idx, col_idx - 1, 1)
          set_cell(board, c_board, row_idx, col_idx + 1, 1)
        elif board[row_idx-1][col_idx] == BEAM_CELL:
          set_cell(board, c_board, row_idx, col_idx - 1, c_board[row_idx-1][col_idx])
          set_cell(board, c_board, row_idx, col_idx + 1, c_board[row_idx-1][col_idx])
        elif board[row_idx-1][col_idx] == SPLIT_CELL:
          set_cell(board, c_board, row_idx, col_idx, EMPTY_CELL)
        elif board[row_idx-1][col_idx] == EMPTY_CELL:
          set_cell(board, c_board, row_idx, col_idx, EMPTY_CELL)
  
  
  print_board(board)
  print_board(c_board)
  print(sum(c_board[-1]))

if __name__ == '__main__':
  main()