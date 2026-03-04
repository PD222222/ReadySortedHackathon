import json

import requests


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


#print(remaining[62])

# 3. Suppose the API says "The top_color is NOT white"
# You keep only those where 'top_color' is NOT 'white'
remaining = [c for c in remaining if c['traits'].get("commute_type") == "bus"]
print(f"After bus filter: {len(remaining)} left.")


print(remaining)

def save_state(candidates, filename="remaining_candidates.json"):
    with open(filename, 'w') as f:
        # indent=4 makes it readable for humans
        json.dump(candidates, f, indent=4)
    print(f"Successfully saved {len(candidates)} candidates to {filename}")

save_state(remaining)







base_url = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
session_id = "s_f6f28223"  


question_id = "T39"






def ask_questions2(base_url, session_id):
    headers = {"questionId": "T39", "value": "bus"}

    response = requests.post(
        f"{base_url}/sessions/{session_id}/ask",
        json=headers
    )

    if response.status_code != 200:
        print("Error starting session:", response.status_code)
        print(response.text)
        return None

    return response.json()

# ASK QUESTIONS HEREERERER

#question_result = ask_questions2(base_url, session_id)
#print(question_result)