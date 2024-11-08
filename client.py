from suds.client import Client

def main():
    # Replace this URL with the actual URL of your SOAP WSDL
    url = 'http://0.0.0.0:65432/?wsdl'

    try:
        # Create a client using the WSDL
        client = Client(url)
        # Print list of available methods
        print(client)

        # Call the 'DescribeScene' method with the request string
        response = client.service.DescribeScene("describe the scene in the view")
        print("Response from server:", response)

    except Exception as e:
        print("Failed to connect to the SOAP service:", e)

if __name__ == "__main__":
    main()
