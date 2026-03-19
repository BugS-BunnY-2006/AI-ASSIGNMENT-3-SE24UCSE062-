ASSIGNMENT-3

This program implements **Dijkstra’s Algorithm (Uniform Cost Search)** to compute the shortest path between Indian cities.

The cities are modeled as nodes and road distances as weighted edges. The graph is constructed using data from a CSV file (`india_roads.csv`). A priority queue (min-heap) is used to always expand the node with the minimum path cost.

The algorithm calculates:

* Shortest distance from a given source city to all other cities
* Optimal path using parent tracking

It also measures:

* Number of nodes explored
* Execution time

---

## **How to Run**

```bash
python3 dijkstra_india.py
```

---

## **Example Input**

```
Enter source city: Delhi
```

---

## **Example Output**

```
Mumbai : 1488.0 km | Path -> Delhi -> Jaipur -> Ahmedabad -> Surat -> Mumbai
Chennai : 2350.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad -> Chennai
Bangalore : 2290.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad -> Bangalore

Nodes explored: 18
Execution time: 0.0003 seconds
```
