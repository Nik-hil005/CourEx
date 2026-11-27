
import json

from algorithms.knapsack import knapsack

with open("data/parcels.json", "r") as file:
    parcels = json.load(file)

capacity = 10

selected, total_value, dp = knapsack(parcels, capacity)

print("\nOPTIMAL PACKING PLAN")
print("-" * 40)

for parcel in selected:
    print(
        parcel["id"],
        "| Weight:", parcel["weight"],
        "| Value:", parcel["value"]
    )

print("-" * 40)

total_weight = sum(p["weight"] for p in selected)

print("Total Weight:", total_weight, "kg")
print("Vehicle Capacity:", capacity, "kg")
print("Maximum Total Value:", total_value)

print("\nDP TABLE")

for row in dp:
    print(row)
