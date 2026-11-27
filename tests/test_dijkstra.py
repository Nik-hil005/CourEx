
import json

from algorithms.dijkstra import build_graph, dijkstra, get_path

# Load location data
with open("data/locations.json", "r") as file:
    location_data = json.load(file)

# Build graph
graph = build_graph(location_data)

# Calculate shortest paths from warehouse
distances, previous = dijkstra(graph, "W")

print("\nDIJKSTRA SHORTEST PATHS")
print("-" * 40)

for location in graph:

    path = get_path(previous, location)

    print(
        "Warehouse to", location,
        "| Path:", " -> ".join(path),
        "| Distance:", distances[location], "km"
    )
