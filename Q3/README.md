Q3 – UGV Navigation in Dynamic Obstacle Environment

Problem Description...
In the previous problem, obstacles were assumed to be static and known beforehand.
However, in real-world environments obstacles may be dynamic, meaning they can appear or move while the robot is navigating.

Therefore, the Unmanned Ground Vehicle (UGV) must be able to detect obstacles during navigation and replan its path dynamically to reach the goal safely.

This program simulates an Unmanned Ground Vehicle (UGV) navigating a battlefield environment where obstacles are dynamic and not known in advance. Unlike static environments, obstacles may appear during movement, requiring the system to adapt in real time.

The program uses a replanning strategy based on repeated A* search. At each step, the UGV recalculates the optimal path from its current position to the goal. If a new obstacle appears in the planned path, the algorithm updates the grid and recomputes a new path.

The algorithm calculates:

* Optimal path under changing conditions
* Real-time navigation decisions

It also measures:

* Number of steps taken
* Number of replanning operations
* Execution time

---


## **How to Run**

```bash id="r07ahd"
python3 ugv_dynamic.py
```

---

## **Example Input**

```id="y3rq6t"
(No user input required – environment changes dynamically during execution)
```

---

## **Example Output**

```id="q4b49y"
Goal Reached
Steps Taken: 58
Replans: 23
Execution Time: 0.0034 seconds
```

---

## **Dataset**

```id="7ed9c0"
Dynamic grid environment generated within the program where obstacles can appear randomly during navigation
```
