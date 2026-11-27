
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from algorithms.sorting import merge_sort

with open("data/parcels.json", "r") as file:
    parcels = json.load(file)

sorted_parcels = merge_sort(parcels)

print("\nSORTED PARCELS")
print("-" * 40)

for parcel in sorted_parcels:
    print(
        parcel["id"],
        "| Priority:", parcel["priority"],
        "| Deadline:", parcel["deadline"]
    )
