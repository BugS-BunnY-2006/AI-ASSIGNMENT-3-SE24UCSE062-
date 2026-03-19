import heapq
import random
import time

n = 70
grid = [[0]*n for _ in range(n)]

def generate_obstacles(density):
    for i in range(n):
        for j in range(n):
            if random.random() < density:
                grid[i][j] = 1

generate_obstacles(0.2)

start = (0, 0)
goal = (69, 69)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar():
    pq = []
    heapq.heappush(pq, (0, start))
    came = {}
    cost = {start: 0}
    visited = 0

    while pq:
        _, current = heapq.heappop(pq)
        visited += 1

        if current == goal:
            break

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0]+dx, current[1]+dy

            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                new_cost = cost[current]+1

                if (nx,ny) not in cost or new_cost < cost[(nx,ny)]:
                    cost[(nx,ny)] = new_cost
                    priority = new_cost + heuristic(goal,(nx,ny))
                    heapq.heappush(pq,(priority,(nx,ny)))
                    came[(nx,ny)] = current

    path = []
    node = goal
    while node in came:
        path.append(node)
        node = came[node]
    path.append(start)
    path.reverse()

    return path, len(path), visited


start_time = time.time()
path, length, visited = astar()
end_time = time.time()

print("Path Length:", length)
print("Nodes Explored:", visited)
print("Execution Time:", round(end_time - start_time, 6), "seconds")
