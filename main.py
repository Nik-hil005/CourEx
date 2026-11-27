"""
main.py
-------
CourEx — Courier Route & Parcel Optimizer
Entry point. Orchestrates the full delivery-planning pipeline.

Pipeline
  1. Load data          — parcels.json + locations.json
  2. Sort parcels       — Merge Sort  (priority → deadline)
  3. Select parcels     — 0/1 Knapsack DP
  4. Build graph        — adjacency list from location data
  5. Shortest paths     — Dijkstra from warehouse
  6. Delivery route     — Nearest-Neighbor TSP
  7. Performance report — execution times for each stage
"""

import time

from algorithms import (
    merge_sort,
    knapsack,
    build_graph,
    dijkstra,
    nearest_neighbor,
)
from modules.parcel_manager import (
    load_parcels,
    print_sorted_parcels,
    print_selected_parcels,
)
from modules.route_manager import (
    load_locations,
    get_destinations,
    print_graph_summary,
    print_shortest_paths,
    print_delivery_route,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

VEHICLE_CAPACITY = 10   # kg
WAREHOUSE        = "W"


# ---------------------------------------------------------------------------
# Pipeline steps (each returns its timing in seconds)
# ---------------------------------------------------------------------------

def step_sort(parcels: list[dict]) -> tuple[list[dict], float]:
    t0 = time.perf_counter()
    sorted_parcels = merge_sort(parcels)
    return sorted_parcels, time.perf_counter() - t0


def step_select(sorted_parcels: list[dict]) -> tuple[list[dict], int, float]:
    t0 = time.perf_counter()
    selected, total_value, _ = knapsack(sorted_parcels, VEHICLE_CAPACITY)
    return selected, total_value, time.perf_counter() - t0


def step_graph(location_data: dict) -> tuple[dict, float]:
    t0 = time.perf_counter()
    graph = build_graph(location_data)
    return graph, time.perf_counter() - t0


def step_dijkstra(graph: dict) -> tuple[dict, dict, float]:
    t0 = time.perf_counter()
    distances, previous = dijkstra(graph, WAREHOUSE)
    return distances, previous, time.perf_counter() - t0


def step_tsp(graph: dict, selected: list[dict]) -> tuple[list[str], float, float]:
    destinations = get_destinations(selected)
    t0 = time.perf_counter()
    route, distance = nearest_neighbor(graph, WAREHOUSE, destinations)
    return route, distance, time.perf_counter() - t0


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _header(text: str) -> None:
    print(f"\n{'─' * 55}")
    print(f"  {text}")
    print(f"{'─' * 55}")


def _banner(text: str) -> None:
    print("=" * 55)
    print(text.center(55))
    print("=" * 55)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    _banner("CourEx — Courier Route & Parcel Optimizer")

    # Load
    parcels       = load_parcels()
    location_data = load_locations()

    # 1 — Sort
    _header("1. PARCEL PRIORITIZATION  (Merge Sort)")
    sorted_parcels, t_sort = step_sort(parcels)
    print_sorted_parcels(sorted_parcels)

    # 2 — Select
    _header("2. OPTIMAL PARCEL SELECTION  (0/1 Knapsack)")
    selected, total_value, t_knapsack = step_select(sorted_parcels)
    total_weight = sum(p["weight"] for p in selected)
    print_selected_parcels(selected, total_weight, total_value)

    # 3 — Graph
    _header("3. DELIVERY GRAPH")
    graph, t_graph = step_graph(location_data)
    print_graph_summary(graph)

    # 4 — Shortest paths
    _header("4. SHORTEST PATHS  (Dijkstra from warehouse)")
    distances, previous, t_dijkstra = step_dijkstra(graph)
    print_shortest_paths(graph, distances, previous, WAREHOUSE)

    # 5 — Route
    _header("5. OPTIMIZED DELIVERY ROUTE  (Nearest-Neighbor TSP)")
    route, route_distance, t_tsp = step_tsp(graph, selected)
    print_delivery_route(route, route_distance)

    # 6 — Performance
    _header("6. PERFORMANCE SUMMARY")
    rows = [
        ("Merge Sort",  t_sort),
        ("Knapsack",    t_knapsack),
        ("Dijkstra",    t_dijkstra),
        ("TSP",         t_tsp),
    ]
    for label, elapsed in rows:
        print(f"  {label:<12}  {elapsed:.8f} s")

    print()
    _banner("CourEx — Planning Completed")


if __name__ == "__main__":
    main()
