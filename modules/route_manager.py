"""
route_manager.py
----------------
Handles loading location/graph data from disk and all route-related
display / reporting helpers used by the main pipeline.
"""

import json


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_locations(path: str = "data/locations.json") -> dict:
    """Return the raw location dict (keys: 'locations', 'roads') from *path*."""
    with open(path, "r") as fh:
        return json.load(fh)


def get_destinations(selected_parcels: list[dict]) -> list[str]:
    """Return an ordered, deduplicated list of destination nodes from *selected_parcels*."""
    return list(dict.fromkeys(p["destination"] for p in selected_parcels))


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def print_graph_summary(graph: dict) -> None:
    """Print a one-line summary of the loaded delivery graph."""
    node_count = len(graph)
    edge_count = sum(len(neighbours) for neighbours in graph.values()) // 2
    print(f"  Nodes: {list(graph.keys())}")
    print(f"  {node_count} locations, {edge_count} roads")


def print_shortest_paths(graph: dict, distances: dict, previous: dict, source: str) -> None:
    """Print shortest paths from *source* to every other node in *graph*."""
    from algorithms.dijkstra import get_path  # local import to avoid circular deps

    for node in graph:
        path = get_path(previous, node)
        print(f"  {source} → {node}  |  Path: {' → '.join(path)}  |  {distances[node]} km")


def print_delivery_route(route: list[str], total_distance: int | float) -> None:
    """Print the TSP delivery route and its total distance."""
    print(f"  Route    : {' → '.join(route)}")
    print(f"  Distance : {total_distance} km")
