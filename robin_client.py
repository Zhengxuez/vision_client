import requests

def client():
    url = "http://172.31.1.79:65432/process"
    payload = {"prompt": "Describe the scene"}
    response = requests.post(url, json=payload)
    print("Response:", response.json())
client()
