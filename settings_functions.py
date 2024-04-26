import time
import pyautogui
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_internet, check_dark_mode, check_settings_opening, check_window_maximized


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
        print("Sam: An error occurred:", e)


# Function to turn on or off Bluetooth
def enable_or_disable_bluetooth(query):
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
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

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

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
                        "images/light_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                else:
                    bluetooth_icon_location = pyautogui.locateCenterOnScreen(
                        "images/dark_mode/settings/toggle_off.png", confidence=0.9, grayscale=True)
                pyautogui.click(bluetooth_icon_location)
                print("Sam: Bluetooth is turned on, sir")
                speak("Bluetooth is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Bluetooth toggle not found, sir")
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
                print("Sam: Bluetooth is turned off, sir")
                speak("Bluetooth is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Bluetooth toggle not found, sir")
                speak("Bluetooth toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Bluetooth status: {e}")
        if "on bluetooth" in query:
            print("Sam: Sorry, I couldn't turn on Bluetooth, sir")
            speak("Sorry, I couldn't turn on Bluetooth sir")
        else:
            print("Sam: Sorry, I couldn't turn off Bluetooth, sir")
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
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

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

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
                response = listen()
                if response == "":
                    continue
                if "yes" in response:
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
                        print("Sam: Bluetooth is turned on, sir")
                        speak("Bluetooth is turned on sir")
                        break

                    except pyautogui.ImageNotFoundException:
                        print("Sam: Bluetooth toggle not found, sir")
                        speak("Bluetooth toggle not found sir")
                        return
                else:
                    print("Sam: Got it, sir. I'll leave Bluetooth as it is.")
                    speak("Got it sir. I'll leave Bluetooth as it is")
                    return

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

            print("Sam: Bluetooth devices list displayed, sir")
            speak("Bluetooth devices list displayed sir")

        except pyautogui.ImageNotFoundException:
            print("Sam: Add devices button not found, sir")
            speak("Add devices button not found sir")
            return

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error displaying Bluetooth devices: {e}")
        print("Sam: Sorry, I couldn't display Bluetooth devices, sir")
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
        print("Sam: An error occurred:", e)


# Function to turn on or off Airplane Mode
def enable_or_disable_airplane_mode(query):
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_settings_opening():
                        if "on airplane mode" in query:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn on Airplane Mode")
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Airplane Mode")
                            return
                        else:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn off Airplane Mode")
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Airplane Mode")
                            return
                else:
                    print("Sam: Closing settings, sir")
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Airplane Mode is already on
        if "on airplane mode" in query and is_airplane_mode_on():
            print("Sam: Airplane Mode is already on, sir")
            speak("Airplane Mode is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

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
                    speak("Airplane mode not enabled, sir.")
                    pyautogui.hotkey('alt', 'f4')
                    return

        # Check if Airplane Mode is already off
        if "off airplane mode" in query and not is_airplane_mode_on():
            print("Sam: Airplane Mode is already off, sir")
            speak("Airplane Mode is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if "on airplane mode" in query:
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
                print("Sam: Airplane Mode is turned on, sir")
                speak("Airplane Mode is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Airplane Mode toggle not found, sir")
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
                print("Sam: Airplane Mode is turned off, sir")
                speak("Airplane Mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Airplane Mode toggle not found, sir")
                speak("Airplane Mode toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Airplane Mode status: {e}")
        if "on airplane mode" in query:
            print("Sam: Sorry, I couldn't turn on Airplane Mode, sir")
            speak("Sorry, I couldn't turn on Airplane Mode sir")
        else:
            print("Sam: Sorry, I couldn't turn off Airplane Mode, sir")
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
        print("Sam: An error occurred:", e)


# Function to enable or disable Night Light mode
def enable_or_disable_night_light(query):
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_settings_opening():
                        if "on night light" in query:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn on Night Light mode")
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Night Light mode")
                            return
                        else:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn off Night Light mode")
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Night Light mode")
                            return
                else:
                    print("Sam: Closing settings, sir")
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Night Light mode is already on
        if "on night light" in query and is_night_light_on():
            print("Sam: Night Light mode is already on, sir")
            speak("Night Light mode is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Check if Night Light mode is already off
        if "off night light" in query and not is_night_light_on():
            print("Sam: Night Light mode is already off, sir")
            speak("Night Light mode is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if "on night light" in query:
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
                print("Sam: Night Light mode is turned on, sir")
                speak("Night Light mode is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Night Light toggle not found, sir")
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
                print("Sam: Night Light mode is turned off, sir")
                speak("Night Light mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Night Light toggle not found, sir")
                speak("Night Light toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Night Light mode status: {e}")
        if "on night light" in query:
            print("Sam: Sorry, I couldn't turn on Night Light mode, sir")
            speak("Sorry, I couldn't turn on Night Light mode sir")
        else:
            print("Sam: Sorry, I couldn't turn off Night Light mode, sir")
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
        print("Sam: An error occurred:", e)


# Function to enable or disable Do Not Disturb mode
def enable_or_disable_do_not_disturb(query):
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_settings_opening():
                        if "on do not disturb" in query:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn on Do Not Disturb mode")
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Do Not Disturb mode")
                            return
                        else:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn off Do Not Disturb mode")
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Do Not Disturb mode")
                            return
                else:
                    print("Sam: Closing settings, sir")
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('tab')

        # Check if Do Not Disturb mode is already on
        if "on do not disturb" in query and is_do_not_disturb_on():
            print("Sam: Do Not Disturb mode is already on, sir")
            speak("Do Not Disturb mode is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Check if Do Not Disturb mode is already off
        if "off do not disturb" in query and not is_do_not_disturb_on():
            print("Sam: Do Not Disturb mode is already off, sir")
            speak("Do Not Disturb mode is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if "on do not disturb" in query:
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
                print("Sam: Do Not Disturb mode is turned on, sir")
                speak("Do Not Disturb mode is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Do Not Disturb toggle not found, sir")
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
                print("Sam: Do Not Disturb mode is turned off, sir")
                speak("Do Not Disturb mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Do Not Disturb toggle not found, sir")
                speak("Do Not Disturb toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Do Not Disturb mode status: {e}")
        if "on do not disturb" in query:
            print("Sam: Sorry, I couldn't turn on Do Not Disturb mode, sir")
            speak("Sorry, I couldn't turn on Do Not Disturb mode sir")
        else:
            print("Sam: Sorry, I couldn't turn off Do Not Disturb mode, sir")
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
        print("Sam: An error occurred:", e)


# Function to enable or disable Nearby Share mode
def enable_or_disable_nearby_share(query):
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_settings_opening():
                        if "on nearby share" in query or "on nearby sharing" in query:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn on Nearby Share mode")
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Nearby Share mode")
                            return
                        else:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn off Nearby Share mode")
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Nearby Share mode")
                            return
                else:
                    print("Sam: Closing settings, sir")
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Nearby Share mode is already on
        if ("on nearby share" in query or "on nearby sharing" in query) and is_nearby_share_on():
            print("Sam: Nearby Share mode is already on, sir")
            speak("Nearby Share mode is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Check if Nearby Share mode is already off
        if ("off nearby share" in query or "off nearby sharing" in query) and not is_nearby_share_on():
            print("Sam: Nearby Share mode is already off, sir")
            speak("Nearby Share mode is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if "on nearby share" in query or "on nearby sharing" in query:
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
                print("Sam: Nearby Share mode is turned on, sir")
                speak("Nearby Share mode is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Nearby Share toggle not found, sir")
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
                print("Sam: Nearby Share mode is turned off, sir")
                speak("Nearby Share mode is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Nearby Share toggle not found, sir")
                speak("Nearby Share toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Nearby Share mode status: {e}")
        if "on nearby share" in query or "on nearby sharing" in query:
            print("Sam: Sorry, I couldn't turn on Nearby Share mode, sir")
            speak("Sorry, I couldn't turn on Nearby Share mode sir")
        else:
            print("Sam: Sorry, I couldn't turn off Nearby Share mode, sir")
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
        print("Sam: An error occurred:", e)


# Function to turn on or off Wi-Fi
def enable_or_disable_wifi(query):
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_settings_opening():
                        if "on Wi-Fi mode" in query:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn on Wi-Fi")
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Wi-Fi")
                            return
                        else:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn off Wi-Fi")
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Wi-Fi")
                            return
                else:
                    print("Sam: Closing settings, sir")
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Wi-Fi is already on
        if "on wi-fi" in query and is_wifi_on():
            print("Sam: Wi-Fi is already on, sir")
            speak("Wi-Fi is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        # Warning message for enabling Wi-Fi
        if "on wi-fi" in query and not is_wifi_on() and check_internet():
            print(
                "Sam: Warning! Enabling Wi-Fi will turn off your current internet connection. Do you want to continue, sir?")
            speak(
                "Warning! Enabling Wi-Fi will turn off your current internet connection. Do you want to continue sir?")
            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    break
                else:
                    print("Sam: Wi-Fi not enabled, sir.")
                    speak("Wi-Fi not enabled, sir.")
                    pyautogui.hotkey('alt', 'f4')
                    return

        # Check if Wi-Fi is already off
        if "off wi-fi" in query and not is_wifi_on():
            print("Sam: Wi-Fi is already off, sir")
            speak("Wi-Fi is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if "on wi-fi" in query:
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
                print("Sam: Wi-Fi is turned on, sir")
                speak("Wi-Fi is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Wi-Fi toggle not found, sir")
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
                print("Sam: Wi-Fi is turned off, sir")
                speak("Wi-Fi is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Wi-Fi toggle not found, sir")
                speak("Wi-Fi toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Wi-Fi status: {e}")
        if "on wi-fi" in query:
            print("Sam: Sorry, I couldn't turn on Wi-Fi, sir")
            speak("Sorry, I couldn't turn on Wi-Fi sir")
        else:
            print("Sam: Sorry, I couldn't turn off Wi-Fi, sir")
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_settings_opening():
                        print(
                            "Sam: The settings app is still taking time to open. Please manually open Wi-Fi settings.")
                        speak(
                            "The settings app is still taking time to open. Please manually open Wi-Fi settings.")
                        return
                else:
                    print("Sam: Closing settings, sir")
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Wi-Fi is already on
        if not is_wifi_on():
            print("Sam: Wi-Fi is off, sir")
            speak("Wi-Fi is off sir")

            print("Sam: Please note that available Wi-Fi networks won't be visible until Wi-Fi is turned on.")
            speak("Please note that available Wi-Fi networks won't be visible until Wi-Fi is turned on.")

            # Ask the user whether to turn on Wi-Fi
            print("Sam: Would you like me to turn on Wi-Fi, sir?")
            speak("Would you like me to turn on Wi-Fi sir?")

            while True:
                response = listen()
                if response == "":
                    continue
                if "yes" in response:
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
                        print("Sam: Wi-Fi is turned on, sir")
                        speak("Wi-Fi is turned on sir")
                        break

                    except pyautogui.ImageNotFoundException:
                        print("Sam: Wi-Fi toggle not found, sir")
                        speak("Wi-Fi toggle not found sir")
                        return
                else:
                    print("Sam: Got it, sir. I'll leave Wi-Fi as it is.")
                    speak("Got it sir. I'll leave Wi-Fi as it is")
                    return

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

            print("Sam: Available Wi-Fi networks displayed, sir")
            speak("Available Wi-Fi networks displayed sir")

        except pyautogui.ImageNotFoundException:
            print("Sam: Show available networks button not found, sir")
            speak("Show available networks button not found sir")
            return

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error displaying Wi-Fi networks: {e}")
        print("Sam: Sorry, I couldn't display Wi-Fi networks, sir")
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
        print("Sam: An error occurred:", e)


# Function to turn on or off Hotspot
def enable_or_disable_hotspot(query):
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_settings_opening():
                        if "on hotspot" in query:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn on Hotspot")
                            speak("The settings app is still taking time to open. Please manually turn on Hotspot")
                            return
                        else:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn off Hotspot")
                            speak(
                                "The settings app is still taking time to open. Please manually turn off Hotspot")
                            return
                else:
                    print("Sam: Closing settings, sir")
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        # Check if Hotspot is already on
        if "on hotspot" in query and is_hotspot_on():
            print("Sam: Hotspot is already on, sir")
            speak("Hotspot is already on sir")
            pyautogui.hotkey('alt', 'f4')
            return

        time.sleep(1)

        # Check if Hotspot is already off
        if "off hotspot" in query and not is_hotspot_on():
            print("Sam: Hotspot is already off, sir")
            speak("Hotspot is already off sir")
            pyautogui.hotkey('alt', 'f4')
            return

        if "on hotspot" in query:
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
                print("Sam: Hotspot is turned on, sir")
                speak("Hotspot is turned on sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Hotspot toggle not found, sir")
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
                print("Sam: Hotspot is turned off, sir")
                speak("Hotspot is turned off sir")
            except pyautogui.ImageNotFoundException:
                print("Sam: Hotspot toggle not found, sir")
                speak("Hotspot toggle not found sir")
            pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Hotspot status: {e}")
        if "on hotspot" in query:
            print("Sam: Sorry, I couldn't turn on Hotspot, sir")
            speak("Sorry, I couldn't turn on Hotspot sir")
        else:
            print("Sam: Sorry, I couldn't turn off Hotspot, sir")
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
        print("Sam: Hotspot details displayed, sir")
        speak("Hotspot details displayed sir")
    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error displaying Hotspot details: {e}")
        print("Sam: Sorry, I couldn't display Hotspot details, sir")
        speak("Sorry, I couldn't display Hotspot details sir")
        pyautogui.hotkey('alt', 'f4')


# Light or Dark mode
# Function to turn on or off Light Mode
def enable_or_disable_light_or_dark_mode(query):
    try:
        # Check if Light Mode is already on
        if ("on light mode" in query or "off dark mode" in query) and not check_dark_mode():
            print("Sam: Light Mode is already on, sir")
            speak("Light Mode is already on sir")
            return

        # Check if Dark Mode is already on
        if ("off light mode" in query or "on dark mode" in query) and check_dark_mode():
            print("Sam: Dark Mode is already on, sir")
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
            print("Sam: The settings app is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak("The settings app is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_settings_opening():
                        if "on light mode" in query:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn on Light Mode")
                            speak("The settings app is still taking time to open. Please manually turn on Light Mode")
                            return
                        else:
                            print(
                                "Sam: The settings app is still taking time to open. Please manually turn on Dark Mode")
                            speak(
                                "The settings app is still taking time to open. Please manually turn on Dark Mode")
                            return
                else:
                    print("Sam: Closing settings, sir")
                    speak("Closing settings sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        if not check_window_maximized():
            pyautogui.hotkey('win', 'up')
            time.sleep(0.2)

        if "on light mode" in query or "off dark mode" in query:
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.press('up')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.hotkey('alt', 'f4')
            print("Sam: Light Mode is turned on, sir")
            speak("Light Mode is turned on sir")
        else:
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.press('down')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.hotkey('alt', 'f4')
            print("Sam: Dark Mode is turned on, sir")
            speak("Dark Mode is turned on sir")

    except Exception as e:
        # Handle any errors that may occur
        print(f"Sam: Error changing Light Mode status: {e}")
        if "on light mode" in query or "off dark mode" in query:
            print("Sam: Sorry, I couldn't turn on Light Mode, sir")
            speak("Sorry, I couldn't turn on Light Mode sir")
        else:
            print("Sam: Sorry, I couldn't turn on Dark Mode, sir")
            speak("Sorry, I couldn't turn on Dark Mode sir")
        pyautogui.hotkey('alt', 'f4')
