import time
import pyautogui
from sam_functions.speak import speak
from app_functions import open_application


def open_settings(query):
    try:
        # Extract the settings query
        if "open settings" in query:
            settings_query = query.split("open settings ")[1]
        else:
            settings_query = query.split("open setting ")[1]

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
                speak(f"Opening the {settings_query} settings, boss.")

            except Exception as e:
                speak(f"Error")
                speak(f"Sorry, boss. I encountered an issue while opening the {settings_query} settings.")
        else:
            speak(f"Sorry, I couldn't find any settings named {settings_query}, boss.")

    except IndexError:
        # If there is no additional text after "open settings", open the Settings app directly
        open_application("open settings")
