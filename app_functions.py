from sam_functions.speak import speak
from AppOpener import open, close
import pyautogui


# Function to open applications
def open_application(query):
    try:
        # Extracting the application name from the query
        app = query.split("open ")[1]
        try:
            # Attempting to open the specified application
            open(app, throw_error=True, match_closest=True)
            speak(f"Opening {app}, boss")

        except Exception as e:
            speak("Error")
            speak(f"Sorry, I couldn't find an application named {app}, boss")
    except IndexError:
        speak("Please specify the application to open, boss")


# Function to close applications
def close_application(query):
    try:
        # Extracting the application name from the query
        app = query.split("close ")[1]
        try:
            # Attempting to close the specified application
            close(app, throw_error=True, match_closest=False)
            speak(f"{app} closed, boss")
        except Exception as e:
            speak("Error")
            speak(f"Sorry, I couldn't close an application named {app}, boss")
    except IndexError:
        speak("Please specify the application to close,, boss")


# Function to close the current window
def close_window():
    try:
        # Simulating Alt + F4 key press to close the current window
        pyautogui.hotkey('alt', 'f4')
        speak(f"Current window close, boss")
    except Exception as e:
        speak("Error")
        speak(f"Sorry, I couldn't find or close the current window, boss")
