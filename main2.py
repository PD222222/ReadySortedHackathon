import requests

api_url = "https://guesswhoservice-cjrwkt3ccq-nw.a.run.app"
response = requests.get(api_url)

print(response.status_code)   # Check if request worked
print(response.text)          # Raw response

