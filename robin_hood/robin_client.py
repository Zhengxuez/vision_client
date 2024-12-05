import requests

class Client:
    def __init__(self, server_url):
        """
        Initialize the client with the server URL.
        """
        self.server_url = server_url

    def send_request(self, value, question):
        payload = {"value": value, "prompt": question}

        try:
            response = requests.post(self.server_url, json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Server returned status code {response.status_code}"}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}