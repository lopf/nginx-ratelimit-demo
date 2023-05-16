import requests

URL = "http://nginx/"

for _ in range(20):
    response = requests.get(URL)
    print(f"Response: {response.status_code}")


