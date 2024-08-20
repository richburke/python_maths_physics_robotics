#!/usr/bin/env python3
'''
Integration with Webbots
'''
from collections import defaultdict
import numpy as np
from heapq import heapify, heappush, heappop
from matplotlib import pyplot as plt


LOCATION_WIDTH = 5 # meters
LOCATION_HEIGHT = 6 # meters
PLOT_PIXELS_PER_UNIT = 100 # Here a meter is considered a "unit"
PLOT_SCALE_WIDTH = 0.5
PLOT_SCALE_HEIGHT = 0.5
PLOT_WIDTH = int(LOCATION_WIDTH * PLOT_SCALE_WIDTH * PLOT_PIXELS_PER_UNIT)
PLOT_HEIGHT = int(LOCATION_HEIGHT * PLOT_SCALE_HEIGHT * PLOT_PIXELS_PER_UNIT)
PLOT_LOCATION_OFFSET_X = LOCATION_WIDTH * PLOT_SCALE_WIDTH
PLOT_LOCATION_OFFSET_Y = LOCATION_HEIGHT * PLOT_SCALE_HEIGHT
PLOT_SHIFT_X = 0
PLOT_SHIFT_Y = -1

moves = [(0,1), (0,-1), (-1,0), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]


def is_move_diagonal(move):
  return move in [(-1,-1), (-1,1), (1,-1), (1,1)]

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

    # if (column, row) == (300, 300): # Wormhole
    #     return([(0,(15,15))])

    for move in moves:
        candidate_column = column + move[0]
        candidate_row = row + move[1]
        if not is_valid(candidate_column, candidate_row):
            continue

        cost = 1
        if is_move_diagonal(move):
            cost = 1.4

        neighbors.append((cost, (candidate_column, candidate_row)))
    return neighbors
  return fn


def assign_goal(map):
    goal = (0,0)
    assigned = False
    while not assigned:
        goal = (np.random.randint(len(map)), np.random.randint(len(map[0])))
        if map[goal[0]][goal[1]]:
            continue
        assigned = True
    return goal

def assign_start(map):
  def fn(goal):
    start = (0,0)
    assigned = False
    while not assigned:
        start = (np.random.randint(len(map)), np.random.randint(len(map[0])))
        if start == goal:
            continue
        if map[start[0]][start[1]]:
            continue
        assigned = True
    return start
  return fn
    

def euclidean_distance(a, b):
  return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def map2world(px, py):
    wx = (px / PLOT_PIXELS_PER_UNIT / PLOT_SCALE_WIDTH) - PLOT_LOCATION_OFFSET_X - PLOT_SHIFT_X
    wy = -(py / PLOT_PIXELS_PER_UNIT / PLOT_SCALE_HEIGHT) + PLOT_LOCATION_OFFSET_Y + PLOT_SHIFT_Y

    # Add offset; factor for plot's pixels. 
    # px = np.floor((xw + PLOT_LOCATION_OFFSET_X + PLOT_SHIFT_X) * PLOT_SCALE_WIDTH * PLOT_PIXELS_PER_UNIT)
    # # Add offset; shift Y up for more centered display; factor for plot's pixels. 
    # py = np.floor((-yw + PLOT_LOCATION_OFFSET_Y + PLOT_SHIFT_Y) * PLOT_SCALE_HEIGHT * PLOT_PIXELS_PER_UNIT)
    # px = min(px, PLOT_WIDTH - 1) # Pixels are 0-indexed
    # py = min(py, PLOT_HEIGHT - 1) # Pixels are 0-indexed
    # px = max(px, 0)
    # py = max(py, 0)
    
    return [wx, wy]
    # return [int(px), int(py)]

rows = 20
cols = 30
# map = np.random.rand(rows, cols) < 0.1
map = np.load('cspace.npy')

goal = (145, 140)
# goal = assign_goal(map)
start = (145, 100)
# start = assign_start(map)(goal)

plt.ion() # turns 'interactive mode' on
plt.plot(goal[1], goal[0],'r*') # puts a yellow asterisk at the goal
plt.plot(start[1], start[0],'b*') # puts a yellow x at the start
plt.imshow(map)

queue = [(0, start)]
heapify(queue)
distances = defaultdict(lambda: float('inf'))
distances[start] = 0
visited = set(start)
parent = {}

while queue:
    distance, current = heappop(queue)
    if current == goal:
        break
    visited.add(current)

    plt.plot(current[1], current[0],'b.')    
    plt.show()
    plt.pause(0.000001)

    for (cost, neighbor) in get_neighbors(map)(current[0], current[1]):
        if neighbor in visited:
            continue

        candidate_distance = distance + cost
        if candidate_distance < distances[neighbor]:
            distances[neighbor] = candidate_distance
            heuristic_distance = candidate_distance + euclidean_distance(neighbor, goal)
            heappush(queue, (heuristic_distance, neighbor))
            parent[neighbor] = current


path = []
key = goal
while key in parent.keys():
    key = parent[key]
    path.insert(0, key)
    if key == start:
        break
path.append(goal)

plt.ioff()
for p in path:    
     plt.plot(p[1], p[0],'r*')

plt.show()
