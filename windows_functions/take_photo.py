import time
import cv2
import os
from sam_functions.speak import speak


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def take_photo(query):
    try:
        if "in camera" in query:
            # Call a function here to take a photo in cameras app
            pass

        # Extract file name from query if mentioned
        file_name = "photo.jpg"
        if "name it as" in query or "save it as" in query:
            name_query = query.split("name it as ")[1] if "name it as" in query else query.split("save it as ")[1]
            file_name = name_query.split()[0] + ".jpg"

        # Define the base directory for the camera roll
        base_directory = os.path.join(os.path.expanduser("~"), "Documents", "Sam Virtual Assistant", "Pictures",
                                      "Camera Roll")

        # Create the base directory if it doesn't exist
        create_directory(base_directory)

        # Construct the full file path
        file_path = os.path.join(base_directory, file_name)

        camera_index = 0

        # Open the camera
        cap = cv2.VideoCapture(camera_index)

        # Check if the camera is opened successfully
        if not cap.isOpened():
            print("Sam: Sorry, I couldn't open the camera, sir.")
            speak("Sorry I couldn't open the camera sir")
            return

        # Prompt user that photo will be taken after 3 seconds
        print("Sam: I'll capture a photo in 3 seconds, sir.")
        speak("I'll capture a photo in 3 seconds sir")

        # Create a window to display the live feed from the webcam
        cv2.namedWindow("Live Feed", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Live Feed", 800, 600)

        start_time = time.time()
        while time.time() - start_time < 3:
            # Capture a frame
            ret, frame = cap.read()

            if ret:
                # Display the frame in the window
                cv2.imshow("Live Feed", frame)

            # Check for user input to break the loop and capture the photo
            if cv2.waitKey(1) == ord('\n'):
                break

        # Capture a frame
        ret, frame = cap.read()

        if ret:
            # Save the captured frame as an image
            cv2.imwrite(file_path, frame)
            print(f"Sam: Photo has been taken and saved as {file_name}, sir.")
            speak(f"Photo has been taken and saved as {file_name} sir")

        # Release the camera
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Sam: An error occurred: {e}")
        print("Sam: Oops! Something went wrong while trying to capture the photo, sir.")
        speak("Oops! Something went wrong while trying to capture the photo sir.")
