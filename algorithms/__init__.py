"""
algorithms package
------------------
Public re-exports so callers can do:

    from algorithms import merge_sort, knapsack, build_graph, dijkstra, get_path, nearest_neighbor
"""

from algorithms.sorting  import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import build_graph, dijkstra, get_path
from algorithms.tsp      import nearest_neighbor

__all__ = [
    "merge_sort",
    "knapsack",
    "build_graph",
    "dijkstra",
    "get_path",
    "nearest_neighbor",
]
