import time
import requests
import darkdetect
import pyautogui


# Function to check internet connectivity
def check_internet():
    try:
        requests.get('http://www.google.com', timeout=3)  # Attempt to make a request to Google
        return True
    except requests.ConnectionError:
        return False


# Function to check if the system is in dark mode
def check_dark_mode():
    theme = darkdetect.theme()
    if theme == 'Dark':
        return True
    else:
        return False


# Function to check for the presence of the settings icon within a specified duration
def check_settings_opening():
    duration = 10
    start_time = time.time()
    while time.time() - start_time < duration:
        # Check if the settings icon is present on the screen
        try:
            if not check_dark_mode():
                if pyautogui.locateOnScreen("images/light_mode/settings/settings_icon.png", confidence=0.9):
                    pass
            else:
                if pyautogui.locateOnScreen("images/dark_mode/settings/settings_icon.png", confidence=0.9):
                    pass

        except pyautogui.ImageNotFoundException:
            return True
    # If settings app is not found within the specified duration, return False
    return False


# Function to check if the current window is maximized
def check_window_maximized():
    try:
        # Check if the Airplane Mode icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/window/window_maximized.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/window/window_maximized.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        print("Sam: An error occurred:", e)
