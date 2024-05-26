import time
import pyautogui
from sam_functions.speak import speak
from app_functions import open_application


def open_settings(query, intent_data):
    try:
        settings_query = None

        for prep in intent_data['text']:
            if prep in query:
                # Extract setting from the query based on the preposition
                parts = query.split(prep)
                if len(parts) > 1:
                    settings_query = parts[1].strip()
                break

        # Check if 'settings_query' is extracted and if it contains "setting" or "settings"
        if settings_query:
            # Remove "setting" or "settings" if present in the extracted query
            settings_query = settings_query.replace("settings", "").replace("setting", "").strip()

        # If there is no specific setting to open, open the Settings app directly
        if not settings_query:
            open_application("open settings", {
                "intent": "open_application",
                "text": [
                    "open application",
                    "open app",
                    "open the",
                    "open",
                    "launch application",
                    "launch app",
                    "launch the",
                    "launch",
                    "start application",
                    "start app",
                    "start the",
                    "start",
                    "run application",
                    "run app",
                    "run the",
                    "run",
                    "fire up application",
                    "fire up app",
                    "fire up the",
                    "fire up",
                    "begin application",
                    "begin app",
                    "begin the",
                    "begin",
                    "activate application",
                    "activate app",
                    "activate the",
                    "activate",
                    "initiate application",
                    "initiate app",
                    "initiate the",
                    "initiate",
                    "commence application",
                    "commence app",
                    "commence the",
                    "commence"
                ],
                "responses": [],
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "",
                "entities": []
            })
            return

        # List of possible settings to open
        settings_options = ["display", "brightness", "night light", "hdr", "resolution", "orientation",
                            "volume", "bluetooth", "printer", "mobile device", "manage cameras", "mouse",
                            "touchpad", "pen and windows", "autoplay", "usb", "wi-fi", "ethernet", "vpn",
                            "hotspot", "airplane mode", "proxy", "background", "light mode", "dark mode",
                            "themes", "change lighting colours, brightness, and effects", "lock screen",
                            "text input", "start settings", "taskbar", "font settings", "data usage",
                            "installed apps", "advanced app settings", "default apps", "offline maps",
                            "video playback", "startup apps", "account info", "sign-in options",
                            "email and accounts", "family options", "other users", "back up",
                            "access work or school", "passkey", "date", "date and time", "time", "language",
                            "typing", "speech settings", "game mode", "game bar settings", "captures",
                            "text size", "visual effects", "mouse pointer and touch", "text cursor",
                            "magnifier settings", "contrast", "narrator settings", "caption styles",
                            "speech settings", "accessibility audio settings", "eye control", "privacy settings",
                            "find my device", "windows update", "advanced display", "graphics", "sync settings"]

        # Check if the query matches any of the settings options
        if settings_query in settings_options:
            try:
                pyautogui.press('win')
                time.sleep(0.2)

                pyautogui.typewrite(settings_query)
                time.sleep(0.2)

                pyautogui.press('enter')
                time.sleep(2)

                # Inform the user that the settings are being opened
                speak(f"Opening the {settings_query} settings sir.")

            except Exception as e:
                speak(f"Error")
                speak(f"Sorry sir. I encountered an issue while opening the {settings_query} settings.")
        else:
            speak(f"Sorry, I couldn't find any setting sir.")

    except Exception as e:
        # Handle any other errors that might occur
        speak("An error occurred")
        speak("Oops! Something went wrong while pressing the keyboard key sir.")
