import time
import pyautogui
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_dark_mode


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
            print("Sam: Action Center opened, sir")
            speak("Action Center opened sir")
        else:
            # Press the Esc key
            pyautogui.press('esc')
            time.sleep(1)
            print("Sam: Action Center, sir")
            speak("Action Center closed sir")
    except Exception as e:
        if "show action centre" in query:
            print(f"Sam: Error opening Action Center: {e}")
            print("Sorry, I couldn't open the Action Center, sir")
            speak("Sorry, I couldn't open the Action Center sir")
        else:
            print(f"Sam: Error closing Action Center: {e}")
            print("Sam: Sorry, I couldn't close the Action Center, sir")
            speak("Sorry, I couldn't close the Action Center sir")
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
        print("Sam: An error occurred:", e)


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
            print("Sam: Wi-Fi is off, sir")
            speak("Wi-Fi is off sir")

            print("Sam: Please note that available Wi-Fi networks won't be visible until Wi-Fi is turned on.")
            speak("Please note that available Wi-Fi networks won't be visible until Wi-Fi is turned on.")

            # Ask the user whether to turn on Wi-Fi
            print("Sam: Would you like me to turn on Wi-Fi, sir?")
            speak("Would you like me to turn on Wi-Fi sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    pyautogui.press('enter')
                    print("Sam: Wi-Fi is turned on, sir")
                    speak("Wi-Fi is turned on sir")
                    break
                else:
                    print("Sam: Got it, sir. I'll leave Wi-Fi as it is.")
                    speak("Got it sir. I'll leave Wi-Fi as it is")
                    return

        # Navigate to Wi-Fi networks
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        print("Sam: Available Wi-Fi networks displayed, sir")
        speak("Available Wi-Fi networks displayed sir")

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error displaying Wi-Fi networks: {e}")
        print("Sam: Sorry, I couldn't display available Wi-Fi networks, sir")
        speak("Sorry, I couldn't display available Wi-Fi networks sir")
        pyautogui.press('esc')

# Bluetooth
# Function to check if bluetooth is already on
def is_bluetooth_on():
    try:
        # Check if the Bluetooth icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/toggle_off.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/toggle_off.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        print("Sam: An error occurred:", e)


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
            print("Sam: Bluetooth is already on, sir")
            speak("Bluetooth is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if bluetooth is already off
        if "off bluetooth" in query and not is_bluetooth_on():
            print("Sam: Bluetooth is already off, sir")
            speak("Bluetooth is already off sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if "on bluetooth" in query:
            # Click on the Bluetooth icon to turn it on
            # Adjust the coordinates based on the location of the Bluetooth icon on your screen
            try:
                if not check_dark_mode():
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/toggle_on.png", confidence=0.9, grayscale=True)
                else:
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/toggle_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(bluetooth_icon_location)
                print("Sam: Bluetooth is turned on, sir")
                speak("Bluetooth is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Bluetooth icon not found, sir")
                speak("Bluetooth icon not found sir")
        else:
            # Click on the Bluetooth icon to turn it off
            # Adjust the coordinates based on the location of the Bluetooth icon on your screen
            try:
                if not check_dark_mode():
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/action_center/toggle_off.png", confidence=0.9, grayscale=True)
                else:
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/action_center/toggle_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(bluetooth_icon_location)
                print("Sam: Bluetooth is turned off, sir")
                speak("Bluetooth is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Bluetooth icon not found, sir")
                speak("Bluetooth icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Bluetooth status: {e}")
        if "on bluetooth" in query:
            print("Sam: Sorry, I couldn't turned on Bluetooth, sir")
            speak("Sorry, I couldn't turned on Bluetooth sir")
        else:
            print("Sam: Sorry, I couldn't turned off Bluetooth, sir")
            speak("Sorry, I couldn't turned off Bluetooth sir")
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
            print("Sam: Bluetooth is off, sir")
            speak("Bluetooth is off sir")

            print("Sam: Please note that Bluetooth devices won't be visible until Bluetooth is turned on.")
            speak("Please note that Bluetooth devices won't be visible until Bluetooth is turned on.")

            # Ask the user whether to turn on Bluetooth
            print("Sam: Would you like me to turn on Bluetooth, sir?")
            speak("Would you like me to turn on Bluetooth sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    pyautogui.press('enter')
                    print("Sam: Bluetooth is turned on, sir")
                    speak("Bluetooth is turned on sir")
                    break
                else:
                    print("Sam: Got it, sir. I'll leave Bluetooth as it is.")
                    speak("Got it sir. I'll leave Bluetooth as it is")
                    return

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
        print("Sam: An error occurred:", e)


# Function to turn on or off airplane mode
def toggle_airplane_mode(query):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        # Warning message for enabling airplane mode
        if "on airplane mode" in query and not is_airplane_mode_on():
            print(
                "Sam: Warning! Enabling airplane mode will turn off your current internet connection. Do you want to continue, sir?")
            speak(
                "Warning! Enabling airplane mode will turn off your current internet connection. Do you want to continue sir?")
            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    break
                else:
                    print("Sam: Airplane mode not enabled, sir.")
                    speak("Airplane mode not enabled sir.")
                    pyautogui.press('esc')
                    return

        # Check if airplane mode is already on
        if "on airplane mode" in query and is_airplane_mode_on():
            print("Sam: Airplane mode is already on, sir")
            speak("Airplane mode is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if airplane mode is already off
        if "off airplane mode" in query and not is_airplane_mode_on():
            print("Sam: Airplane mode is already off, sir")
            speak("Airplane mode is already off sir")
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
                print("Sam: Airplane mode is turned on, sir")
                speak("Airplane mode is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Airplane mode icon not found, sir")
                speak("Airplane mode icon not found sir")
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
                print("Sam: Airplane mode is turned off, sir")
                speak("Airplane mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Airplane mode icon not found, sir")
                speak("Airplane mode icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error toggling Airplane mode: {e}")
        if "on airplane mode" in query:
            print("Sam: Sorry, I couldn't turn on Airplane mode, sir")
            speak("Sorry, I couldn't turn on Airplane mode sir")
        else:
            print("Sam: Sorry, I couldn't turn off Airplane mode, sir")
            speak("Sorry, I couldn't turn off Airplane mode sir")
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
        print("Sam: An error occurred:", e)


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
        print("Sam: An error occurred:", e)


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
            print("Sam: Battery is charging, Battery Saver can not be turn on or off, sir")
            speak("Battery is charging, Battery Saver can not be turn on or off sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if Battery Saver is already off
        if "on battery saver" in query and is_battery_saver_on():
            print("Sam: Battery Saver is already on, sir")
            speak("Battery Saver is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if Battery Saver is already off
        if "off battery saver" in query and not is_battery_saver_on():
            print("Sam: Battery Saver is already off, sir")
            speak("Battery Saver is already off sir")
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
                print("Sam: Battery Saver is turned on, sir")
                speak("Battery Saver is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Battery Saver icon not found, sir")
                speak("Battery Saver icon not found sir")
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
                print("Sam: Battery Saver is turned off, sir")
                speak("Battery Saver is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Battery Saver icon not found, sir")
                speak("Battery Saver icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error toggling Battery Saver: {e}")
        if "on battery saver" in query:
            print("Sam: Sorry, I couldn't turn on Battery Saver, sir")
            speak("Sorry, I couldn't turn on Battery Saver sir")
        else:
            print("Sam: Sorry, I couldn't turn off Battery Saver, sir")
            speak("Sorry, I couldn't turn off Battery Saver sir")
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
        print("Sam: An error occurred:", e)


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
            print("Sam: Night light is already on, sir")
            speak("Night light is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if night light is already off
        if "off night light" in query and not is_night_light_on():
            print("Sam: Night light is already off, sir")
            speak("Night light is already off sir")
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
                print("Sam: Night light is turned on, sir")
                speak("Night light is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Night light icon not found, sir")
                speak("Night light icon not found sir")
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
                print("Sam: Night light is turned off, sir")
                speak("Night light is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Night light icon not found, sir")
                speak("Night light icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error toggling Night light: {e}")
        if "on night light" in query:
            print("Sam: Sorry, I couldn't turn on Night light, sir")
            speak("Sorry, I couldn't turn on Night light sir")
        else:
            print("Sam: Sorry, I couldn't turn off Night light, sir")
            speak("Sorry, I couldn't turn off Night light sir")
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
        print("Sam: An error occurred:", e)


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
        if "on nearby sharing" in query and is_nearby_sharing_on():
            print("Sam: Nearby sharing is already on, sir")
            speak("Nearby sharing is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if nearby sharing is already off
        if "off nearby sharing" in query and not is_nearby_sharing_on():
            print("Sam: Nearby sharing is already off, sir")
            speak("Nearby sharing is already off sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if "on nearby sharing" in query:
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
                print("Sam: Nearby sharing is turned on, sir")
                speak("Nearby sharing is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Nearby sharing icon not found, sir")
                speak("Nearby sharing icon not found sir")
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
                print("Sam: Nearby sharing is turned off, sir")
                speak("Nearby sharing is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Nearby sharing icon not found, sir")
                speak("Nearby sharing icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error toggling Nearby sharing: {e}")
        if "on nearby sharing" in query:
            print("Sam: Sorry, I couldn't turn on Nearby sharing, sir")
            speak("Sorry, I couldn't turn on Nearby sharing sir")
        else:
            print("Sam: Sorry, I couldn't turn off Nearby sharing, sir")
            speak("Sorry, I couldn't turn off Nearby sharing sir")
        pyautogui.press('esc')
