#!/usr/bin/env python3

move_threshold = 0.3

map = [[0,0,0],
       [0.9,0.8,0],
       [0,0.4,0]]

moves = [(0,1), (0,-1), (-1,0), (1,0)]

graph = {(0,0) : [(0,1)],
         (0,1) : [(0,0),(0,2)],
         (0,2) : [(0,1),(1,2)],
         (1,2) : [(0,2),(2,2)],
         (2,0) : [(2,1)],
         (2,1) : [(2,0),(2,2)],
         (2,2) : [(2,1),(1,2)]}

def is_neighbor_valid(map):
  def fn(column, row):
    if column < 0 or column >= len(map):
      return False
    if row < 0 or row >= len(map[0]):
      return False
    if map[column][row] > move_threshold:
      return False
    return True
  return fn

def get_neighbors(map):
  is_valid = is_neighbor_valid(map)
  def fn(column, row):
    neighbors = []
    for move in moves:
        candidate_column = column + move[0]
        candidate_row = row + move[1]
        if is_valid(candidate_column, candidate_row):
            neighbors.append((candidate_column, candidate_row))
    return neighbors
  return fn

print(get_neighbors(map)(2, 0))

