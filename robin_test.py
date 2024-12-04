from robin_client import Client
import time

# Define the robot movement logic
def move_robot_to_position(value):
    """
    Move the robot to a predefined position based on the value.
    Args:
        value (int): The predefined position index.
    """
    positions = {
        1: "Position A",
        2: "Position B",
        3: "Position C",
    }
    if value in positions:
        print(f"Moving robot to {positions[value]}...")
        # Simulate robot movement with a delay
        time.sleep(2)  # Replace with actual robot movement logic
        print(f"Robot has reached {positions[value]}.")
    else:
        print(f"No predefined position for value {value}. Please add it to the positions map.")

def main():
    # Initialize the client with the server URL
    client = Client("http://172.31.1.79:65432/process")

    # Predefined list of value-question pairs
    queries = [
        (1, "Is there a human? Only answer True or False."),
        (2, "How many humans in the scene?"),
        # (3, "Describe the scene in detail."),
    ]

    responses = []  # Store all responses for inspection

    try:
        for value, question in queries:
            # Move the robot to the predefined position
            print(f"\nStarting inspection for Value={value}, Question='{question}'")
            move_robot_to_position(value)

            # Send the question to the server
            print(f"Sending Question: '{question}'")
            response = client.send_request(value, question)  # No value sent to server

            # Store and print the response
            responses.append({"value": value, "question": question, "response": response})
            print("Response:", response)

        # After all inspections are done, wait for human input
        print("\nAll questions have been answered.")
        print("Press Enter to continue to the next step after inspection.")
        input()  # Wait for user to press Enter

        # Display all collected responses
        print("\nCollected Responses for Review:")
        for idx, entry in enumerate(responses, 1):
            print(f"{idx}. Question: {entry['question']}, Response: {entry['response']}")

    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
