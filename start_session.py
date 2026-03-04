import requests

BASE_URL = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
TEAM_ID = "your-team-id-here"   # <-- PUT YOUR REAL TEAM ID HERE

def start_session():
    headers = {
        "X-Team-Id": "team-14cba74d-6cd3-49a7-aeb3-f727339624c1"
    }

    response = requests.post(
        f"{BASE_URL}/sessions/start",
        headers=headers
    )

    if response.status_code != 200:
        print("Error starting session:", response.status_code)
        print(response.text)
        return None

    data = response.json()
    return data["sessionId"]

session_id = start_session()
print("Session ID:", session_id)