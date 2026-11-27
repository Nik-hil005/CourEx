
import random
import time

from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor


def generate_parcels(n):

    parcels = []

    for i in range(n):

        parcels.append({
            "id": f"P{i}",
            "destination": "A",
            "weight": random.randint(1, 10),
            "priority": random.randint(1, 3),
            "deadline": random.randint(1, 30),
            "value": random.randint(10, 200)
        })

    return parcels


sizes = [100, 500, 1000, 2000, 5000]

print("\nPERFORMANCE ANALYSIS")
print("=" * 60)

print(
    f"{'Input Size':<15}"
    f"{'Merge Sort (s)':<20}"
    f"{'Knapsack (s)':<20}"
)

for n in sizes:

    parcels = generate_parcels(n)

    # Measure Merge Sort
    start = time.perf_counter()

    sorted_parcels = merge_sort(parcels)

    sorting_time = time.perf_counter() - start

    # Measure Knapsack
    start = time.perf_counter()

    selected, value, dp = knapsack(parcels, 50)

    knapsack_time = time.perf_counter() - start

    print(
        f"{n:<15}"
        f"{sorting_time:<20.8f}"
        f"{knapsack_time:<20.8f}"
    )

print("=" * 60)
print("Performance testing completed.")


# GRAPH ALGORITHM PERFORMANCE TESTING

def generate_graph(n):

    graph = {}

    for i in range(n):
        graph[f"L{i}"] = []

    # Create a connected graph using a chain
    for i in range(n - 1):

        a = f"L{i}"
        b = f"L{i + 1}"
        weight = random.randint(1, 20)

        graph[a].append((b, weight))
        graph[b].append((a, weight))

    # Add additional random roads
    for _ in range(n * 2):

        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)

        if a != b:

            node_a = f"L{a}"
            node_b = f"L{b}"

            weight = random.randint(1, 20)

            graph[node_a].append((node_b, weight))
            graph[node_b].append((node_a, weight))

    return graph


graph_sizes = [10, 20, 40, 80]

print("\nGRAPH ALGORITHM PERFORMANCE")
print("=" * 65)

print(
    f"{'Locations':<15}"
    f"{'Dijkstra (s)':<20}"
    f"{'TSP (s)':<20}"
)

for n in graph_sizes:

    graph = generate_graph(n)

    # Measure Dijkstra
    start = time.perf_counter()

    distances, previous = dijkstra(graph, "L0")

    dijkstra_time = time.perf_counter() - start

    # Measure TSP
    destinations = [f"L{i}" for i in range(1, n)]

    start = time.perf_counter()

    route, distance = nearest_neighbor(
        graph,
        "L0",
        destinations
    )

    tsp_time = time.perf_counter() - start

    print(
        f"{n:<15}"
        f"{dijkstra_time:<20.8f}"
        f"{tsp_time:<20.8f}"
    )

print("=" * 65)
print("Graph performance testing completed.")

