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
            print(f"Sam: Opening {app}, sir")
            speak(f"Opening {app} sir")
        except Exception as e:
            print(f"Error: {e}")
            print(f"Sam: Sorry, I couldn't find an application named {app}, sir")
            speak(f"Sorry, I couldn't find an application named {app} sir")
    except IndexError:
        print("Sam: Please specify the application to open, sir")
        speak("Please specify the application to open sir")


# Function to close applications
def close_application(query):
    try:
        # Extracting the application name from the query
        app = query.split("close ")[1]
        try:
            # Attempting to close the specified application
            close(app, throw_error=True, match_closest=False)
            print(f"Sam: {app} closed, sir")
            speak(f"{app} closed sir")
        except Exception as e:
            print(e)
            print(f"Sam: Sorry, I couldn't close an application named {app}, sir")
            speak(f"Sorry, I couldn't close an application named {app} sir")
    except IndexError:
        print("Sam: Please specify the application to close,, sir")
        speak("Please specify the application to close sir")


# Function to close the current window
def close_window():
    try:
        # Simulating Alt + F4 key press to close the current window
        pyautogui.hotkey('alt', 'f4')
        print(f"Sam: Current window close, sir")
        speak(f"Current window close sir")
    except Exception as e:
        print(e)
        print(f"Sam: Sorry, I couldn't find or close the current window, sir")
        speak(f"Sorry, I couldn't close the current window sir")
