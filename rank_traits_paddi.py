import json
from collections import defaultdict
from math import log2

# Load board from file
with open("board_s_f6f28223.json", "r") as f:
    players = json.load(f)

def calculate_entropy(value_counts, total):
    """Calculate entropy (information gain metric)"""
    entropy = 0
    for count in value_counts:
        p = count / total
        if p > 0:
            entropy -= p * log2(p)
    return entropy


def rank_traits(players):
    total_players = len(players)
    trait_value_counts = defaultdict(lambda: defaultdict(int))

    # Count occurrences of each trait value
    for player in players:
        for trait, value in player["traits"].items():
            trait_value_counts[trait][value] += 1

    trait_scores = []

    for trait, values in trait_value_counts.items():
        counts = list(values.values())

        # Skip useless traits (only one value across all players)
        if len(counts) <= 1:
            continue

        entropy = calculate_entropy(counts, total_players)

        trait_scores.append({
            "trait": trait,
            "entropy": entropy,
            "distribution": dict(values)
        })

    # Sort by highest entropy (best split first)
    trait_scores.sort(key=lambda x: x["entropy"], reverse=True)

    return trait_scores


ranked = rank_traits(players)

# Print top 5 best traits
for trait in ranked[:5]:
    print(f"Trait: {trait['trait']}")
    print(f"Distribution: {trait['distribution']}")
    print(f"Entropy: {trait['entropy']:.4f}")
    print("-" * 40)