
import os
import matplotlib.pyplot as plt

# Create results folder if it does not exist
os.makedirs("results", exist_ok=True)

# Parcel algorithm benchmark results
parcel_sizes = [100, 500, 1000, 2000, 5000]

merge_sort_times = [
    0.00029790,
    0.00124180,
    0.00699580,
    0.00946820,
    0.01840580
]

knapsack_times = [
    0.00109910,
    0.00529860,
    0.02065380,
    0.02326360,
    0.04700740
]

# Graph algorithm benchmark results
graph_sizes = [10, 20, 40, 80]

dijkstra_times = [
    0.00003680,
    0.00003590,
    0.00024710,
    0.00012050
]

tsp_times = [
    0.00017750,
    0.00058530,
    0.00253210,
    0.00966500
]

# Chart 1: Merge Sort
plt.figure()
plt.plot(parcel_sizes, merge_sort_times, marker="o")
plt.title("Merge Sort Performance")
plt.xlabel("Number of Parcels")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.savefig("results/merge_sort_performance.png")
plt.close()

# Chart 2: Knapsack
plt.figure()
plt.plot(parcel_sizes, knapsack_times, marker="o")
plt.title("Knapsack Performance")
plt.xlabel("Number of Parcels")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.savefig("results/knapsack_performance.png")
plt.close()

# Chart 3: Dijkstra
plt.figure()
plt.plot(graph_sizes, dijkstra_times, marker="o")
plt.title("Dijkstra Performance")
plt.xlabel("Number of Locations")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.savefig("results/dijkstra_performance.png")
plt.close()

# Chart 4: TSP
plt.figure()
plt.plot(graph_sizes, tsp_times, marker="o")
plt.title("Nearest Neighbor TSP Performance")
plt.xlabel("Number of Locations")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.savefig("results/tsp_performance.png")
plt.close()

print("All performance charts generated successfully!")

print("\nGenerated files:")
print("1. merge_sort_performance.png")
print("2. knapsack_performance.png")
print("3. dijkstra_performance.png")
print("4. tsp_performance.png")
