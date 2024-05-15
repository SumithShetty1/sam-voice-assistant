import os
import pyautogui
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

        # Check if the file already exists
        count = 1
        while os.path.exists(file_path):
            # Append a number to the filename
            file_name = f"screenshot ({count}).png"
            file_path = os.path.join(base_directory, file_name)
            count += 1

        # Capture the screenshot of the entire screen
        screen_capture = pyautogui.screenshot()
        screen_capture.save(file_path)

        # Inform the user about successful screenshot capture
        speak(f"I've captured a screenshot of the entire screen and saved it as {file_name}, boss.")
    except Exception as e:
        speak(f"An error occurred")
        speak("Oops! Something went wrong while trying to capture the screenshot, boss.")


# Function to capture a screenshot using the Snipping Tool
def capture_snipping():
    try:
        # Open the Snipping Tool
        pyautogui.hotkey('win', 'shift', 's')

        # Instruct the user to use the Snipping Tool to select the area to capture
        speak("Please use the Snipping tool to select the area you'd like to capture, boss.")
    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to capture the screenshot, boss.")


# Function to handle screenshot requests
def screenshot(query):
    if "in snipping tool" in query:
        capture_snipping()
    else:
        capture_full_screen(query)
