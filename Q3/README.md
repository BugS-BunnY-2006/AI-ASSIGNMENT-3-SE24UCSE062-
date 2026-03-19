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
Good—this is exactly the level your answer should be at. Here’s **your version**, same depth, but tighter, cleaner, and slightly more technical so it stands out.



# **Approach**

The navigation system follows a **Sense–Plan–Act loop**, which is essential for real-time autonomous systems.

Initially, the UGV computes an optimal path from the start node to the goal node using the A* search algorithm. As the robot moves along this path, it continuously senses its environment (simulated using probabilistic obstacle generation).

If a new obstacle is detected in the planned path:

* The grid map is updated immediately
* The current path is discarded
* A new optimal path is recomputed from the robot’s current position

This cycle continues until the robot successfully reaches the goal.

This adaptive strategy allows the UGV to respond to environmental changes while maintaining efficient navigation.

---

# **Algorithm Used**

To handle dynamic environments, the system uses **Repeated A*** search.

Repeated A* works by:

* Running A* initially to compute a path
* Monitoring the environment during execution
* Re-running A* whenever the environment changes

This ensures that the path is always optimal with respect to the latest known map.

Other advanced algorithms for dynamic path planning include:

* **D*** (Dynamic A*)
* **D* Lite**
* **Real-Time A***

In this implementation, Repeated A* is used due to its simplicity and effectiveness for simulation.

---

# **Pseudocode**

```
Initialize grid map
Set start node and goal node

Compute initial path using A*

WHILE current node is not goal DO

    Move to next step along path

    Sense environment for obstacles

    IF obstacle detected THEN
        Update grid map
        Recompute path using A* from current node
    END IF

END WHILE

Goal reached
```

---

# **Measures of Effectiveness**

The performance of the UGV navigation is evaluated using:

* **Path Length** – Total number of steps taken to reach the goal
* **Execution Time** – Time required for computation and replanning
* **Nodes Expanded** – Number of grid cells explored during search
* **Number of Replans** – Frequency of path recomputation
* **Success Rate** – Whether the UGV successfully reaches the goal

---

# **Conclusion**

In dynamic environments, a fixed path is insufficient due to unpredictable obstacle behavior. By continuously sensing the environment and replanning paths using Repeated A*, the UGV can adapt in real time and maintain safe navigation.

This approach ensures that the system remains robust, flexible, and capable of finding near-optimal paths even under changing battlefield conditions.

---


  
