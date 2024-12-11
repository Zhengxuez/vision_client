from robin_client import Client
import threading
import time

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
    client = Client("http://172.31.1.79:65432/process")
    queries = [
        (1, "Is the vial holder empty?"),
        (2, "Is the door of Quantos opened?"),
    ]
    response_received = threading.Event()  # Event to signal when to continue
    response_status = [None] 

    def check_response(value, question):
        nonlocal response_status
        while True:
            response = client.send_request(value, question)
            if response:  # If the response is True, allow the loop to continue
                response_status[0] = True
                response_received.set()
                break
            else:  # If response is False, wait for manual intervention
                print("Waiting for manual recovery. Press Enter to retry...")
                input()
                response_received.clear()

    try:
        for value, question in queries:
            # Move the robot to the predefined position
            move_robot_to_position(value)

            # Start a thread to check the response
            response_received.clear()  # Clear the event before starting
            response_status[0] = None  # Reset the response status
            response_thread = threading.Thread(target=check_response, args=(value, question))
            response_thread.start()

            # Wait until the response thread signals to continue
            response_received.wait()

            if response_status[0]:
                print(f"Query {value} passed, moving to the next step.")
            else:
                print(f"Query {value} failed but recovered. Continuing...")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()