
import json

from algorithms.dijkstra import build_graph
from algorithms.tsp import nearest_neighbor

# Load locations
with open("data/locations.json", "r") as file:
    location_data = json.load(file)

# Build graph
graph = build_graph(location_data)

# Customer locations
destinations = ["A", "B", "C", "D", "E"]

# Generate delivery route
route, total_distance = nearest_neighbor(
    graph,
    "W",
    destinations
)

print("\nCOURIER DELIVERY ROUTE")
print("-" * 40)

print(" -> ".join(route))

print("Total Route Distance:", total_distance, "km")
