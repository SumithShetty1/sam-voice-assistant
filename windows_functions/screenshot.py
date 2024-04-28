import os
import pyautogui
import time
from sam_functions.speak import speak


# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Function to capture the entire screen
def capture_full_screen(query):
    try:
        file_name = "screenshot.png"
        if query:
            # Extract file name from query if mentioned
            if "name it as" in query or "save it as" in query:
                name_query = query.split("name it as ")[1] if "name it as" in query else query.split("save it as ")[1]
                file_name = name_query.split()[0] + ".png"

        # Define the base directory for the camera roll
        base_directory = os.path.join(os.path.expanduser("~"), "Documents", "Sam Virtual Assistant", "Pictures",
                                      "Screenshots")

        # Create the base directory if it doesn't exist
        create_directory(base_directory)

        # Construct the full file path
        file_path = os.path.join(base_directory, file_name)

        # Capture the screenshot of the entire screen
        screen_capture = pyautogui.screenshot()
        screen_capture.save(file_path)

        # Inform the user about successful screenshot capture
        print(f"Sam: I've captured a screenshot of the entire screen and saved it as {file_name}, sir.")
        speak(f"I've captured a screenshot of the entire screen and saved it as {file_name} sir")
    except Exception as e:
        print(f"Sam: An error occurred: {e}")
        print("Sam: Oops! Something went wrong while trying to capture the screenshot, sir.")
        speak("Oops! Something went wrong while trying to capture the screenshot sir")


# Function to capture a screenshot using the Snipping Tool
def capture_snipping():
    try:
        # Open the Snipping Tool
        pyautogui.hotkey('win', 'shift', 's')

        # Instruct the user to use the Snipping Tool to select the area to capture
        print("Sam: Please use the Snipping tool to select the area you'd like to capture, sir.")
        speak("Please use the Snipping tool to select the area you'd like to capture sir.")
    except Exception as e:
        print(f"Sam: An error occurred: {e}")
        print("Sam: Oops! Something went wrong while trying to capture the screenshot, sir.")
        speak("Oops! Something went wrong while trying to capture the screenshot sir")


# Function to handle screenshot requests
def screenshot(query):
    if "in snipping tool" in query:
        capture_snipping()
    else:
        capture_full_screen(query)
