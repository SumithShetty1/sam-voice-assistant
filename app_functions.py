from sam_functions.speak import speak
from AppOpener import open, close
import pyautogui


# Function to open applications
def open_application(query, intent_data):
    try:
        app = None

        for prep in intent_data['text']:
            if prep in query:
                # Extract app from the query based on the preposition
                parts = query.split(prep)
                if len(parts) > 1:
                    app = parts[1].strip()
                break

        # Check if 'app' is extracted and if it contains "app" or "application"
        if app:
            # Remove "setting" or "settings" if present in the extracted query
            app = app.replace("app", "").replace("application", "").strip()

        # If there is no specific app to close, then return
        if not app:
            speak("Please specify the application to open sir")
            return

        try:
            # Attempting to open the specified application
            open(app, throw_error=True, match_closest=True)
            speak(f"Opening {app} sir")

        except Exception as e:
            speak("Error")
            speak(f"Sorry, I couldn't find an application named {app} sir")
    except Exception as e:
        # Handle any other errors that might occur
        speak("An error occurred")
        speak("Oops! Something went wrong while opening sir.")


# Function to close applications
def close_application(query, intent_data):
    try:
        app = None

        for prep in intent_data['text']:
            if prep in query:
                # Extract app from the query based on the preposition
                parts = query.split(prep)
                if len(parts) > 1:
                    app = parts[1].strip()
                break

        # Check if 'app' is extracted and if it contains "app" or "application"
        if app:
            # Remove "setting" or "settings" if present in the extracted query
            app = app.replace("app", "").replace("application", "").strip()

        # If there is no specific app to close, then return
        if not app:
            speak("Please specify the application to close sir")
            return

        try:
            # Attempting to close the specified application
            close(app, throw_error=True, match_closest=False)
            speak(f"{app} closed sir")
        except Exception as e:
            speak("Error")
            speak(f"Sorry, I couldn't close an application named {app} sir")
    except Exception as e:
        # Handle any other errors that might occur
        speak("An error occurred")
        speak("Oops! Something went wrong while closing sir.")


# Function to close the current window
def close_window():
    try:
        # Simulating Alt + F4 key press to close the current window
        pyautogui.hotkey('alt', 'f4')
        speak(f"Current window close sir")
    except Exception as e:
        speak("Error")
        speak(f"Sorry, I couldn't find or close the current window sir")
