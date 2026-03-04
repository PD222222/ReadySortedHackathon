import json

def load_candidates(filepath):
    with open(filepath, 'r') as f:
        # Based on your snippet, this is likely a list of objects
        return json.load(f)

def filter_candidates(candidates, trait_key, target_value):
    """
    Keeps only candidates where the trait matches the target_value.
    Example: filter_candidates(data, "has_dimples", True)
    """
    return [c for c in candidates if c['traits'].get(trait_key) == target_value]

# --- Workflow Example ---

# 1. Load your 64 characters
all_candidates = load_candidates("board_s_f6f28223.json")
remaining = all_candidates

print(f"Starting with {len(remaining)} candidates.")


print(remaining[62])

