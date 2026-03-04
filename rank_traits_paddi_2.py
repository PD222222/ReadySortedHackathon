import json
from collections import defaultdict
from math import log2

# Load players
with open("remaining_candidates.json", "r") as f:
    players = json.load(f)

# Load questions
with open("questions_s_f6f28223.json", "r") as f:
    questions = json.load(f)

# Build mapping: traitKey -> questionId
trait_to_question = {
    q["traitKey"]: q["questionId"]
    for q in questions
}


def calculate_entropy(value_counts, total):
    """Calculate entropy (information gain metric)"""
    entropy = 0
    for count in value_counts:
        p = count / total
        if p > 0:
            entropy -= p * log2(p)
    return entropy


def rank_traits(players, trait_to_question):
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
            "questionId": trait_to_question.get(trait, None),
            "entropy": entropy,
            "distribution": dict(values)
        })

    # Sort by highest entropy (best split first)
    trait_scores.sort(key=lambda x: x["entropy"], reverse=True)

    return trait_scores


ranked = rank_traits(players, trait_to_question)

# Print top 5 best traits
for trait in ranked[:5]:
    print(f"Trait: {trait['trait']}")
    print(f"QuestionId: {trait['questionId']}")
    print(f"Distribution: {trait['distribution']}")
    print(f"Entropy: {trait['entropy']:.4f}")
    print("-" * 40)