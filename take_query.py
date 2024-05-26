import time
from greet import greet
from check_functions import check_internet
from sam_functions.speak import speak
from sam_functions.listen import listen
from app_functions import open_application, close_application, close_window
from volume_functions import volume_up, volume_down, mute_volume, unmute_volume
from brightness_functions import increase_brightness, decrease_brightness, set_brightness
from actioncenter_functions import show_or_hide_action_center, toggle_wifi, action_center_show_wifi_networks, \
    toggle_bluetooth, action_center_show_bluetooth_devices, toggle_airplane_mode, toggle_battery_saver, \
    toggle_night_light, toggle_nearby_sharing
from settings_functions import enable_or_disable_bluetooth, settings_show_bluetooth_devices, enable_or_disable_wifi, \
    settings_show_wifi_networks, enable_or_disable_airplane_mode, enable_or_disable_night_light, \
    enable_or_disable_do_not_disturb, enable_or_disable_nearby_share, enable_or_disable_hotspot, \
    enable_or_disable_light_or_dark_mode
from actioncenter_or_settings_functions import turn_on_or_off_bluetooth, show_bluetooth_devices, \
    turn_on_or_off_airplane_mode, turn_on_or_off_night_light, turn_on_or_off_nearby_sharing, turn_on_or_off_wifi, \
    show_wifi_networks
from windows_functions.search_in_windows import search_in_windows
from windows_functions.open_settings import open_settings
from windows_functions.take_photo import take_photo
from windows_functions.start_video import start_video
from windows_functions.scan_barcode import scan_barcode
from windows_functions.screenshot import screenshot
from windows_functions.screenrecord import screenrecord
from windows_functions.record_audio import record_audio
from windows_functions.keyboard_keys import keyboard_keys
from windows_functions.shortcut_functions import shortcut_functions
from windows_functions.system_control import system_control
from windows_functions.create_file import create_file
from windows_functions.time_and_date import tell_time_and_date
from search import search
from media_functions.play_functions import play_functions
from temperature_and_weather_functions import temperature, weather
from wikipedia_functions import wikipedia_functions
import eel
from random import choice
from intent_detect.load_model import recognize_intent


@eel.expose
# Function to interact with the user and perform actions based on their commands
def take_query():
    time.sleep(0.3)

    # Initial greeting
    speak("Hello sir, How may I help you?")

    # Initialize the sleeping state
    sleeping = False

    # Flag to track if the internet connection message has been displayed
    internet_connection_message_displayed = False

    # Loop to continuously listen for user commands
    while True:
        # Check internet connectivity
        if not check_internet():
            # Check if the message has already been displayed
            if not internet_connection_message_displayed:
                speak("Sir, it seems there is no internet connection. Please connect to the internet and try again")
                internet_connection_message_displayed = True  # Set the flag to True to indicate that the message has been displayed
            continue
        else:
            # Reset the flag when internet connection is available
            internet_connection_message_displayed = False

        if not sleeping:
            query = listen()

            if query == "":
                continue

            intent_data = recognize_intent(query)

            # Check if the user wants to wake up the assistant
            if "hey sam" in query or "sam" in query:
                speak("Yes sir, How may I help you?")

            # System controls
            elif intent_data['intent'] == "system_control_lock" or intent_data['intent'] == "system_control_sleep" or \
                    intent_data['intent'] == "system_control_sign_out" or intent_data[
                'intent'] == "system_control_restart" or intent_data['intent'] == "system_control_shutdown":
                system_control(intent_data)
                continue

            # Check if the user wants the assistant to sleep
            elif intent_data['intent'] == "assistant_sleep":
                # Use a random response from the JSON data
                response = choice(intent_data["responses"])
                speak(response + " sir")
                sleeping = True
                continue

        else:
            # Listen for wake-up phrase
            eel.DisplayMessage("Say, Hey Sam or wake up")
            time.sleep(0.6)
            wake_up_phrase = listen()

            if wake_up_phrase == "":
                continue

            wake_intent_data = recognize_intent(wake_up_phrase)

            if wake_intent_data['intent'] == "wake_up":
                # Use a random response from the JSON data
                response = choice(wake_intent_data["responses"])
                speak(response)
                sleeping = False

            continue

        # Respond to specific queries
        # Tell the user the assistant's name
        if intent_data['intent'] == "assistant_name":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "user_identity":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "assistant_status":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "assistant_capabilities":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "thank_you":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "goodbye":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "hobbies":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "dream":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "meaning_of_life":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "robot":
            speak(intent_data["responses"])

        elif intent_data['intent'] == "apology":
            response = choice(intent_data["responses"])
            speak(response)

        elif intent_data['intent'] == "good_day":
            response = choice(intent_data["responses"])
            speak(response)

        # Greet
        elif intent_data['intent'] == "greet":
            greet(query, intent_data)

        # Exit the program
        elif intent_data['intent'] == "exit":
            speak("Exiting sir.")
            eel.close_window()
            exit()

        # Date and Time
        elif intent_data['intent'] == "day_before_yesterday" or intent_data['intent'] == "yesterday_date" or \
                intent_data['intent'] == "yesterday_day" or intent_data['intent'] == "yesterday_month" or intent_data[
            'intent'] == "yesterday_year" or intent_data['intent'] == "day_after_tomorrow_date" or intent_data[
            'intent'] == "tomorrow_date" or intent_data['intent'] == "tomorrow_day" or intent_data[
            'intent'] == "tomorrow_month" or intent_data['intent'] == "tomorrow_year" or intent_data[
            'intent'] == "time_and_date" or intent_data['intent'] == "time_and_day" or intent_data[
            'intent'] == "time_and_month" or intent_data['intent'] == "time_and_year" or intent_data[
            'intent'] == "current_time" or intent_data['intent'] == "current_hour_day" or intent_data[
            'intent'] == "current_hour_month" or intent_data['intent'] == "current_hour_year" or intent_data[
            'intent'] == "current_hour" or intent_data['intent'] == "current_date" or intent_data[
            'intent'] == "current_day" or intent_data['intent'] == "current_month" or intent_data[
            'intent'] == "current_year":
            tell_time_and_date(intent_data)

        # Temperature
        elif intent_data['intent'] == "temperature":
            temperature(query, intent_data)

        # Weather
        elif intent_data['intent'] == "weather":
            weather(query, intent_data)

        # Check if the user wants to turn on internet
        elif intent_data['intent'] == "internet_on" and check_internet():
            response = choice(intent_data["responses"])
            speak(response)

        # Check if the user wants to turn off internet
        elif intent_data['intent'] == "internet_off" and check_internet():
            # Display warning message
            speak(intent_data["responses"])

        # Open settings
        elif intent_data['intent'] == "open_settings":
            open_settings(query, intent_data)

        # Keyboard keys
        elif intent_data['intent'] == "keyboard_keys":
            keyboard_keys(query, intent_data)

        # Shortcuts
        elif intent_data['intent'] == "shortcut_keys":
            shortcut_functions(query, intent_data)

        # Open application
        elif intent_data['intent'] == "open_application":
            open_application(query, intent_data)

        # Close application
        elif intent_data['intent'] == "close_application":
            close_application(query, intent_data)

        # Close current application
        elif intent_data['intent'] == "close_current_window":
            close_window()

        # Search on Wikipedia
        elif intent_data['intent'] == "wikipedia":
            wikipedia_functions(query, intent_data)

        # Increase system volume
        elif intent_data['intent'] == "volume_up":
            volume_up(1)

        # Decrease system volume
        elif intent_data['intent'] == "volume_down":
            volume_down(1)

        # UnMute
        elif intent_data['intent'] == "unmute":
            unmute_volume()

        # Mute
        elif intent_data['intent'] == "mute":
            mute_volume()

        # Increase screen brightness
        elif intent_data['intent'] == "increase_brightness":
            increase_brightness(10)

        # Decrease screen brightness
        elif intent_data['intent'] == "decrease_brightness":
            decrease_brightness(10)

        # Check if the query mentions setting brightness to a specific level
        elif intent_data['intent'] == "set_brightness":
            # Extract the brightness level from the query
            try:
                brightness_str = next(word for word in query.split() if word.isdigit() or "%" in word)
                # Remove the "%" sign if present and convert to integer
                brightness_level = int(brightness_str.rstrip("%"))
                # Set the brightness to the extracted level
                set_brightness(brightness_level)
            except StopIteration:
                speak("Sir please specify the brightness level.")
            except ValueError:
                speak("Sir please provide a valid brightness level.")

        # Action Center
        # To show or hide action center
        elif intent_data['intent'] == "show_action_center" or intent_data['intent'] == "hide_action_center":
            show_or_hide_action_center(intent_data)

        # On action center toggle wi-fi
        elif intent_data['intent'] == "on_wifi_action_center" or intent_data['intent'] == "off_wifi_action_center":
            toggle_wifi(intent_data)

        # On action center show Bluetooth devices
        elif intent_data['intent'] == "show_wifi_networks_action_center":
            action_center_show_wifi_networks()

        # On action center toggle Bluetooth
        elif intent_data['intent'] == "on_bluetooth_action_center" or intent_data['intent'] == "off_bluetooth_action_center":
            toggle_bluetooth(intent_data)

        # On action center show Bluetooth devices
        elif intent_data['intent'] == "show_bluetooth_devices_action_center":
            action_center_show_bluetooth_devices()

        # On action center toggle airplane mode
        elif intent_data['intent'] == "on_airplane_mode_action_center" or intent_data['intent'] == "off_airplane_mode_action_center":
            toggle_airplane_mode(intent_data)

        # On action center toggle battery saver
        elif intent_data['intent'] == "on_battery_saver" or intent_data['intent'] == "off_battery_saver":
            toggle_battery_saver(intent_data)

        # On action center toggle night light mode
        elif intent_data['intent'] == "on_night_light_action_center" or intent_data['intent'] == "off_night_light_action_center":
            toggle_night_light(intent_data)

        # On action center toggle nearby sharing
        elif intent_data['intent'] == "on_nearby_sharing_action_center" or intent_data['intent'] == "off_nearby_sharing_action_center":
            toggle_nearby_sharing(intent_data)

        # Settings
        # Enable or disable Bluetooth in settings
        elif intent_data['intent'] == "on_bluetooth_settings" or intent_data['intent'] == "off_bluetooth_settings":
            enable_or_disable_bluetooth(intent_data)

        # On settings show Bluetooth devices
        elif intent_data['intent'] == "show_bluetooth_devices_settings":
            settings_show_bluetooth_devices()

        # Enable or disable Airplane Mode in settings
        elif intent_data['intent'] == "on_airplane_mode_settings" or intent_data['intent'] == "off_airplane_mode_settings":
            enable_or_disable_airplane_mode(intent_data)

        # Enable or disable Night Light in settings
        elif intent_data['intent'] == "on_night_light_settings" or intent_data['intent'] == "off_night_light_settings":
            enable_or_disable_night_light(intent_data)

        # Enable or disable Do Not Disturb in settings
        elif intent_data['intent'] == "on_do_not_disturb" or intent_data['intent'] == "off_do_not_disturb":
            enable_or_disable_do_not_disturb(intent_data)

        # Enable or disable Nearby Share in settings
        elif intent_data['intent'] == "on_nearby_share_settings" or intent_data['intent'] == "off_nearby_share_settings":
            enable_or_disable_nearby_share(intent_data)

        # Enable or disable Wi-Fi in settings
        elif intent_data['intent'] == "on_wifi_settings" or intent_data['intent'] == "off_wifi_settings":
            enable_or_disable_wifi(intent_data)

        # Show available Wi-Fi networks in settings
        elif intent_data['intent'] == "show_wifi_networks_settings":
            settings_show_wifi_networks()

        # Enable or disable Hotspot in settings
        elif intent_data['intent'] == "on_hotspot" or intent_data['intent'] == "off_hotspot":
            enable_or_disable_hotspot(intent_data)

        # Enable or disable Light or Dark Mode in settings
        elif intent_data['intent'] == "on_light_dark_mode" or intent_data['intent'] == "off_light_dark_mode":
            enable_or_disable_light_or_dark_mode(intent_data)

        # Turn on or off Bluetooth
        elif intent_data['intent'] == "on_bluetooth" or intent_data['intent'] == "off_bluetooth":
            turn_on_or_off_bluetooth(intent_data)

        # Show Bluetooth devices
        elif intent_data['intent'] == "show_bluetooth_devices":
            show_bluetooth_devices()

        # Turn on or off airplane mode
        elif intent_data['intent'] == "on_airplane_mode" or intent_data['intent'] == "off_airplane_mode":
            turn_on_or_off_airplane_mode(intent_data)

        # Turn on or off night light mode
        elif intent_data['intent'] == "on_night_light" or intent_data['intent'] == "off_night_light":
            turn_on_or_off_night_light(intent_data)

        # Turn on or off nearby sharing
        elif intent_data['intent'] == "on_nearby_sharing" or intent_data['intent'] == "off_nearby_sharing":
            turn_on_or_off_nearby_sharing(intent_data)

        # Turn on or off Wi-Fi
        elif intent_data['intent'] == "on_wifi" or intent_data['intent'] == "off_wifi":
            enable_or_disable_wifi(intent_data)

        # Show available Wi-Fi networks
        elif intent_data['intent'] == "show_wifi_networks":
            show_wifi_networks()

        # Camera
        # Take a photo
        elif intent_data['intent'] == "take_photo" or intent_data['intent'] == "camera_take_photo":
            take_photo(query, intent_data)

        # Start a video
        elif intent_data['intent'] == "camera_start_video":
            start_video()

        # Scan barcode
        elif intent_data['intent'] == "scan_barcode":
            scan_barcode()

        # Screenshot
        elif intent_data['intent'] == "take_screenshot" or intent_data['intent'] == "snipping_tool_take_screenshot":
            screenshot(query, intent_data)

        # Screenrecord
        elif intent_data['intent'] == "screen_record" or intent_data['intent'] == "snipping_tool_screen_record":
            screenrecord(intent_data)

        # Record audio
        elif intent_data['intent'] == "record_audio":
            record_audio()

        # Create a file
        elif intent_data['intent'] == "create_file":
            create_file(query, intent_data)

        # Search in Windows
        elif intent_data['intent'] == "search_windows":
            search_in_windows(query, intent_data)

        # Search
        elif intent_data['intent'] == "search_google" or intent_data['intent'] == "search_youtube" or intent_data['intent'] == "search_spotify" or intent_data['intent'] == "search_linkedin" or intent_data['intent'] == "search_amazon" or intent_data['intent'] == "search_twitter" or intent_data['intent'] == "search_github" or intent_data['intent'] == "search_wikipedia" or intent_data['intent'] == "search_facebook" or intent_data['intent'] == "search_instagram" or intent_data['intent'] == "search_netflix" or intent_data['intent'] == "search_bing" or intent_data['intent'] == "search_file_explorer":
            search(query, intent_data)

        # Play music or video
        elif intent_data['intent'] == "play_media" or intent_data['intent'] == "play_media_spotify":
            sleeping = play_functions(query, intent_data)

        else:
            speak(
                "Sorry sir, I didn't quite catch that. As much as I'd like to, I have some limitations. How can I assist you within my capabilities?")
