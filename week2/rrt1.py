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


def get_neighbors(graph):
  def fn(column, row):
    return graph[(column, row)]
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


def step_from_to(a):
  def fn(b):
    def gn(step):
      hyp = euclidean_distance(a, b)
      opp = b[1] - a[1]
      theta = np.arccos(opp/hyp)
      return (int(a[0] + Dq * np.sin(theta)), int(a[1] + Dq * np.cos(theta)))
    return gn
  return fn


map = np.ones((200, 300)) * 255
start = (100, 150)
goal = (np.random.randint(0, len(map)), np.random.randint(0, len(map[0])))
graph = { start: [] }
K = 2000
k = 0
Dq = 30
goal_found = False


plt.ion() # turns 'interactive mode' on
plt.plot(goal[1], goal[0],'y*') # puts a yellow asterisk at the goal
plt.plot(start[1], start[0],'g*') # puts a yellow x at the start
plt.imshow(map)

while k < K and not goal_found:
  print(k)
  '''
        if qnewqnew​ is less thanΔqΔq from qgoalqgoal​, qnew=qgoalqnew​=qgoal​

        if edge between qnearqnear​ and qnewqnew​ is collision-free:

            Add qnewqnew​ to G

            Add an edge between qnearqnear​ and qnewqnew​

            Increment k
  '''
  # A random configuration in C
  q_rand = (np.random.randint(0, len(map)), np.random.randint(0, len(map[0])))
  # if map[q_rand[0]][q_rand[1]]:
  #     continue

  # The nearest vertex to qrand that is already in G
  distances = []
  for node in graph.keys():
      distances.append((euclidean_distance(node, q_rand), node))
  distances.sort()
  q_near = distances[0][1]

  # Compute a new configuration by moving Δq from qnear into the direction of 
  # qrand or use qrand if closer to qnear than Δq
  q_new = q_rand
  if euclidean_distance(q_near, q_rand) > Dq:
      pt = step_from_to(q_near)(q_rand)(Dq)
      q_new = (int(pt[0]), int(pt[1]))
  if euclidean_distance(q_new, goal) < Dq:
      q_new = goal

      # q_new = (int(q_near[0] + (q_rand[0] - q_near[0])/euclidean_distance(q_near, q_rand)), int(q_near[1] + (q_rand[1] - q_near[1])/euclidean_distance(q_near, q_rand)))
  # if map[q_new[0]][q_new[1]]:
  #     continue

  graph[q_new] = []
  for node in graph.keys():
      dist = euclidean_distance(node, q_new)
      if dist < Dq:
          graph[node].append((dist, q_new))
          graph[q_new].append((dist, node))

  if q_new != goal:
    plt.plot(q_new[1], q_new[0],'b.') 
  plt.show()
  plt.pause(0.000001)
  if euclidean_distance(q_new, goal) < Dq:
      goal_found = True
  k += 1


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

    plt.plot(current[1], current[0],'y.')    
    plt.show()
    plt.pause(0.000001)

    for (cost, neighbor) in get_neighbors(graph)(current[0], current[1]):
        if neighbor in visited:
            continue

        candidate_distance = distance + cost
        if candidate_distance < distances[neighbor]:
            distances[neighbor] = candidate_distance
            heuristic_distance = candidate_distance + euclidean_distance(neighbor, goal)
            heappush(queue, (heuristic_distance, neighbor))
            parent[neighbor] = current

print("parent created")
print(parent)
print(len(parent.keys()))

path = []
key = goal
plt.ioff()

for key in parent.keys():
    # print("key", key)
    # print("value", parent[key])
    # key = parent[key]
    path.insert(0, key)
    # print(">", key, parent[key])
    plt.plot([key[1],parent[key][1]],[key[0],parent[key][0]],'ro-', linewidth=2, markersize=3)
    # plt.plot([key[1],parent[key][1]],[key[0],parent[key][0]],'ro-', linewidth=2, markersize=3)
    if key == start:
        print("start reached")
        break


path.append(goal)

for p in path:
  print("path", p)
    #  plt.plot(p[1], p[0],'r*')

plt.show()
