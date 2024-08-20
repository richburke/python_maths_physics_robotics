#!/usr/bin/env python3
'''
BFS
'''
import numpy as np
from matplotlib import pyplot as plt


moves = [(0,1), (0,-1), (-1,0), (1,0)]


def is_location_valid(location_value):
  return not location_value

def is_neighbor_valid(map):
  def fn(column, row):
    if column < 0 or column >= len(map):
      return False
    if row < 0 or row >= len(map[0]):
      return False
    if not is_location_valid(map[column][row]):
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


rows = 20
cols = 30
map = np.random.rand(rows, cols) < 0.1

goal = (0,0)
assigned = False
while not assigned:
    goal = (np.random.randint(rows), np.random.randint(cols))
    if map[goal]:
        continue
    assigned = True

start = (0,0)
assigned = False
while not assigned:
    start = (np.random.randint(rows), np.random.randint(cols))
    if map[start]:
        continue
    if start == goal:
        continue
    assigned = True


plt.ion() # turns 'interactive mode' on
plt.plot(goal[1], goal[0],'y*') # puts a yellow asterisk at the goal
plt.plot(start[1], start[0],'yx') # puts a yellow asterisk at the goal
plt.imshow(map)

queue = [start]
visited = set(start)
parent = {}

while queue:
    current = queue.pop(0)
    if current == goal:
        break

    plt.plot(current[1], current[0],'b.')    
    plt.show()
    plt.pause(0.000001)

    for neighbor in get_neighbors(map)(current[0], current[1]):
        if neighbor in visited:
            continue
        queue.append(neighbor)
        visited.add(neighbor)
        parent[neighbor] = current

# print(map)

path = []
key = goal
while key in parent.keys():
    key = parent[key]
    path.insert(0, key)
    if key == start:
        break
path.append(goal)

print(path)

plt.ioff()
for p in path:    
     plt.plot(p[1], p[0],'r*')

plt.show()
