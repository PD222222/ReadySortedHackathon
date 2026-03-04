import requests


BASE_URL = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
TEAM_ID = "team-14cba74d-6cd3-49a7-aeb3-f727339624c1"

headers = {
    "X-Team-Id": TEAM_ID
}

def start_session():
    response = requests.post(
        f"{BASE_URL}/sessions/start",
        headers=headers
    )
    return response.json()["sessionId"]

def get_board(session_id):
    response = requests.get(
        f"{BASE_URL}/sessions/{session_id}/board",
        headers=headers
    )
    
    if response.status_code != 200:
        print("Error fetching board:", response.status_code)
        print(response.text)
        return None
    
    return response.json()

# ---- Run ----
session_id = start_session()
print("Session ID:", session_id)

board = get_board(session_id)
print("Board data:")
print(board)