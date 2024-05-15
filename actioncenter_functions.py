import time
import pyautogui
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_internet, check_dark_mode


# Function to show or hide the Action Center
def show_or_hide_action_center(query):
    try:
        if "show action centre" in query:
            # Press the Esc key
            pyautogui.press('esc')
            time.sleep(1)
            # Press the Windows key and hold it, then press the A key
            pyautogui.hotkey('win', 'a')
            # Add a slight delay to ensure the keys are pressed in sequence
            time.sleep(1)
            speak("Action Center opened boss")
        else:
            # Press the Esc key
            pyautogui.press('esc')
            time.sleep(1)
            speak("Action Center closed boss")
    except Exception as e:
        if "show action centre" in query:
            speak("Error opening Action Center")
            speak("Sorry, I couldn't open the Action Center boss")
        else:
            speak("Error closing Action Center")
            speak("Sorry, I couldn't close the Action Center boss")
            pyautogui.press('esc')


# Wi-Fi
# Function to check if Wi-Fi is already on
def is_wifi_on():
    try:
        # Check if the Wi-Fi icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/wifi_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/wifi_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Wi-Fi
def toggle_wifi(query):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        # Check if Wi-Fi is already on
        if "on wi-fi" in query and is_wifi_on():
            speak("Wi-Fi is already on boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Warning message for enabling Wi-Fi
        if "on wi-fi" in query and not is_wifi_on() and check_internet():
            speak(
                "Warning! Enabling Wi-Fi will turn off your current internet connection. Do you want to continue boss?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    break
                else:
                    speak("Wi-Fi not enabled boss.")
                    pyautogui.press('esc')
                    return

        # Check if Wi-Fi is already off
        if "off wi-fi" in query and not is_wifi_on():
            speak("Wi-Fi is already off boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if "on wi-fi" in query:
            # Click on the Wi-Fi mode icon to turn it on
            # Adjust the coordinates based on the location of the Wi-Fi mode icon on your screen
            try:
                if not check_dark_mode():
                    wifi_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/wifi_off.png", confidence=0.9, grayscale=True)
                else:
                    wifi_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/wifi_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(wifi_icon_location)
                speak("Wi-Fi is turned on boss")
            except pyautogui.ImageNotFoundException:
                speak("Wi-Fi icon not found boss")
        else:
            # Click on the Wi-Fi icon to turn it off
            # Adjust the coordinates based on the location of the Wi-Fi icon on your screen
            try:
                if not check_dark_mode():
                    wifi_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/wifi_on.png", confidence=0.9, grayscale=True)
                else:
                    wifi_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/wifi_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(wifi_icon_location)
                speak("Wi-Fi is turned off boss")
            except pyautogui.ImageNotFoundException:
                speak("Wi-Fi icon not found boss")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error toggling Wi-Fi mode")
        if "on wi-fi" in query:
            speak("Sorry, I couldn't turn on Wi-Fi boss")
        else:
            speak("Sorry, I couldn't turn off Wi-Fi boss")
        pyautogui.press('esc')


# Function to show available Wi-Fi networks
def action_center_show_wifi_networks():
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        # Check if Wi-Fi is off
        if not is_wifi_on():
            speak("Wi-Fi is off boss")

            speak("Please note that available Wi-Fi networks won't be visible until Wi-Fi is turned on.")

            # Ask the user whether to turn on Wi-Fi
            speak("Would you like me to turn on Wi-Fi boss?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    pyautogui.press('enter')
                    speak("Wi-Fi is turned on boss")
                    break
                else:
                    speak("Got it boss. I'll leave Wi-Fi as it is.")
                    return

        # Navigate to Wi-Fi networks
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        speak("Available Wi-Fi networks displayed boss")

    except Exception as e:
        # Handle any errors that may occur
        speak("Error displaying Wi-Fi networks")
        speak("Sorry, I couldn't display available Wi-Fi networks boss")
        pyautogui.press('esc')


# Bluetooth
# Function to check if bluetooth is already on
def is_bluetooth_on():
    try:
        # Check if the Bluetooth icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/bluetooth_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/bluetooth_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Bluetooth
def toggle_bluetooth(query):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        # Check if bluetooth is already on
        if "on bluetooth" in query and is_bluetooth_on():
            speak("Bluetooth is already on boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if bluetooth is already off
        if "off bluetooth" in query and not is_bluetooth_on():
            speak("Bluetooth is already off boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if "on bluetooth" in query:
            # Click on the Bluetooth icon to turn it on
            # Adjust the coordinates based on the location of the Bluetooth icon on your screen
            try:
                if not check_dark_mode():
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/bluetooth_off.png", confidence=0.9, grayscale=True)
                else:
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/bluetooth_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(bluetooth_icon_location)
                speak("Bluetooth is turned on boss")
            except pyautogui.ImageNotFoundException:
                speak("Bluetooth icon not found boss")
        else:
            # Click on the Bluetooth icon to turn it off
            # Adjust the coordinates based on the location of the Bluetooth icon on your screen
            try:
                if not check_dark_mode():
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/bluetooth_on.png", confidence=0.9, grayscale=True)
                else:
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/bluetooth_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(bluetooth_icon_location)
                speak("Bluetooth is turned off boss")
            except pyautogui.ImageNotFoundException:
                speak("Bluetooth icon not found boss")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error changing Bluetooth status")
        if "on bluetooth" in query:
            speak("Sorry, I couldn't turned on Bluetooth boss")
        else:
            speak("Sorry, I couldn't turned off Bluetooth boss")
        # Press the Esc key
        pyautogui.press('esc')


# Function show Bluetooth devices
def action_center_show_bluetooth_devices():
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        # Check if bluetooth is off
        if not is_bluetooth_on():
            speak("Bluetooth is off boss")

            speak("Please note that Bluetooth devices won't be visible until Bluetooth is turned on.")

            # Ask the user whether to turn on Bluetooth
            speak("Would you like me to turn on Bluetooth boss?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    pyautogui.press('enter')
                    speak("Bluetooth is turned on boss")
                    break
                else:
                    speak("Got it boss. I'll leave Bluetooth as it is.")
                    return

        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        speak("Bluetooth devices list displayed boss")

    except Exception as e:
        # Handle any errors that may occur
        speak("Error displaying Bluetooth devices")
        speak("Sorry, I couldn't display Bluetooth devices boss")
        pyautogui.press('esc')


# Airplane Mode
# Function to check if airplane mode is already on
def is_airplane_mode_on():
    try:
        # Check if the airplane mode icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/airplane_mode_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/airplane_mode_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off airplane mode
def toggle_airplane_mode(query):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        # Check if airplane mode is already on
        if "on airplane mode" in query and is_airplane_mode_on():
            speak("Airplane mode is already on boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Warning message for enabling airplane mode
        if "on airplane mode" in query and not is_airplane_mode_on():
            speak(
                "Warning! Enabling airplane mode will turn off your current internet connection. Do you want to continue boss?")
            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    break
                else:
                    speak("Airplane mode not enabled boss.")
                    pyautogui.press('esc')
                    return

        # Check if airplane mode is already off
        if "off airplane mode" in query and not is_airplane_mode_on():
            speak("Airplane mode is already off boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if "on airplane mode" in query:
            # Click on the Airplane mode icon to turn it on
            # Adjust the coordinates based on the location of the Airplane mode icon on your screen
            try:
                if not check_dark_mode():
                    airplane_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/airplane_mode_off.png", confidence=0.9, grayscale=True)
                else:
                    airplane_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/airplane_mode_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(airplane_icon_location)
                speak("Airplane mode is turned on boss")
            except pyautogui.ImageNotFoundException:
                speak("Airplane mode icon not found boss")
        else:
            # Click on the Airplane mode icon to turn it off
            # Adjust the coordinates based on the location of the Airplane mode icon on your screen
            try:
                if not check_dark_mode():
                    airplane_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/airplane_mode_on.png", confidence=0.9, grayscale=True)
                else:
                    airplane_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/airplane_mode_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(airplane_icon_location)
                speak("Airplane mode is turned off boss")
            except pyautogui.ImageNotFoundException:
                speak("Airplane mode icon not found boss")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error toggling Airplane mode")
        if "on airplane mode" in query:
            speak("Sorry, I couldn't turn on Airplane mode boss")
        else:
            speak("Sorry, I couldn't turn off Airplane mode boss")
        pyautogui.press('esc')


# Battery Saver
# Function to check if Battery Saver is already on
def is_battery_saver_on():
    try:
        # Check if the Battery Saver icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/battery_saver_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/battery_saver_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to check if Battery is charging
def is_battery_charging():
    try:
        # Check if the Battery Charging icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/battery_charging.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/battery_charging.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred:", e)


# Function to toggle Battery Saver
def toggle_battery_saver(query):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        # Check if Battery Saver is already on
        if is_battery_charging():
            speak("Battery is charging, Battery Saver can not be turn on or off boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if Battery Saver is already off
        if "on battery saver" in query and is_battery_saver_on():
            speak("Battery Saver is already on boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if Battery Saver is already off
        if "off battery saver" in query and not is_battery_saver_on():
            speak("Battery Saver is already off boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if "on battery saver" in query:
            # Click on the Battery Saver icon to turn it on
            # Adjust the coordinates based on the location of the Battery Saver icon on your screen
            try:
                if not check_dark_mode():
                    battery_saver_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/battery_saver_off.png", confidence=0.9, grayscale=True)
                else:
                    battery_saver_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/battery_saver_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(battery_saver_icon_location)
                speak("Battery Saver is turned on boss")
            except pyautogui.ImageNotFoundException:
                speak("Battery Saver icon not found boss")
        else:
            # Click on the Battery Saver icon to turn it off
            # Adjust the coordinates based on the location of the Battery Saver icon on your screen
            try:
                if not check_dark_mode():
                    battery_saver_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/battery_saver_on.png", confidence=0.9, grayscale=True)
                else:
                    battery_saver_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/battery_saver_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(battery_saver_icon_location)
                speak("Battery Saver is turned off boss")
            except pyautogui.ImageNotFoundException:
                speak("Battery Saver icon not found boss")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak(f"Error toggling Battery Saver")
        if "on battery saver" in query:
            speak("Sorry, I couldn't turn on Battery Saver boss")
        else:
            speak("Sorry, I couldn't turn off Battery Saver boss")
        pyautogui.press('esc')


# Night light
# Function to check if Night light is already on
def is_night_light_on():
    try:
        # Check if the Night light icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/night_light_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/night_light_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Night light
def toggle_night_light(query):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        # Check if night light is already on
        if "on night light" in query and is_night_light_on():
            speak("Night light is already on boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if night light is already off
        if "off night light" in query and not is_night_light_on():
            speak("Night light is already off boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if "on night light" in query:
            # Click on the Night light icon to turn it on
            # Adjust the coordinates based on the location of the Night light icon on your screen
            try:
                if not check_dark_mode():
                    night_light_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/night_light_off.png", confidence=0.9, grayscale=True)
                else:
                    night_light_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/night_light_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(night_light_icon_location)
                speak("Night light is turned on boss")
            except pyautogui.ImageNotFoundException:
                speak("Night light icon not found boss")
        else:
            # Click on the Night light icon to turn it off
            # Adjust the coordinates based on the location of the Night light icon on your screen
            try:
                if not check_dark_mode():
                    night_light_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/night_light_on.png", confidence=0.9, grayscale=True)
                else:
                    night_light_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/night_light_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(night_light_icon_location)
                speak("Night light is turned off boss")
            except pyautogui.ImageNotFoundException:
                speak("Night light icon not found boss")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error toggling Night light")
        if "on night light" in query:
            speak("Sorry, I couldn't turn on Night light boss")
        else:
            speak("Sorry, I couldn't turn off Night light boss")
        pyautogui.press('esc')


# Nearby Sharing
# Function to check if Nearby Sharing is already on
def is_nearby_sharing_on():
    try:
        # Check if the Nearby Sharing icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/nearby_sharing_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/nearby_sharing_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Nearby Sharing
def toggle_nearby_sharing(query):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        # Check if nearby sharing is already on
        if ("on nearby share" in query or "on nearby sharing" in query) and is_nearby_sharing_on():
            speak("Nearby sharing is already on boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if nearby sharing is already off
        if ("off nearby share" in query or "off nearby sharing" in query) and not is_nearby_sharing_on():
            speak("Nearby sharing is already off boss")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if "on nearby share" in query or "on nearby sharing" in query:
            # Click on the nearby sharing icon to turn it on
            # Adjust the coordinates based on the location of the nearby sharing icon on your screen
            try:
                if not check_dark_mode():
                    nearby_sharing_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/nearby_sharing_off.png",
                        confidence=0.9, grayscale=True)
                else:
                    nearby_sharing_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/nearby_sharing_off.png",
                        confidence=0.9, grayscale=True)
                pyautogui.click(nearby_sharing_icon_location)
                speak("Nearby sharing is turned on boss")
            except pyautogui.ImageNotFoundException:
                speak("Nearby sharing icon not found boss")
        else:
            # Click on the nearby sharing icon to turn it off
            # Adjust the coordinates based on the location of the nearby sharing icon on your screen
            try:
                if not check_dark_mode():
                    nearby_sharing_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/nearby_sharing_on.png",
                        confidence=0.9, grayscale=True)
                else:
                    nearby_sharing_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/nearby_sharing_on.png",
                        confidence=0.9, grayscale=True)
                pyautogui.click(nearby_sharing_icon_location)
                speak("Nearby sharing is turned off boss")
            except pyautogui.ImageNotFoundException:
                speak("Nearby sharing icon not found boss")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error toggling Nearby sharing")
        if "on nearby share" in query or "on nearby sharing" in query:
            speak("Sorry, I couldn't turn on Nearby sharing boss")
        else:
            speak("Sorry, I couldn't turn off Nearby sharing boss")
        pyautogui.press('esc')
