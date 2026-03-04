import requests
import json

BASE_URL = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
SESSION = "s_f6f28223"   # <-- PUT YOUR REAL TEAM ID HERE



def get_board(SESSION):
    headers = {
        "X-Session-Id": SESSION
    }

    response = requests.get(
        f"{BASE_URL}/sessions/{SESSION}/board",
        headers=headers
    )

    if response.status_code != 200:
        print("Error getting board:", response.status_code)
        print(response.text)
        return None

    data = response.json()
    return data["board"]

board_data = get_board(SESSION)
print("board:", board_data)

if board_data:
    # 2. Save to a JSON file
    filename = f"board_{SESSION}.json"
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(board_data, f, indent=4)
    
    print(f"Successfully saved {len(board_data)} characters to {filename}")
else:
    print("Failed to retrieve board data; no file created.")
