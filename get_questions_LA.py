import requests
import json

BASE_URL = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
SESSION = "s_f6f28223"   # <-- PUT YOUR REAL TEAM ID HERE



def get_questions(SESSION):
    headers = {
        "X-Session-Id": SESSION
    }

    response = requests.get(
        f"{BASE_URL}/sessions/{SESSION}/questions",
        headers=headers
    )

    if response.status_code != 200:
        print("Error getting questions:", response.status_code)
        print(response.text)
        return None

    data = response.json()
    return data["questions"]

questions_data = get_questions(SESSION)
print("questions:", questions_data)

if questions_data:
    # 2. Save to a JSON file
    filename = f"questions_{SESSION}.json"
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(questions_data, f, indent=4)
    
    print(f"Successfully saved {len(questions_data)} questions to {filename}")
else:
    print("Failed to retrieve questions data; no file created.")
