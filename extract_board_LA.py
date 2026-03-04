import json

import requests


def load_candidates(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def filter_candidates(candidates, trait_key, target_value):
    """
    Keeps only candidates where the trait matches the target_value.
    Example: filter_candidates(data, "has_dimples", True)
    """
    return [c for c in candidates if c['traits'].get(trait_key) == target_value]


# 1. Load your 64 characters
all_candidates = load_candidates("board_s_f6f28223.json")
remaining = all_candidates

print(f"Starting with {len(remaining)} candidates.")



# THIS NARROWS DOWN TO 1 CANDIDATE BASED ON THE QUESTIONS ASKED AND THEIR ANSWERS

# 1. Keep if commute_type IS 'bus' OR if it's missing (None)
remaining = [c for c in remaining if c['traits'].get("commute_type") == "bus" or c['traits'].get("commute_type") is None]
print(f"After bus filter: {len(remaining)} left.")

# 2. Keep if hair_length IS NOT 'medium' OR if it's missing (None)
remaining = [c for c in remaining if c['traits'].get("hair_length") != "medium" or c['traits'].get("hair_length") is None]
print(f"After hair length filter: {len(remaining)} left.")

# 3. Keep if bottom_type IS NOT 'jeans' OR if it's missing (None)
remaining = [c for c in remaining if c['traits'].get("bottom_type") != "jeans" or c['traits'].get("bottom_type") is None]
print(f"After bottom type filter: {len(remaining)} left.")

# 4. Keep if eyebrow_style IS NOT 'thick' OR if it's missing (None)
remaining = [c for c in remaining if c['traits'].get("eyebrow_style") != "thick" or c['traits'].get("eyebrow_style") is None]
print(f"After eyebrow style filter: {len(remaining)} left.")

# 5. Keep if carries_laptop IS False OR if it's missing (None)
# Note: Using 'is False' explicitly helps distinguish from None
remaining = [c for c in remaining if c['traits'].get("carries_laptop") is False or c['traits'].get("carries_laptop") is None]
print(f"After carries laptop filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("preferred_editor") == "Other" or c['traits'].get("preferred_editor") is None]
print(f"After preferred editor filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("hat_type") != "cap" or c['traits'].get("hat_type") is None]
print(f"After hat type filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("eyebrow_style") != "arched" or c['traits'].get("eyebrow_style") is None]
print(f"After eyebrow style filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("skin_tone") != "A" or c['traits'].get("skin_tone") is None]
print(f"After skin tone filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("faculty") == "Arts" or c['traits'].get("faculty") is None]
print(f"After faculty filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("food_pref") == "vegan" or c['traits'].get("food_pref") is None]
print(f"After food preference filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("wears_necklace") is True or c['traits'].get("wears_necklace") is None]
print(f"After wears necklace filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("wears_hoodie") is True or c['traits'].get("wears_hoodie") is None]
print(f"After wears hoodie filter: {len(remaining)} left.")

remaining = [c for c in remaining if c['traits'].get("library_frequency") != "low" or c['traits'].get("library_frequency") is None]
print(f"After library frequency filter: {len(remaining)} left.")
print(remaining)




# Save the remaining candidates to a new JSON file
def save_state(candidates, filename="remaining_candidates.json"):
    with open(filename, 'w') as f:
        # indent=4 makes it readable for humans
        json.dump(candidates, f, indent=4)
    print(f"Successfully saved {len(candidates)} candidates to {filename}")

save_state(remaining)







base_url = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
# AUTOMATE THESE VALUES
session_id = "s_f6f28223"  
question_id = "T02"





# ASK QUESTIONS HEREERERER
def ask_questions2(base_url, session_id, question_id):
    headers = {"questionId": question_id}

    response = requests.post(
        f"{base_url}/sessions/{session_id}/ask",
        json=headers
    )

    if response.status_code != 200:
        print("Error starting session:", response.status_code)
        print(response.text)
        return None

    return response.json()

# uncomment to ask api questions

#print("\n\n\n\nAsking questions...\n\n\n\n")
#question_result = ask_questions2(base_url, session_id)
#print(question_result)





# SUBMIT GUESSES HEREERERER
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

# uncomment to submit a guess

#print("\n\n\n\nSubmitting guess...\n\n\n\n")
#guess_result = submit_guess(base_url, session_id, 'P45')
#print(guess_result)