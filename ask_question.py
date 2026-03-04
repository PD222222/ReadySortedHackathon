import requests

base_url = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
session_id = "s_f6f28223"  

def ask_questions2(base_url, session_id):
    payload = {"questionId": "T40", "value": "low"}

    response = requests.post(
        f"{base_url}/sessions/{session_id}/ask",
        json=payload
    )

    if response.status_code != 200:
        print("Error starting session:", response.status_code)
        print(response.text)
        return None

    return response.json()

# ASK QUESTIONS HEREERERER

print("\n\n\n\nAsking questions...\n\n\n\n")
question_result = ask_questions2(base_url, session_id)
print(question_result)
