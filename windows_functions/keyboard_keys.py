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
def keyboard_keys(query):
    try:
        key = query.split("press ")[1]

        # Check if the key is valid
        if key in key_mapping:
            try:
                # Simulate pressing the key
                pyautogui.press(key_mapping[key])
                time.sleep(0.2)

                # Inform the user that the key has been pressed
                print(f"Sam: {key} key pressed, sir.")
                speak(f"{key} key pressed sir")

            except Exception as e:
                print(f"Sam: Error: {e}")
                print(f"Sam: Sorry, sir. I encountered an issue while pressing the {key} key, sir.")
                speak(f"Sorry sir. I encountered an issue while pressing the {key} key sir")
        else:
            print(f"Sam: Sorry, {key} is not a valid key, sir.")
            speak(f"Sorry {key} is not a valid key sir")

    except IndexError:
        # Handle the case where the query is not properly formatted
        print("Sam: Please provide a valid query to press a keyboard key, sir.")
        speak("Please provide a valid query to press a keyboard key sir")
    except Exception as e:
        # Handle any other errors that might occur
        print(f"Sam: An error occurred: {e}")
        print("Sam: Oops! Something went wrong while pressing the keyboard key, sir.")
        speak("Oops! Something went wrong while pressing the keyboard key sir")
