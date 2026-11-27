# CourEx — Courier Route & Parcel Optimizer

> An intelligent courier logistics engine built with classic algorithms: sort parcels by priority, pack them optimally, find the shortest paths, and generate an efficient delivery route — all in pure Python.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Algorithms](#algorithms)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Performance Analysis](#performance-analysis)
- [Complexity Reference](#complexity-reference)
- [Limitations](#limitations)
- [Tech Stack](#tech-stack)

---

## Overview

CourEx tackles a real-world courier logistics problem using four fundamental algorithms from Design & Analysis of Algorithms. Given a set of parcels and a delivery network, it:

1. **Prioritizes** parcels by urgency and deadline (Merge Sort)
2. **Selects** the most valuable parcels that fit in the vehicle (0/1 Knapsack)
3. **Maps** the shortest road between every location pair (Dijkstra)
4. **Plans** the most efficient round-trip delivery route (Nearest-Neighbor TSP)

---

## Features

- 📦 Parcel prioritization by priority level and delivery deadline
- 🎒 Optimal parcel selection within vehicle weight capacity
- 🗺️ Weighted graph representation of the delivery network
- 🛣️ Shortest-path computation from the warehouse to all destinations
- 🔄 Approximate TSP delivery route that returns to the warehouse
- 📊 Performance benchmarking with execution-time charts
- 🧪 Unit tests for every algorithm module

---

## Algorithms

| # | Algorithm | Role | Complexity |
|---|-----------|------|------------|
| 1 | **Merge Sort** | Sort parcels by priority & deadline | O(n log n) |
| 2 | **0/1 Knapsack (DP)** | Maximize parcel value within weight limit | O(n × W) |
| 3 | **Dijkstra** | Shortest paths in weighted graph | O((V + E) log V) |
| 4 | **Nearest-Neighbor TSP** | Approximate delivery tour | O(V(V + E) log V + V²) |

> **Variable key** — n: parcels · W: vehicle capacity · V: graph vertices · E: graph edges

---

## Architecture

CourEx is split into three clearly separated layers:

```
┌─────────────────────────────────────────────────────┐
│                     main.py                         │
│  Thin orchestrator — calls pipeline steps in order, │
│  prints section headers, reports timings.           │
│  Config lives here: VEHICLE_CAPACITY, WAREHOUSE.    │
└────────────────┬──────────────────┬─────────────────┘
                 │                  │
    ┌────────────▼──────┐  ┌────────▼──────────────┐
    │   modules/        │  │   algorithms/          │
    │                   │  │                        │
    │  parcel_manager   │  │  sorting   → Merge Sort│
    │  · load_parcels   │  │  knapsack  → 0/1 DP    │
    │  · print helpers  │  │  dijkstra  → SSSP      │
    │                   │  │  tsp       → NN heuristic│
    │  route_manager    │  │                        │
    │  · load_locations │  │  __init__  re-exports  │
    │  · print helpers  │  │  all public symbols    │
    └───────────────────┘  └────────────────────────┘
                 │                  │
         ┌───────▼──────────────────▼──────┐
         │            data/                │
         │  parcels.json · locations.json  │
         └─────────────────────────────────┘
```

### Module responsibilities

| File | Responsibility |
|------|----------------|
| `main.py` | Pipeline orchestration, config constants, section printing |
| `modules/parcel_manager.py` | Load parcels from JSON; display sorted/selected parcel tables |
| `modules/route_manager.py` | Load locations from JSON; display graph, paths, and routes |
| `algorithms/sorting.py` | Pure Merge Sort — no domain knowledge |
| `algorithms/knapsack.py` | Pure 0/1 Knapsack DP — no domain knowledge |
| `algorithms/dijkstra.py` | `build_graph`, `dijkstra`, `get_path` |
| `algorithms/tsp.py` | Nearest-Neighbor TSP using pre-computed Dijkstra distances |
| `algorithms/__init__.py` | Re-exports all public algorithm symbols for clean imports |

---

## Project Structure

```
CourEx/
├── main.py                    # Entry point & pipeline orchestrator
├── README.md
├── DESIGN.md                  # Algorithm design & complexity notes
├── Mini-Courier-Planner-Report.pdf
│
├── data/
│   ├── parcels.json           # Sample parcel dataset
│   └── locations.json         # Delivery network graph
│
├── algorithms/
│   ├── __init__.py            # Public re-exports
│   ├── sorting.py             # Merge Sort
│   ├── knapsack.py            # 0/1 Knapsack via DP
│   ├── dijkstra.py            # Dijkstra's shortest path
│   └── tsp.py                 # Nearest-Neighbor TSP
│
├── modules/
│   ├── parcel_manager.py      # Parcel I/O + display helpers
│   └── route_manager.py       # Location/graph I/O + display helpers
│
├── tests/
│   ├── test_sorting.py
│   ├── test_knapsack.py
│   ├── test_dijkstra.py
│   ├── test_tsp.py
│   ├── performance_test.py    # Benchmarks across input sizes
│   └── generate_charts.py    # Matplotlib chart generation
│
└── results/
    ├── merge_sort_performance.png
    ├── knapsack_performance.png
    ├── dijkstra_performance.png
    └── tsp_performance.png
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Matplotlib (for performance charts only)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/CourEx.git
cd CourEx

# (Optional) Install Matplotlib for chart generation
pip install matplotlib
```

---

## Usage

### Run the full courier pipeline

```bash
python main.py
```

### Run algorithm unit tests

```bash
python -m tests.test_sorting
python -m tests.test_knapsack
python -m tests.test_dijkstra
python -m tests.test_tsp
```

### Run performance benchmarks

```bash
python -m tests.performance_test
```

### Generate performance charts

```bash
python -m tests.generate_charts
# Charts are saved to results/
```

---

## Sample Output

```
=======================================================
      CourEx — Courier Route & Parcel Optimizer
=======================================================

───────────────────────────────────────────────────────
  1. PARCEL PRIORITIZATION  (Merge Sort)
───────────────────────────────────────────────────────
  P101  |  Priority: 1  |  Deadline: 4
  P103  |  Priority: 1  |  Deadline: 3
  P102  |  Priority: 2  |  Deadline: 6
  ...

───────────────────────────────────────────────────────
  2. OPTIMAL PARCEL SELECTION  (0/1 Knapsack)
───────────────────────────────────────────────────────
  P101  |  Weight: 5 kg  |  Value: 100
  P102  |  Weight: 3 kg  |  Value: 80
  P104  |  Weight: 2 kg  |  Value: 50

  Total Weight : 10 kg
  Total Value  : 230

───────────────────────────────────────────────────────
  3. DELIVERY GRAPH
───────────────────────────────────────────────────────
  Nodes: ['W', 'A', 'B', 'C', 'D', 'E']
  6 locations, 9 roads

───────────────────────────────────────────────────────
  4. SHORTEST PATHS  (Dijkstra from warehouse)
───────────────────────────────────────────────────────
  W → A  |  Path: W → A  |  4 km
  W → B  |  Path: W → B  |  2 km
  ...

───────────────────────────────────────────────────────
  5. OPTIMIZED DELIVERY ROUTE  (Nearest-Neighbor TSP)
───────────────────────────────────────────────────────
  Route    : W → B → A → D → W
  Distance : 16 km

───────────────────────────────────────────────────────
  6. PERFORMANCE SUMMARY
───────────────────────────────────────────────────────
  Merge Sort    0.00001200 s
  Knapsack      0.00003400 s
  Dijkstra      0.00008900 s
  TSP           0.00021500 s

=======================================================
              CourEx — Planning Completed
=======================================================
```

---

## Performance Analysis

Benchmarks are run across a range of input sizes to verify theoretical complexities:

| Metric | Input Sizes |
|--------|-------------|
| Parcel count (Merge Sort / Knapsack) | 100, 500, 1 000, 2 000, 5 000 |
| Graph size (Dijkstra / TSP) | 10, 20, 40, 80 locations |

Charts are saved as PNGs in `results/` after running `generate_charts.py`.

---

## Complexity Reference

| Algorithm | Time | Space |
|-----------|------|-------|
| Merge Sort | O(n log n) | O(n) |
| 0/1 Knapsack | O(n × W) | O(n × W) |
| Dijkstra (Binary Heap) | O((V + E) log V) | O(V + E) |
| Nearest-Neighbor TSP | O(V(V + E) log V + V²) | O(V²) |

---

## Limitations

- Dataset is static (JSON files); no live database or GPS integration
- Vehicle capacity is a constant in `main.py` (`VEHICLE_CAPACITY = 10`)
- Nearest-Neighbor TSP is a heuristic — it does **not** guarantee the globally optimal route
- Deadlines are used for sorting priority only, not for time-window feasibility checks

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| Data Storage | JSON |
| Visualization | Matplotlib |
| Data Structures | Lists, Dicts, Graphs, Priority Queues |
| Paradigms | Divide & Conquer, Dynamic Programming, Greedy, Graph Algorithms |

---

*CourEx — where classic algorithms meet real-world logistics.*
