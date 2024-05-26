import time
import pyautogui
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_internet, check_dark_mode, check_settings_opening, check_window_maximized
import eel
from intent_detect.load_model import recognize_intent


# Bluetooth
# Function to check if bluetooth is already on
def is_bluetooth_on():
    try:
        # Check if the Bluetooth icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/settings/toggle_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/settings/toggle_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Bluetooth
def enable_or_disable_bluetooth(intent_data):
    try:
        pyautogui.hotkey('win')
        time.sleep(0.2)
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
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        if intent_data['intent'] == "on_bluetooth_settings":
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Bluetooth")
                            return
                        else:
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Bluetooth")
                            return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if bluetooth is already on
        if intent_data['intent'] == "on_bluetooth_settings" and is_bluetooth_on():
            speak("Bluetooth is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Check if bluetooth is already off
        if intent_data['intent'] == "off_bluetooth_settings" and not is_bluetooth_on():
            speak("Bluetooth is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if intent_data['intent'] == "on_bluetooth_settings":
            # Click on the Bluetooth icon to turn it on
            # Adjust the coordinates based on the location of the Bluetooth icon on your screen
            try:
                if not check_dark_mode():
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                else:
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(bluetooth_icon_location)
                speak("Bluetooth is turned on sir")
            except pyautogui.ImageNotFoundException:
                speak("Bluetooth toggle not found sir")
            pyautogui.hotkey('alt', 'f4')
        else:
            # Click on the Bluetooth icon to turn it off
            # Adjust the coordinates based on the location of the Bluetooth icon on your screen
            try:
                if not check_dark_mode():
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/toggle_on.png", confidence=0.9, grayscale=True)
                else:
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/toggle_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(bluetooth_icon_location)
                speak("Bluetooth is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Bluetooth toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error changing Bluetooth status")
        if intent_data['intent'] == "on_bluetooth_settings":
            speak("Sorry, I couldn't turn on Bluetooth sir")
        else:
            speak("Sorry, I couldn't turn off Bluetooth sir")
        pyautogui.hotkey('alt', 'f4')


# Function show Bluetooth devices
def settings_show_bluetooth_devices():
    try:
        # Press keys to open Action Center
        pyautogui.hotkey('win')
        time.sleep(0.2)
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
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        speak(
                            "The settings app is still taking time to open. Please manually check Bluetooth devices")
                        return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

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
                    # Click on the Bluetooth icon to turn it on
                    # Adjust the coordinates based on the location of the Bluetooth icon on your screen
                    try:
                        if not check_dark_mode():
                            bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                                "images/light_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                        else:
                            bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                                "images/dark_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                        pyautogui.click(bluetooth_icon_location)
                        speak("Bluetooth is turned on sir")
                        break

                    except pyautogui.ImageNotFoundException:
                        speak("Bluetooth toggle not found sir")
                        return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        # Check for the "Add devices" button
        try:
            if not check_dark_mode():
                add_devices_button = pyautogui.locateCenterOnScreen(
                    "images/light_mode/settings/add_devices_button.png", confidence=0.9)
            else:
                add_devices_button = pyautogui.locateCenterOnScreen(
                    "images/dark_mode/settings/add_devices_button.png", confidence=0.9)

            pyautogui.click(add_devices_button)
            time.sleep(1)  # Wait for the "Add devices" page to load
            pyautogui.press('enter')

            speak("Bluetooth devices list displayed sir")

        except pyautogui.ImageNotFoundException:
            speak("Add devices button not found sir")
            return

    except Exception as e:
        # Handle any errors that may occur
        speak("Error displaying Bluetooth devices")
        speak("Sorry, I couldn't display Bluetooth devices sir")


# Airplane Mode
# Function to check if Airplane Mode is already on
def is_airplane_mode_on():
    try:
        # Check if the Airplane Mode icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/settings/focused_toggle_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/settings/focused_toggle_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Airplane Mode
def enable_or_disable_airplane_mode(intent_data):
    try:
        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('Flight')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # Check for the settings app continuously for 10 seconds
        if check_settings_opening():
            # Settings opening found, proceed with the operation
            pass
        else:
            # Settings app not found within 10 seconds, ask the user whether to continue waiting or exit
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        if intent_data['intent'] == "on_airplane_mode_settings":
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Airplane Mode")
                            return
                        else:
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Airplane Mode")
                            return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Airplane Mode is already on
        if intent_data['intent'] == "on_airplane_mode_settings" and is_airplane_mode_on():
            speak("Airplane Mode is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Warning message for enabling airplane mode
        if intent_data['intent'] == "on_airplane_mode_settings" and not is_airplane_mode_on():
            speak(
                "Warning! Enabling airplane mode will turn off your current internet connection. Do you want to continue sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Airplane mode not enabled sir.")
                    pyautogui.hotkey('alt', 'f4')
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

        # Check if Airplane Mode is already off
        if intent_data['intent'] == "off_airplane_mode_settings" and not is_airplane_mode_on():
            speak("Airplane Mode is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if intent_data['intent'] == "on_airplane_mode_settings":
            # Click on the Airplane Mode toggle to turn it on
            # Adjust the coordinates based on the location of the Airplane Mode toggle on your screen
            try:
                if not check_dark_mode():
                    airplane_mode_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/focused_toggle_off.png", confidence=0.9, grayscale=True)
                else:
                    airplane_mode_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/focused_toggle_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(airplane_mode_toggle_location)
                speak("Airplane Mode is turned on sir")
            except pyautogui.ImageNotFoundException:
                speak("Airplane Mode toggle not found sir")
            pyautogui.hotkey('alt', 'f4')
        else:
            # Click on the Airplane Mode toggle to turn it off
            # Adjust the coordinates based on the location of the Airplane Mode toggle on your screen
            try:
                if not check_dark_mode():
                    airplane_mode_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/focused_toggle_on.png", confidence=0.9, grayscale=True)
                else:
                    airplane_mode_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/focused_toggle_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(airplane_mode_toggle_location)
                speak("Airplane Mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Airplane Mode toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error changing Airplane Mode status")
        if intent_data['intent'] == "on_airplane_mode_settings":
            speak("Sorry, I couldn't turn on Airplane Mode sir")
        else:
            speak("Sorry, I couldn't turn off Airplane Mode sir")
        pyautogui.hotkey('alt', 'f4')


# Night Light mode
# Function to check if Night Light mode is already on
def is_night_light_on():
    try:
        # Check if the Night Light icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/settings/toggle_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/settings/toggle_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to enable or disable Night Light mode
def enable_or_disable_night_light(intent_data):
    try:
        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('Display')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # Check for the settings app continuously for 10 seconds
        if check_settings_opening():
            # Settings opening found, proceed with the operation
            pass
        else:
            # Settings app not found within 10 seconds, ask the user whether to continue waiting or exit
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        if intent_data['intent'] == "on_night_light_settings":
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Night Light mode")
                            return
                        else:
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Night Light mode")
                            return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Night Light mode is already on
        if intent_data['intent'] == "on_night_light_settings" and is_night_light_on():
            speak("Night Light mode is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Check if Night Light mode is already off
        if intent_data['intent'] == "off_night_light_settings" and not is_night_light_on():
            speak("Night Light mode is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if intent_data['intent'] == "on_night_light_settings":
            # Click on the Night Light toggle to turn it on
            # Adjust the coordinates based on the location of the Night Light toggle on your screen
            try:
                if not check_dark_mode():
                    night_light_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                else:
                    night_light_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(night_light_toggle_location)
                speak("Night Light mode is turned on sir")
            except pyautogui.ImageNotFoundException:
                speak("Night Light toggle not found sir")
            pyautogui.hotkey('alt', 'f4')
        else:
            # Click on the Night Light toggle to turn it off
            # Adjust the coordinates based on the location of the Night Light toggle on your screen
            try:
                if not check_dark_mode():
                    night_light_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/toggle_on.png", confidence=0.9, grayscale=True)
                else:
                    night_light_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/toggle_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(night_light_toggle_location)
                speak("Night Light mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Night Light toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error changing Night Light mode status")
        if intent_data['intent'] == "on_night_light_settings":
            speak("Sorry, I couldn't turn on Night Light mode sir")
        else:
            speak("Sorry, I couldn't turn off Night Light mode sir")
        pyautogui.hotkey('alt', 'f4')


# Do Not Disturb mode
# Function to check if Do Not Disturb mode is already on
def is_do_not_disturb_on():
    try:
        # Check if the Do Not Disturb icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/settings/focused_toggle_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/settings/focused_toggle_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to enable or disable Do Not Disturb mode
def enable_or_disable_do_not_disturb(intent_data):
    try:
        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('Notifications')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # Check for the settings app continuously for 10 seconds
        if check_settings_opening():
            # Settings opening found, proceed with the operation
            pass
        else:
            # Settings app not found within 10 seconds, ask the user whether to continue waiting or exit
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        if intent_data['intent'] == "on_do_not_disturb":
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Do Not Disturb mode")
                            return
                        else:
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Do Not Disturb mode")
                            return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('tab')

        # Check if Do Not Disturb mode is already on
        if intent_data['intent'] == "on_do_not_disturb" and is_do_not_disturb_on():
            speak("Do Not Disturb mode is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Check if Do Not Disturb mode is already off
        if intent_data['intent'] == "off_do_not_disturb" and not is_do_not_disturb_on():
            speak("Do Not Disturb mode is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if intent_data['intent'] == "on_do_not_disturb":
            # Click on the Do Not Disturb toggle to turn it on
            # Adjust the coordinates based on the location of the Do Not Disturb toggle on your screen
            try:
                if not check_dark_mode():
                    do_not_disturb_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/focused_toggle_off.png", confidence=0.9, grayscale=True)
                else:
                    do_not_disturb_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/focused_toggle_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(do_not_disturb_toggle_location)
                speak("Do Not Disturb mode is turned on sir")
            except pyautogui.ImageNotFoundException:
                speak("Do Not Disturb toggle not found sir")
            pyautogui.hotkey('alt', 'f4')
        else:
            # Click on the Do Not Disturb toggle to turn it off
            # Adjust the coordinates based on the location of the Do Not Disturb toggle on your screen
            try:
                if not check_dark_mode():
                    do_not_disturb_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/focused_toggle_on.png", confidence=0.9, grayscale=True)
                else:
                    do_not_disturb_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/focused_toggle_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(do_not_disturb_toggle_location)
                speak("Do Not Disturb mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Do Not Disturb toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error changing Do Not Disturb mode status")
        if intent_data['intent'] == "on_do_not_disturb":
            speak("Sorry, I couldn't turn on Do Not Disturb mode sir")
        else:
            speak("Sorry, I couldn't turn off Do Not Disturb mode sir")
        pyautogui.hotkey('alt', 'f4')


# Nearby Share
# Function to check if Nearby Share mode is already on
def is_nearby_share_on():
    try:
        # Check if the Nearby Share icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/settings/nearby_share_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/settings/nearby_share_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to enable or disable Nearby Share mode
def enable_or_disable_nearby_share(intent_data):
    try:
        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('Nearby share')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # Check for the settings app continuously for 10 seconds
        if check_settings_opening():
            # Settings opening found, proceed with the operation
            pass
        else:
            # Settings app not found within 10 seconds, ask the user whether to continue waiting or exit
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        if intent_data['intent'] == "on_nearby_share_settings":
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Nearby Share mode")
                            return
                        else:
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Nearby Share mode")
                            return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Nearby Share mode is already on
        if intent_data['intent'] == "on_nearby_share_settings" and is_nearby_share_on():
            speak("Nearby Share mode is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Check if Nearby Share mode is already off
        if intent_data['intent'] == "off_nearby_share_settings" and not is_nearby_share_on():
            speak("Nearby Share mode is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if intent_data['intent'] == "on_nearby_share_settings":
            # Click on the Nearby Share toggle to turn it on
            # Adjust the coordinates based on the location of the Nearby Share toggle on your screen
            try:
                if not check_dark_mode():
                    nearby_share_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/nearby_share_on_button.png", confidence=0.9, grayscale=True)
                else:
                    nearby_share_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/nearby_share_on_button.png", confidence=0.9, grayscale=True)
                pyautogui.click(nearby_share_toggle_location)
                speak("Nearby Share mode is turned on sir")
            except pyautogui.ImageNotFoundException:
                speak("Nearby Share toggle not found sir")
            pyautogui.hotkey('alt', 'f4')
        else:
            # Click on the Nearby Share toggle to turn it off
            # Adjust the coordinates based on the location of the Nearby Share toggle on your screen
            try:
                if not check_dark_mode():
                    nearby_share_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/nearby_share_off_button.png", confidence=0.9, grayscale=True)
                else:
                    nearby_share_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/nearby_share_off_button.png", confidence=0.9, grayscale=True)
                pyautogui.click(nearby_share_toggle_location)
                speak("Nearby Share mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Nearby Share toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error changing Nearby Share mode status")
        if intent_data['intent'] == "on_nearby_share_settings":
            speak("Sorry, I couldn't turn on Nearby Share mode sir")
        else:
            speak("Sorry, I couldn't turn off Nearby Share mode sir")
        pyautogui.hotkey('alt', 'f4')


# Wi-fi
# Function to check if Wi-fi is already on
def is_wifi_on():
    try:
        # Check if the toggle icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/settings/toggle_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/settings/toggle_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Wi-Fi
def enable_or_disable_wifi(intent_data):
    try:
        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('WiFi')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # Check for the settings app continuously for 10 seconds
        if check_settings_opening():
            # Settings opening found, proceed with the operation
            pass
        else:
            # Settings app not found within 10 seconds, ask the user whether to continue waiting or exit
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        if intent_data['intent'] == "on_wifi_settings":
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Wi-Fi")
                            return
                        else:
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Wi-Fi")
                            return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Wi-Fi is already on
        if intent_data['intent'] == "on_wifi_settings" and is_wifi_on():
            speak("Wi-Fi is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Warning message for enabling Wi-Fi
        if intent_data['intent'] == "on_wifi_settings" and not is_wifi_on() and check_internet():
            speak(
                "Warning! Enabling Wi-Fi will turn off your current internet connection. Do you want to continue sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Wi-Fi not enabled sir.")
                    pyautogui.hotkey('alt', 'f4')
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
        if intent_data['intent'] == "off_wifi_settings" and not is_wifi_on():
            speak("Wi-Fi is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if intent_data['intent'] == "on_wifi_settings":
            # Click on the Wi-Fi toggle to turn it on
            # Adjust the coordinates based on the location of the Wi-Fi toggle on your screen
            try:
                if not check_dark_mode():
                    wifi_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                else:
                    wifi_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(wifi_toggle_location)
                speak("Wi-Fi is turned on sir")
            except pyautogui.ImageNotFoundException:
                speak("Wi-Fi toggle not found sir")
            pyautogui.hotkey('alt', 'f4')
        else:
            # Click on the Wi-Fi toggle to turn it off
            # Adjust the coordinates based on the location of the Wi-Fi toggle on your screen
            try:
                if not check_dark_mode():
                    wifi_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/toggle_on.png", confidence=0.9, grayscale=True)
                else:
                    wifi_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/toggle_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(wifi_toggle_location)
                speak("Wi-Fi is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Wi-Fi toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        speak("Error changing Wi-Fi status")
        if intent_data['intent'] == "on_wifi_settings":
            speak("Sorry, I couldn't turn on Wi-Fi sir")
        else:
            speak("Sorry, I couldn't turn off Wi-Fi sir")
        pyautogui.hotkey('alt', 'f4')


# Function to show available Wi-Fi networks
def settings_show_wifi_networks():
    try:
        # Press keys to open Wi-Fi settings
        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('WiFi')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # Check for the settings app continuously for 10 seconds
        if check_settings_opening():
            # Settings opening found, proceed with the operation
            pass
        else:
            # Settings app not found within 10 seconds, ask the user whether to continue waiting or exit
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        if not check_settings_opening():
                            speak(
                                "The settings app is still taking time to open. Please manually open Wi-Fi settings.")

                            return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Wi-Fi is already on
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
                    # Click on the Wi-Fi icon to turn it on
                    # Adjust the coordinates based on the location of the Wi-Fi icon on your screen
                    try:
                        if not check_dark_mode():
                            wifi_icon_location = pyautogui.locateCenterOnScreen(
                                "images/light_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                        else:
                            wifi_icon_location = pyautogui.locateCenterOnScreen(
                                "images/dark_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                        pyautogui.click(wifi_icon_location)
                        speak("Wi-Fi is turned on sir")
                        break

                    except pyautogui.ImageNotFoundException:
                        speak("Wi-Fi toggle not found sir")
                        return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        # Check for the "Show available networks" button
        try:
            if not check_dark_mode():
                show_networks_button = pyautogui.locateCenterOnScreen(
                    "images/light_mode/settings/show_available_networks_button.png", confidence=0.9)
            else:
                show_networks_button = pyautogui.locateCenterOnScreen(
                    "images/dark_mode/settings/show_available_networks_button.png", confidence=0.9)

            pyautogui.click(show_networks_button)
            time.sleep(1)  # Wait for the available networks page to load

            speak("Available Wi-Fi networks displayed sir")

        except pyautogui.ImageNotFoundException:
            speak("Show available networks button not found sir")
            return

    except Exception as e:
        # Handle any errors that may occur
        speak("Error displaying Wi-Fi networks")
        speak("Sorry, I couldn't display Wi-Fi networks sir")


# Mobile Hotspot
# Function to check if hotspot is already on
def is_hotspot_on():
    try:
        # Check if the Hotspot icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/settings/toggle_on.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/settings/toggle_on.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        speak("An error occurred")


# Function to turn on or off Hotspot
def enable_or_disable_hotspot(intent_data):
    try:
        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('Mobile hotspot')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # Check for the settings app continuously for 10 seconds
        if check_settings_opening():
            # Settings opening found, proceed with the operation
            pass
        else:
            # Settings app not found within 10 seconds, ask the user whether to continue waiting or exit
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        if intent_data['intent'] == "on_hotspot":
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Hotspot")
                            return
                        else:
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Hotspot")
                            return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Hotspot is already on
        if intent_data['intent'] == "on_hotspot" and is_hotspot_on():
            speak("Hotspot is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        time.sleep(1)

        # Check if Hotspot is already off
        if intent_data['intent'] == "off_hotspot" and not is_hotspot_on():
            speak("Hotspot is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if intent_data['intent'] == "on_hotspot":
            # Click on the Hotspot toggle to turn it on
            # Adjust the coordinates based on the location of the Hotspot toggle on your screen
            try:
                if not check_dark_mode():
                    hotspot_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                else:
                    hotspot_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(hotspot_toggle_location)
                speak("Hotspot is turned on sir")
            except pyautogui.ImageNotFoundException:
                speak("Hotspot toggle not found sir")
            pyautogui.hotkey('alt', 'f4')
        else:
            # Click on the Hotspot toggle to turn it off
            # Adjust the coordinates based on the location of the Hotspot toggle on your screen
            try:
                if not check_dark_mode():
                    hotspot_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/light_mode/settings/toggle_on.png", confidence=0.9, grayscale=True)
                else:
                    hotspot_toggle_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/toggle_on.png", confidence=0.9, grayscale=True)
                pyautogui.click(hotspot_toggle_location)
                speak("Hotspot is turned off sir")
            except pyautogui.ImageNotFoundException:
                speak("Hotspot toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        speak(f"Error changing Hotspot status")
        if intent_data['intent'] == "on_hotspot":
            speak("Sorry, I couldn't turn on Hotspot sir")
        else:
            speak("Sorry, I couldn't turn off Hotspot sir")
        pyautogui.hotkey('alt', 'f4')


# Function to show Hotspot details
def show_hotspot_details():
    try:
        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('Mobile hotspot')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)
        speak("Hotspot details displayed sir")
    except Exception as e:
        # Handle any errors that may occur
        speak("Error displaying Hotspot details")
        speak("Sorry, I couldn't display Hotspot details sir")
        pyautogui.hotkey('alt', 'f4')


# Light or Dark mode
# Function to turn on or off Light Mode
def enable_or_disable_light_or_dark_mode(intent_data):
    try:
        # Check if Light Mode is already on
        if intent_data['intent'] == "on_light_dark_mode" and not check_dark_mode():
            speak("Light Mode is already on sir")
            return

        # Check if Dark Mode is already on
        if intent_data['intent'] == "off_light_dark_mode" and check_dark_mode():
            speak("Dark Mode is already on sir")
            return

        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('light mode')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)

        # Check for the settings app continuously for 10 seconds
        if check_settings_opening():
            # Settings opening found, proceed with the operation
            pass
        else:
            # Settings app not found within 10 seconds, ask the user whether to continue waiting or exit
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return
                elif confirm['intent'] == "yes":
                    if not check_settings_opening():
                        if intent_data['intent'] == "on_light_dark_mode":
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Light Mode")
                            return
                        else:
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Dark Mode")
                            return
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        if intent_data['intent'] == "on_light_dark_mode":
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.press('up')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.hotkey('alt', 'f4')
            speak("Light Mode is turned on sir")
        else:
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.press('down')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.hotkey('alt', 'f4')
            speak("Dark Mode is turned on sir")

    except Exception as e:
        # Handle any errors that may occur
        speak("Error changing Light Mode status")
        if intent_data['intent'] == "on_light_dark_mode":
            speak("Sorry, I couldn't turn on Light Mode sir")
        else:
            speak("Sorry, I couldn't turn on Dark Mode sir")
        pyautogui.hotkey('alt', 'f4')
