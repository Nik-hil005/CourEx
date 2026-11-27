
# MINI-COURIER PLANNER
## Design and Analysis of Algorithms – Capstone Project

**University:** K.R. Mangalam University, Gurugram  
**Course:** Design & Analysis of Algorithms (ETCCDA302)  
**Project:** Mini-Courier Planner  
**Programming Language:** Python

## 1. Problem Definition

The Mini-Courier Planner is a Python-based application designed to simulate an intelligent courier delivery system. It prioritizes parcels, optimizes vehicle capacity, calculates shortest paths between delivery locations, and generates an efficient delivery route.

The main objective is to maximize the value of selected parcels without exceeding vehicle capacity and to generate an approximate delivery route with a low total distance.

## 2. Objectives

- Prioritize parcels based on priority and delivery deadlines.
- Select parcels using Dynamic Programming.
- Represent delivery locations using a weighted graph.
- Calculate shortest paths using Dijkstra's Algorithm.
- Generate an approximate delivery route using Nearest Neighbor TSP.
- Measure and compare algorithm execution times.

## 3. Input Data

Each parcel contains:
- Parcel ID
- Destination
- Weight
- Priority
- Delivery deadline
- Value score

The delivery vehicle has a maximum capacity of 10 kg.

The location graph contains one warehouse and five customer locations connected by weighted roads.

## 4. Algorithms Selected

### A. Merge Sort

Parcels are sorted by priority and deadline. Priority 1 represents the highest priority, followed by priority 2 and priority 3.

### B. Dynamic Programming – 0/1 Knapsack

Selects parcels that maximize total value without exceeding the vehicle's maximum weight capacity. Each parcel can either be selected or rejected.

### C. Dijkstra's Algorithm

Calculates shortest paths in a weighted graph with non-negative edge weights. A priority queue is used to efficiently select the next vertex.

### D. Nearest Neighbor TSP Approximation

Generates an approximate delivery route by repeatedly visiting the nearest unvisited destination using precomputed shortest-path distances. Finally, it returns to the warehouse.

The algorithm does not guarantee the globally shortest possible TSP route.

## 5. Algorithm Complexity

| Algorithm | Time Complexity |
|---|---|
| Merge Sort | O(n log n) |
| 0/1 Knapsack | O(n × W) |
| Dijkstra (Binary Heap) | O((V + E) log V) |
| Nearest Neighbor TSP with All-Pairs Dijkstra | O(V(V + E) log V + V²) |

Where:
- n = Number of parcels
- W = Vehicle capacity
- V = Number of graph vertices
- E = Number of graph edges

Knapsack space complexity: O(n × W).

Dijkstra space complexity: O(V + E).

## 6. Expected Output

The application displays:
- Sorted parcel list.
- Selected parcels.
- Total selected parcel weight and value.
- Shortest paths from the warehouse.
- Approximate delivery route.
- Total route distance.
- Execution time of major algorithms.

## 7. Performance Testing

The project evaluates algorithm execution time using different input sizes.

Parcel sizes:
100, 500, 1000, 2000, 5000.

Graph sizes:
10, 20, 40, 80 locations.

Four performance charts are generated using Matplotlib.

## 8. Conclusion

The Mini-Courier Planner integrates sorting, dynamic programming, greedy techniques, and graph algorithms into one application. It demonstrates how algorithmic concepts can solve practical courier delivery and resource optimization problems.
