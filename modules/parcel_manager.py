"""
parcel_manager.py
-----------------
Handles loading parcel data from disk and all parcel-related
display / reporting helpers used by the main pipeline.
"""

import json


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_parcels(path: str = "data/parcels.json") -> list[dict]:
    """Return the list of parcel dicts from *path*."""
    with open(path, "r") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def print_sorted_parcels(parcels: list[dict]) -> None:
    """Print each parcel's id, priority and deadline."""
    for p in parcels:
        print(f"  {p['id']}  |  Priority: {p['priority']}  |  Deadline: {p['deadline']}")


def print_selected_parcels(parcels: list[dict], total_weight: int, total_value: int) -> None:
    """Print the knapsack-selected parcels and their totals."""
    for p in parcels:
        print(f"  {p['id']}  |  Weight: {p['weight']} kg  |  Value: {p['value']}")
    print(f"\n  Total Weight : {total_weight} kg")
    print(f"  Total Value  : {total_value}")
