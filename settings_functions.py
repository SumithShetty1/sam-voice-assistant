import time
import pyautogui
from sam_functions import speak, takeCommand
from check_functions import check_dark_mode, check_settings_opening

q = "on bluetooth"


# Function to check if bluetooth is already on
def is_bluetooth_on():
    try:
        # Check if the Bluetooth icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/settings/bluetooth_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/settings/bluetooth_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        print("Sam: An error occurred:", e)


# Function to turn on or off Bluetooth
def enable_or_disable_bluetooth(query):
    try:
        # Press keys to open Action Center
        pyautogui.hotkey('win')
        pyautogui.typewrite('Bluetooth')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # Check for the settings app continuously for 10 seconds
        if check_settings_opening():
            # Settings opening found, proceed with the operation
            pass
        else:
            # Settings app not found within 10 seconds, ask the user whether to continue waiting or exit
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = takeCommand()
                if confirm is None:
                    continue
                if confirm == 'yes':
                    if not check_settings_opening():
                        if "on bluetooth" in query:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn on Bluetooth")
                            speak("The settings app is still taking time to open. Please manually turn on Bluetooth")
                            return
                        else:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn off Bluetooth")
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Bluetooth")
                            return

                else:
                    print("Sam: Closing settings, sir")
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        # Check if bluetooth is already on
        if "on bluetooth" in query and is_bluetooth_on():
            print("Sam: Bluetooth is already on, sir")
            speak("Bluetooth is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Check if bluetooth is already off
        if "off bluetooth" in query and not is_bluetooth_on():
            print("Sam: Bluetooth is already off, sir")
            speak("Bluetooth is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if "on bluetooth" in query:
            # Click on the Bluetooth icon to turn it on
            # Adjust the coordinates based on the location of the Bluetooth icon on your screen
            try:
                if not check_dark_mode():
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/bluetooth_off.png", confidence=0.9, grayscale=True)
                else:
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/bluetooth_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(bluetooth_icon_location)
                print("Sam: Bluetooth is turned on, sir")
                speak("Bluetooth is turned on sir")
                pyautogui.hotkey('alt', 'f4')
            except pyautogui.ImageNotFoundException:
                print("Sam: Bluetooth icon not found, sir")
                speak("Bluetooth icon not found sir")
                pyautogui.hotkey('alt', 'f4')
        else:
            # Click on the Bluetooth icon to turn it off
            # Adjust the coordinates based on the location of the Bluetooth icon on your screen
            try:
                if not check_dark_mode():
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/bluetooth_on.png", confidence=0.9, grayscale=True)
                else:
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/bluetooth_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(bluetooth_icon_location)
                print("Sam: Bluetooth is turned off, sir")
                speak("Bluetooth is turned off sir")
                pyautogui.hotkey('alt', 'f4')
            except pyautogui.ImageNotFoundException:
                print("Sam: Bluetooth icon not found, sir")
                speak("Bluetooth icon not found sir")
                pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Bluetooth status: {e}")
        if "on bluetooth" in query:
            print("Sam: Sorry, I couldn't turn on Bluetooth, sir")
            speak("Sorry, I couldn't turn on Bluetooth sir")
            pyautogui.hotkey('alt', 'f4')
        else:
            print("Sam: Sorry, I couldn't turn off Bluetooth, sir")
            speak("Sorry, I couldn't turn off Bluetooth sir")
            pyautogui.hotkey('alt', 'f4')


enable_or_disable_bluetooth(q)
