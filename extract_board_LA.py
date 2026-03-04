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

remaining = [c for c in remaining if c['traits'].get("hair_length") != "medium"]
print(f"After hair length filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("bottom_type") != "jeans"]
print(f"After bottom type filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("eyebrow_style") != "thick"]
print(f"After eyebrow style filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("carries_laptop") == False]
print(f"After carries laptop filter: {len(remaining)} left.")

print(remaining)





def save_state(candidates, filename="remaining_candidates.json"):
    with open(filename, 'w') as f:
        # indent=4 makes it readable for humans
        json.dump(candidates, f, indent=4)
    print(f"Successfully saved {len(candidates)} candidates to {filename}")

save_state(remaining)







base_url = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
session_id = "s_f6f28223"  


question_id = "T02"






def ask_questions2(base_url, session_id):
    headers = {"questionId": "T28"}

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

#print("\n\n\n\nAsking questions...\n\n\n\n")
#question_result = ask_questions2(base_url, session_id)
#print(question_result)


def submit_guess(base_url, session_id, candidate_id):

    
    # The API expects the candidateId in the body
    payload = {
        "candidateId": candidate_id
    }

    response = requests.post(
        f"{base_url}/sessions/{session_id}/guess",
        json=payload
    )

    if response.status_code != 200:
        print("Error submitting guess:", response.status_code)
        print(response.text)
        return None

    return response.json()

#print("\n\n\n\nSubmitting guess...\n\n\n\n")
#guess_result = submit_guess(base_url, session_id, 'P58')
#print(guess_result)