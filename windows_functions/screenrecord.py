import time
import pyautogui
from sam_functions.speak import speak


def record_screen_windows():
    try:
        speak("I'm about to start recording. Please feel free to stop the recording whenever you need sir.")

        # Start screen recording using Windows shortcut
        pyautogui.hotkey('win', 'alt', 'r')

    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to start recording sir.")


# Function to screenrecord using the Snipping Tool
def record_snipping():
    try:
        # Open the Snipping Tool
        pyautogui.hotkey('win', 'shift', 's')
        time.sleep(1)
        pyautogui.press('space')
        time.sleep(0.2)

        # Instruct the user to use the Snipping Tool to select the area to capture
        speak("Please use the Snipping tool to select the area you'd like to record sir.")
    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to record the screen sir.")


# Function to handle screenshot requests
def screenrecord(intent_data):
    if intent_data['intent'] == "snipping_tool_screen_record":
        record_snipping()
    else:
        record_screen_windows()
