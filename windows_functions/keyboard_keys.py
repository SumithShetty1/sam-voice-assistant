import time
import pyautogui
from sam_functions.speak import speak

# Define a dictionary to map spoken key names to their corresponding keys
key_mapping = {
    "page down": "pagedown",
    "page up": "pageup",
    "left arrow": "left",
    "right arrow": "right",
    "up arrow": "up",
    "down arrow": "down",
    "backspace": "backspace",
    "tab": "tab",
    "enter": "enter",
    "pause": "pause",
    "caps lock": "capslock",
    "escape": "esc",
    "space": "space",
    "end": "end",
    "home": "home",
    "insert": "insert",
    "delete": "delete",
    "f1": "f1",
    "f2": "f2",
    "f3": "f3",
    "f4": "f4",
    "f5": "f5",
    "f6": "f6",
    "f7": "f7",
    "f8": "f8",
    "f9": "f9",
    "f10": "f10",
    "f11": "f11",
    "f12": "f12",
    "print screen": "printscreen",
    "scroll lock": "scrolllock",
    "num lock": "numlock",
    "left windows key": "winleft",
    "right windows key": "winright",
    "apps key": "appskey",
    "volume up": "volumeup",
    "volume down": "volumedown",
    "volume mute": "volumemute",
    "media next": "medianext",
    "media previous": "mediaprev",
    "media stop": "mediastop",
    "media play pause": "mediaplaypause"
}


# Function to perform various keyboard shortcuts and actions based on the provided query
def keyboard_keys(query, intent_data):
    try:
        key = None

        # Loop through each preposition pattern
        for prep in intent_data['text']:
            if prep in query:
                # Extract key from the query based on the preposition
                parts = query.split(prep)
                if len(parts) > 1:
                    key = parts[1].strip()
                break

        # Check if 'key' is extracted and if it contains "key" or "button"
        if key:
            # Remove "key" or "button" if present in the extracted key
            key = key.replace("key", "").replace("button", "").strip()

        # If there is no specific setting to open, open the Settings app directly
        if not key:
            # Handle the case where the query is not properly formatted
            speak("Please provide a valid query to press a keyboard key sir.")
            return

        # Check if the key is valid
        if key in key_mapping:
            try:
                # Simulate pressing the key
                pyautogui.press(key_mapping[key])
                time.sleep(0.2)

                # Inform the user that the key has been pressed
                speak(f"{key} key pressed sir.")

            except Exception as e:
                speak("Error")
                speak(f"Sorry sir. I encountered an issue while pressing the {key} key sir.")
        else:
            speak(f"Sorry, it is not a valid key sir.")

    except Exception as e:
        # Handle any other errors that might occur
        speak("An error occurred")
        speak("Oops! Something went wrong while pressing the keyboard key sir.")
