import requests

def test_response_code():
    response = requests.get("https://reqres.in")
    assert response.status_code == 200