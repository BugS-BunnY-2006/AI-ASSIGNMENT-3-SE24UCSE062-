import heapq
import random
import time

n = 30
grid = [[0]*n for _ in range(n)]

start = (0, 0)
goal = (29, 29)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start):
    pq = []
    heapq.heappush(pq, (0, start))
    came = {}
    cost = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

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

    return path

def navigate():
    current = start
    steps = 0
    replans = 0

    while current != goal:
        path = astar(current)
        replans += 1

        if len(path) < 2:
            print("No Path Available")
            return

        next_step = path[1]

        if random.random() < 0.2:
            grid[next_step[0]][next_step[1]] = 1
        else:
            current = next_step
            steps += 1

    print("Goal Reached")
    print("Steps Taken:", steps)
    print("Replans:", replans)


start_time = time.time()
navigate()
end_time = time.time()

print("Execution Time:", round(end_time - start_time, 6), "seconds")
