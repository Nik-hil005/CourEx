
import heapq


def build_graph(location_data):

    graph = {}

    # Create an empty list for every location
    for location in location_data["locations"]:
        graph[location] = []

    # Add roads in both directions
    for road in location_data["roads"]:

        source = road["from"]
        destination = road["to"]
        distance = road["distance"]

        graph[source].append((destination, distance))
        graph[destination].append((source, distance))

    return graph


def dijkstra(graph, start):

    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


def get_path(previous, destination):

    path = []

    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path
