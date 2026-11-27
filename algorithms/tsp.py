
from algorithms.dijkstra import dijkstra, get_path


def nearest_neighbor(graph, start, destinations):

    # Calculate shortest paths from every location
    all_distances = {}
    all_previous = {}

    for source in graph:
        distances, previous = dijkstra(graph, source)

        all_distances[source] = distances
        all_previous[source] = previous

    unvisited = list(destinations)
    unvisited = [node for node in unvisited if node != start]

    route = [start]
    current = start
    total_distance = 0

    while unvisited:

        nearest = min(
            unvisited,
            key=lambda node: all_distances[current][node]
        )

        distance = all_distances[current][nearest]

        if distance == float("inf"):
            raise ValueError("Destination is unreachable")

        # Reconstruct the shortest road path
        path = get_path(all_previous[current], nearest)

        route.extend(path[1:])

        total_distance += distance

        unvisited.remove(nearest)
        current = nearest

    # Return to warehouse using shortest path
    return_distance = all_distances[current][start]

    if return_distance == float("inf"):
        raise ValueError("Warehouse is unreachable")

    return_path = get_path(
        all_previous[current],
        start
    )

    route.extend(return_path[1:])
    total_distance += return_distance

    return route, total_distance
