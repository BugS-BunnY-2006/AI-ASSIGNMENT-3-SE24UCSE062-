Q2 – UGV Navigation in Static Obstacle Environment

This program simulates an Unmanned Ground Vehicle (UGV) navigating a 70×70 grid-based battlefield with static obstacles known in advance. The grid represents the environment where each cell is either free or blocked by an obstacle, generated randomly based on a given density. The objective is to find the shortest path from a start node to a goal node while avoiding all obstacles.

The program uses the A* search algorithm, which combines the actual path cost and a heuristic (Manhattan distance) to efficiently guide the search. It ensures optimal pathfinding while reducing unnecessary exploration compared to uninformed search methods.

The algorithm calculates:

* Shortest path from start to goal
* Optimal navigation avoiding obstacles

It also measures:

* Number of nodes explored
* Execution time

---

## **How to Run**

```bash
python3 ugv_static.py
```

---

## **Example Input**

```
(No user input required – grid and obstacles are generated automatically)
```

---

## **Example Output**

```
Path Length: 132
Nodes Explored: 845
Execution Time: 0.0021 seconds
```

---

## **Dataset**

```
Grid-based environment (70x70) generated within the program with random obstacle density
```
