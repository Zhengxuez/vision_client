from requests import post
import xml.etree.ElementTree as ET

class ArucoClient:
    def __init__(self, service_url):
        self.service_url = service_url
        self.headers = {"Content-Type": "text/xml"}

    def update_marker_frame(self, marker_id):
        # SOAP request body
        body = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="acl.kuka.soap">
            <soapenv:Header/>
            <soapenv:Body>
                <tns:UpdateMarkerFrame>
                    <tns:id>{marker_id}</tns:id>
                </tns:UpdateMarkerFrame>
            </soapenv:Body>
        </soapenv:Envelope>
        """
        # Send the request
        response = post(self.service_url, data=body, headers=self.headers)
        # Check for successful response
        if response.status_code == 200:
            return self.parse_response(response.text)
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

    @staticmethod
    def parse_response(response_xml):
        # Define namespaces for the XML
        ns = {
            "soapenv": "http://schemas.xmlsoap.org/soap/envelope/",
            "tns": "acl.kuka.soap"
        }
        # Parse the XML response
        root = ET.fromstring(response_xml)
        pose_element = root.find(".//tns:pose", ns)
        # Extract pose data
        if pose_element is not None:
            pose = {
                "x": float(pose_element.find("tns:x", ns).text),
                "y": float(pose_element.find("tns:y", ns).text),
                "z": float(pose_element.find("tns:z", ns).text),
                "a": float(pose_element.find("tns:a", ns).text),
                "b": float(pose_element.find("tns:b", ns).text),
                "c": float(pose_element.find("tns:c", ns).text),
            }
            return pose
        else:
            raise ValueError("Pose data not found in the response.")


# Usage Example
if __name__ == "__main__":
    service_url = "http://172.31.1.79:65432/acl.kuka.soap"
    client = ArucoClient(service_url)
    
    try:
        marker_id = 10  # Replace with the desired marker ID
        pose = client.update_marker_frame(marker_id)
        print(f"Pose Data: [x: {pose['x']}, y: {pose['y']}, z: {pose['z']}, a: {pose['a']}, b: {pose['b']}, c: {pose['c']}]")
    except Exception as e:
        print(f"An error occurred: {e}")
