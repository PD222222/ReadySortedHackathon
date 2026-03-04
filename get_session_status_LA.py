import requests
import json

BASE_URL = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
SESSION = "s_f6f28223"



def get_session_status(SESSION):
    headers = {
        "X-Session-Id": SESSION
    }

    response = requests.get(
        f"{BASE_URL}/sessions/{SESSION}/status",
        headers=headers
    )

    if response.status_code != 200:
        print("Error getting session status:", response.status_code)
        print(response.text)
        return None

    data = response.json()
    return data

session_data = get_session_status(SESSION)
print("session status:", session_data)