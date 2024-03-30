import time
import pyautogui  # https://pypi.org/project/PyAutoGUI/
from sam_functions import speak


# Function to show or hide the Action Center
def show_or_hide_action_center(query):
    try:
        # Press the Windows key and hold it, then press the A key
        pyautogui.hotkey('win', 'a')
        # Add a slight delay to ensure the keys are pressed in sequence
        time.sleep(1)
        if "show action centre" in query:
            print("Sam: Opening Action Center, sir")
            speak("Opening Action Center sir")
        else:
            print("Sam: Closing Action Center, sir")
            speak("Closing Action Center sir")
    except Exception as e:
        if "show action centre" in query:
            print(f"Sam: Error opening Action Center: {e}")
            print("Sorry, I couldn't open the Action Center, sir")
            speak("Sorry, I couldn't open the Action Center sir")
        else:
            print(f"Sam: Error closing Action Center: {e}")
            print("Sam: Sorry, I couldn't close the Action Center, sir")
            speak("Sorry, I couldn't close the Action Center sir")


# Function to turn on or off Bluetooth
def turn_on_or_off_bluetooth():
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        print("Sam: Bluetooth status changed, sir")
        speak("Bluetooth status changed sir")

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Bluetooth status: {e}")
        print("Sam: Sorry, I couldn't change Bluetooth status, sir")
        speak("Sorry, I couldn't change Bluetooth status sir")


# Function show Bluetooth devices
def show_bluetooth_devices():
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        print("Sam: Bluetooth devices list displayed, sir")
        speak("Bluetooth devices list displayed sir")

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error displaying Bluetooth devices: {e}")
        print("Sam: Sorry, I couldn't display Bluetooth devices, sir")
        speak("Sorry, I couldn't display Bluetooth devices sir")


# Function to turn on or off airplane mode
def turn_on_or_off_airplane_mode(query):
    try:
        # Warning message for enabling airplane mode
        if "on airplane mode" in query:
            print("Sam: Warning! Enabling airplane mode will turn off your current internet connection, sir")
            speak("Warning! Enabling airplane mode will turn off your current internet connection sir")

        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        print("Sam: Airplane mode status changed, sir")
        speak("Airplane mode status changed sir")

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Airplane mode status: {e}")
        print("Sam: Sorry, I couldn't change Airplane mode status, sir")
        speak("Sorry, I couldn't change Airplane mode status sir")


# Function to turn on or off Battery Saver
def turn_on_or_off_battery_saver():
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        print("Sam: Battery saver status changed, sir")
        speak("Battery saver status changed sir")

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing battery saver status: {e}")
        print("Sam: Sorry, I couldn't change battery saver status, sir")
        speak("Sorry, I couldn't change battery saver status sir")


# Function to turn on or off Night light
def turn_on_or_off_night_light():
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        print("Sam: Night light mode status changed, sir")
        speak("Night light mode status changed sir")

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error toggling night light mode: {e}")
        print("Sam: Sorry, I couldn't change night light mode status, sir")
        speak("Sorry, I couldn't change night light mode status sir")


# Function to turn on or off Nearby Sharing
def turn_on_or_off_nearby_sharing():
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        print("Sam: Nearby sharing status changed, sir")
        speak("Nearby sharing status changed sir")

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error toggling nearby sharing: {e}")
        print("Sam: Sorry, I couldn't change nearby sharing mode status, sir")
        speak("Sorry, I couldn't change nearby sharing status sir")
