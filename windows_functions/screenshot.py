import os
import pyautogui
from sam_functions.speak import speak


# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Function to capture the entire screen
def capture_full_screen(query, intent_data):
    try:
        # Initialize file_name with default value
        file_name = "screenshot.png"

        # Loop through each preposition pattern
        for prep in intent_data['text']:
            if prep in query:
                # Extract file name from the query based on the preposition
                name_query = query.split(prep)[1].strip()
                file_name = name_query.split()[0] + ".jpg"
                break
        
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
        speak(f"I've captured a screenshot of the entire screen and saved it as {file_name} sir.")
    except Exception as e:
        speak(f"An error occurred")
        speak("Oops! Something went wrong while trying to capture the screenshot sir.")


# Function to capture a screenshot using the Snipping Tool
def capture_snipping():
    try:
        # Open the Snipping Tool
        pyautogui.hotkey('win', 'shift', 's')

        # Instruct the user to use the Snipping Tool to select the area to capture
        speak("Please use the Snipping tool to select the area you'd like to capture sir.")
    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to capture the screenshot sir.")


# Function to handle screenshot requests
def screenshot(query, intent_data):
    if intent_data['intent'] == "snipping_tool_take_screenshot":
        capture_snipping()
    else:
        capture_full_screen(query, intent_data)
