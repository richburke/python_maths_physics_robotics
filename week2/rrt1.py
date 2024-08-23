#!/usr/bin/env python3
'''
Rapidly Exploring Random Trees (RRT)
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


def get_edges(graph):
  def fn(column, row):
    return graph[(column, row)]
  return fn


def euclidean_distance(a, b):
  return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def step_from_to(start):
  def fn(goal):
    def gn(step):
      hyp = euclidean_distance(start, goal)
      opp = abs(goal[0] - start[0])
      theta = np.arcsin(opp/hyp)
      sign_x = -1 if goal[1] < start[1] else 1
      sign_y = -1 if goal[0] < start[0] else 1
      return (start[0] + sign_y * Dq * np.sin(theta), start[1] + sign_x * Dq * np.cos(theta))
    return gn
  return fn

pixel_columns = 300
pixel_rows = 200

map = np.ones((pixel_rows, pixel_columns)) * 255
start = (100, 150)
# goal = (180, 10)
# goal = (10, 10)
# goal = (10, 220)
# goal = (180, 220)
goal = (np.random.randint(0, pixel_rows), np.random.randint(0, pixel_columns))
graph = { start: [] }
q_near = start
K = 3000
k = 0
Dq = 20
goal_direction_probability = 0.01

plt.ion() # turns 'interactive mode' on
plt.plot(goal[1], goal[0],'y*') # puts a yellow asterisk at the goal
plt.plot(start[1], start[0],'g*') # puts a yellow x at the start
plt.imshow(map)

initial = True
while k < K and q_near != goal:
  # A random configuration in C
  if initial or np.random.rand() < goal_direction_probability:
    q_rand = goal
  else:
    q_rand = (np.random.randint(0, pixel_rows), np.random.randint(0, pixel_columns))
  initial = False

  # The nearest vertex to qrand that is already in G
  distances = []
  heapify(distances)
  for node in graph.keys():
      heappush(distances, (euclidean_distance(node, q_rand), node))
  q_near = heappop(distances)[1]

  # Compute a new configuration by moving Δq from qnear into the direction of 
  # qrand or use qrand if closer to qnear than Δq
  q_new = q_rand
  if euclidean_distance(q_near, q_rand) > Dq:
    q_new = step_from_to(q_near)(q_rand)(Dq)
    print(q_near, q_rand, q_new)
    # If off the map, try a different random value.
    if q_new[0] < 0 or q_new[0] >= pixel_rows or q_new[1] < 0 or q_new[1] >= pixel_columns:
      continue

  # If qnew is less than Δq from qgoal, qnew = qgoal.
  if euclidean_distance(q_new, goal) < Dq:
    q_new = goal

  # Add an edge between qnear and qnew.
  distance_q_new_q_near = euclidean_distance(q_new, q_near)
  graph[q_near].append((distance_q_new_q_near, q_new))
  graph[q_new] = [(distance_q_new_q_near, q_near)]
  k += 1

  if q_new != goal:
    plt.plot(q_new[1], q_new[0],'b.') 
  plt.show()
  plt.pause(0.000001)

queue = [(0, start)]
heapify(queue)
distances = defaultdict(lambda: float('inf'))
distances[start] = 0
visited = set(start)
parent = {start: None}

while queue:
    distance, current = heappop(queue)
    if current == goal:
        break
    visited.add(current)

    plt.plot(current[1], current[0], 'y.')    
    plt.show()
    plt.pause(0.000001)

    for (cost, neighbor) in get_edges(graph)(current[0], current[1]):
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
while key != start:
    key = parent[key]
    path.insert(0, key)
path.append(goal)

prev = None
# print("path", prev)
plt.ioff()
for p in path:
  if prev:
    plt.plot([p[1], prev[1]], [p[0], prev[0]],'ro-', linewidth=2, markersize=3)
  # print("path", p)
  prev = p

plt.show()
