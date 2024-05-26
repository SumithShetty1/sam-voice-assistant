import time
import pyautogui
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_internet, check_dark_mode
from settings_functions import enable_or_disable_bluetooth, settings_show_bluetooth_devices, enable_or_disable_airplane_mode, enable_or_disable_night_light, enable_or_disable_nearby_share, enable_or_disable_wifi, settings_show_wifi_networks
import eel
from intent_detect.load_model import recognize_intent


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


# Function to check if bluetooth is already off
def is_bluetooth_off():
    try:
        # Check if the Bluetooth icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/bluetooth_off.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/bluetooth_off.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Bluetooth
def turn_on_or_off_bluetooth(intent_data):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        if not is_bluetooth_on() and not is_bluetooth_off():
            pyautogui.press('esc')
            time.sleep(1)
            enable_or_disable_bluetooth(intent_data)
            return

        # Check if bluetooth is already on
        if intent_data['intent'] == "on_bluetooth" and is_bluetooth_on():
            speak("Bluetooth is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if bluetooth is already off
        if intent_data['intent'] == "off_bluetooth" and is_bluetooth_off():
            speak("Bluetooth is already off sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if intent_data['intent'] == "on_bluetooth":
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
                speak("Bluetooth is turned on sir")
            except pyautogui.ImageNotFoundException:
                speak("Bluetooth icon not found sir")
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
                speak("Bluetooth is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Bluetooth icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error changing Bluetooth status")
        if intent_data['intent'] == "on_bluetooth":
            speak("Sorry, I couldn't turned on Bluetooth sir")
        else:
            speak("Sorry, I couldn't turned off Bluetooth sir")
        # Press the Esc key
        pyautogui.press('esc')


# Function show Bluetooth devices
def show_bluetooth_devices():
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        if not is_bluetooth_on() and not is_bluetooth_off():
            pyautogui.press('esc')
            time.sleep(1)
            settings_show_bluetooth_devices()
            return

        pyautogui.press('right')
        time.sleep(1)
        # Check if bluetooth is off
        if not is_bluetooth_on():
            speak("Bluetooth is off sir")

            speak("Please note that Bluetooth devices won't be visible until Bluetooth is turned on.")

            # Ask the user whether to turn on Bluetooth
            speak("Would you like me to turn on Bluetooth sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Got it sir. I'll leave Bluetooth as it is.")
                    return
                elif confirm['intent'] == "yes":
                    pyautogui.press('enter')
                    speak("Bluetooth is turned on sir")
                    break
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        speak("Bluetooth devices list displayed sir")

    except Exception as e:
        # Handle any errors that may occur
        speak("Error displaying Bluetooth devices")
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
        speak("An error occurred")


# Function to check if airplane mode is already off
def is_airplane_mode_off():
    try:
        # Check if the airplane mode icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/airplane_mode_off.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/airplane_mode_off.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off airplane mode
def turn_on_or_off_airplane_mode(intent_data):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        if not is_airplane_mode_on() and not is_airplane_mode_off():
            pyautogui.press('esc')
            time.sleep(1)
            enable_or_disable_airplane_mode(intent_data)
            return

        # Warning message for enabling airplane mode
        if intent_data['intent'] == "on_airplane_mode" and not is_airplane_mode_on():
            speak(
                "Warning! Enabling airplane mode will turn off your current internet connection. Do you want to continue sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Airplane mode not enabled sir.")
                    pyautogui.press('esc')
                    return
                elif confirm['intent'] == "yes":
                    break
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        # Check if airplane mode is already on
        if intent_data['intent'] == "on_airplane_mode" and is_airplane_mode_on():
            speak("Airplane mode is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if airplane mode is already off
        if intent_data['intent'] == "off_airplane_mode" and not is_airplane_mode_on():
            speak("Airplane mode is already off sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if intent_data['intent'] == "on_airplane_mode":
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
                speak("Airplane mode is turned on sir")
            except pyautogui.ImageNotFoundException:
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
                speak("Airplane mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Airplane mode icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error toggling Airplane mode")
        if intent_data['intent'] == "on_airplane_mode":
            speak("Sorry, I couldn't turn on Airplane mode sir")
        else:
            speak("Sorry, I couldn't turn off Airplane mode sir")
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


# Function to check if Night light is already off
def is_night_light_off():
    try:
        # Check if the Night light icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/night_light_off.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/night_light_off.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Night light
def turn_on_or_off_night_light(intent_data):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        if not is_night_light_on() and not is_night_light_off():
            pyautogui.press('esc')
            time.sleep(1)
            enable_or_disable_night_light(intent_data)
            return

        # Check if night light is already on
        if intent_data['intent'] == "on_night_light" and is_night_light_on():
            speak("Night light is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if night light is already off
        if intent_data['intent'] == "off_night_light" and not is_night_light_on():
            speak("Night light is already off sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if intent_data['intent'] == "on_night_light":
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
                speak("Night light is turned on sir")
            except pyautogui.ImageNotFoundException:
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
                speak("Night light is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Night light icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error toggling Night light")
        if intent_data['intent'] == "on_night_light":
            speak("Sorry, I couldn't turn on Night light sir")
        else:
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
        speak("An error occurred")


# Function to check if Nearby Sharing is already off
def is_nearby_sharing_off():
    try:
        # Check if the Nearby Sharing icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/nearby_sharing_off.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/nearby_sharing_off.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Nearby Sharing
def turn_on_or_off_nearby_sharing(intent_data):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        if not is_nearby_sharing_on() and not is_nearby_sharing_off():
            pyautogui.press('esc')
            time.sleep(1)
            enable_or_disable_nearby_share(intent_data)
            return

        # Check if nearby sharing is already on
        if intent_data['intent'] == "on_nearby_sharing" and is_nearby_sharing_on():
            speak("Nearby sharing is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Check if nearby sharing is already off
        if intent_data['intent'] == "off_nearby_sharing" and not is_nearby_sharing_on():
            speak("Nearby sharing is already off sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if intent_data['intent'] == "on_nearby_sharing":
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
                speak("Nearby sharing is turned on sir")
            except pyautogui.ImageNotFoundException:
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
                speak("Nearby sharing is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Nearby sharing icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error toggling Nearby sharing")
        if intent_data['intent'] == "on_nearby_sharing":
            speak("Sorry, I couldn't turn on Nearby sharing sir")
        else:
            speak("Sorry, I couldn't turn off Nearby sharing sir")
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


# Function to check if Wi-Fi is already on
def is_wifi_off():
    try:
        # Check if the Wi-Fi icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/action_center/wifi_off.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/action_center/wifi_off.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Wi-Fi
def turn_on_or_off_wifi(intent_data):
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        if not is_wifi_on() and not is_wifi_off():
            pyautogui.press('esc')
            time.sleep(1)
            enable_or_disable_wifi(intent_data)
            return

        # Check if Wi-Fi is already on
        if intent_data['intent'] == "on_wifi" and is_wifi_on():
            speak("Wi-Fi is already on sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        # Warning message for enabling Wi-Fi
        if intent_data['intent'] == "on_wifi" and not is_wifi_on() and check_internet():
            speak(
                "Warning! Enabling Wi-Fi will turn off your current internet connection. Do you want to continue sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Wi-Fi not enabled sir.")
                    pyautogui.press('esc')
                    return
                elif confirm['intent'] == "yes":
                    break
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue


        # Check if Wi-Fi is already off
        if intent_data['intent'] == "off_wifi" and is_wifi_off():
            speak("Wi-Fi is already off sir")
            # Press the Esc key
            pyautogui.press('esc')
            return

        if intent_data['intent'] == "on_wifi":
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
                speak("Wi-Fi is turned on sir")
            except pyautogui.ImageNotFoundException:
                speak("Wi-Fi icon not found sir")
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
                speak("Wi-Fi is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Wi-Fi icon not found sir")
        # Press the Esc key
        pyautogui.press('esc')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error toggling Wi-Fi mode")
        if intent_data['intent'] == "on_wifi":
            speak("Sorry, I couldn't turn on Wi-Fi sir")
        else:
            speak("Sorry, I couldn't turn off Wi-Fi sir")
        pyautogui.press('esc')


# Function to show available Wi-Fi networks
def show_wifi_networks():
    try:
        # Press the Esc key
        pyautogui.press('esc')
        time.sleep(1)
        # Press keys to open Action Center
        pyautogui.hotkey('win', 'a')
        time.sleep(1)

        if not is_wifi_on() and not is_wifi_off():
            pyautogui.press('esc')
            time.sleep(1)
            settings_show_wifi_networks()
            return

        # Check if Wi-Fi is off
        if not is_wifi_on():
            speak("Wi-Fi is off sir")

            speak("Please note that available Wi-Fi networks won't be visible until Wi-Fi is turned on.")

            # Ask the user whether to turn on Wi-Fi
            speak("Would you like me to turn on Wi-Fi sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Got it sir. I'll leave Wi-Fi as it is.")
                    return
                elif confirm['intent'] == "yes":
                    pyautogui.press('enter')
                    speak("Wi-Fi is turned on sir")
                    break
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        # Navigate to Wi-Fi networks
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        speak("Available Wi-Fi networks displayed sir")

    except Exception as e:
        # Handle any errors that may occur
        speak("Error displaying Wi-Fi networks")
        speak("Sorry, I couldn't display available Wi-Fi networks sir")
        pyautogui.press('esc')
