import requests

response = requests.get("https://reqres.in")

assert response.status_code == 200