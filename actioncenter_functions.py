import time
import wmi
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
            print("Sam: Opening Action Center sir.")
            speak("Opening Action Center sir")
        else:
            print("Sam: Closing Action Center sir.")
            speak("Closing Action Center sir")
    except Exception as e:
        if "show action centre" in query:
            print(f"Sam: Error opening Action Center: {e}")
            speak("Sorry, I couldn't open the Action Center sir.")
        else:
            print(f"Sam: Error closing Action Center: {e}")
            speak("Sam: Sorry, I couldn't close the Action Center sir.")
            speak("Sorry, I couldn't close the Action Center sir.")


# Function to check if Bluetooth is already on
def is_bluetooth_on():
    try:
        # Connect to the WMI service
        c = wmi.WMI()
        # Query for the status of Bluetooth services
        bt_services = c.Win32_Service(Name="bthserv")
        for service in bt_services:
            # Check if the Bluetooth service is running
            if service.State == "Running":
                return True
    except Exception as e:
        print(f"Error checking Bluetooth status: {e}")
    return False


# Function to turn on or off Bluetooth
def turn_on_or_off_bluetooth(query):
    try:
        # Check the current state of Bluetooth
        bluetooth_on = is_bluetooth_on()

        # If the query is to turn on Bluetooth and it's already on
        if "on bluetooth" in query and bluetooth_on:
            print("Sam: Bluetooth is already on sir.")
            speak("Bluetooth is already on sir.")
            return

        # If the query is to turn off Bluetooth and it's already off
        if "off bluetooth" in query and not bluetooth_on:
            print("Sam: Bluetooth is already off sir.")
            speak("Bluetooth is already off sir.")
            return

        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        # Provide feedback based on the query
        if "on bluetooth" in query:
            print("Sam: Bluetooth turned on, sir.")
            speak("Bluetooth turned on sir.")
        else:
            print("Sam: Bluetooth turned off, sir.")
            speak("Bluetooth turned off sir.")

    except Exception as e:
        # Handle any errors that may occur
        if "on bluetooth" in query:
            print(f"Error turning on Bluetooth: {e}")
            print("Sam: Sorry, I couldn't turn on Bluetooth, sir.")
            speak("Sorry, I couldn't turn on Bluetooth sir.")
        else:
            print(f"Error turning off Bluetooth: {e}")
            print("Sam: Sorry, I couldn't turn off Bluetooth, sir.")
            speak("Sorry, I couldn't turn off Bluetooth sir.")
