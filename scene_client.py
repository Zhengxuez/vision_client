from requests import post

class SceneClient:
    def __init__(self, service_url):
        self.service_url = service_url
        self.headers = {"Content-Type": "text/xml"}

    def describe_scene(self):
        body = """
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="acl.kuka.soap">
            <soapenv:Header/>
            <soapenv:Body>
                <tns:DescribeScene>
                    <tns:request>Describe the scene in the view</tns:request>
                </tns:DescribeScene>
            </soapenv:Body>
        </soapenv:Envelope>
        """
        response = post(self.service_url, data=body, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

# Usage example
if __name__ == "__main__":
    service_url = "http://172.31.1.79:65432/acl.kuka.soap"
    client = SceneClient(service_url)
    try:
        result = client.describe_scene()
        print("Describe Scene Response:")
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
