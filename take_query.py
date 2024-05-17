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
from intent_detect.load_model import recognize_intent


@eel.expose
# Function to interact with the user and perform actions based on their commands
def take_query():
    time.sleep(0.6)
    # Initial greeting
    speak("Hello Boss, How may I help you?")

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
                speak("Boss, it seems there is no internet connection. Please connect to the internet and try again")
                internet_connection_message_displayed = True  # Set the flag to True to indicate that the message has been displayed
            continue
        else:
            # Reset the flag when internet connection is available
            internet_connection_message_displayed = False

        query = ""

        if not sleeping:
            query = listen()

            if query == "":
                continue

            intent_data = recognize_intent(query)

            # Check if the user wants to wake up the assistant
            if "hey sam" in query or "sam" in query:
                speak("Yes boss, How may I help you?")

            # System controls
            elif intent_data['intent'] == "system_control":
                system_control(query)

            # Check if the user wants the assistant to sleep
            elif intent_data['intent'] == "assistant_sleep":
                speak("Going to sleep boss")
                sleeping = True
                continue

        else:
            # Listen for wake-up phrase
            eel.DisplayMessage("Say, hey Sam or wake up")
            wake_up_phrase = listen()

            if "hey sam" in wake_up_phrase or "wake up" in wake_up_phrase or "sam":
                speak("Yes boss, How may I help you?")
                sleeping = False
                continue

        # Respond to specific queries
        # Tell the user the assistant's name
        if intent_data['intent'] == "assistant_name":
            speak("I'm Sam your virtual assistant! I'm here to help you with tasks and provide information boss")

        elif intent_data['intent'] == "user_identity":
            speak("You are you boss. You're the wonderful individual interacting with me right now.")

        elif intent_data['intent'] == "assistant_status":
            speak("I'm just a bunch of code, but I'm functioning perfectly fine boss")

        elif intent_data['intent'] == "assistant_capabilities":
            speak(
                "As your assistant boss I can handle tasks like managing settings searching the web opening apps and more")

        elif intent_data['intent'] == "thank_you":
            speak("You're welcome boss! Always happy to assist.")

        elif intent_data['intent'] == "goodbye":
            speak("Goodbye boss! Have a great day ahead!")

        elif intent_data['intent'] == "hobbies":
            speak("My main hobby is assisting you with your tasks and inquiries boss!")

        elif intent_data['intent'] == "like_music":
            speak("I don't have ears to enjoy music but I can play your favorite songs for you boss!")

        elif intent_data['intent'] == "favorite_color":
            speak("I don't have eyes to see colors boss but I like the concept of 'electric blue' boss!")

        elif intent_data['intent'] == "dream":
            speak("I don't sleep, so I don't dream boss!")

        elif intent_data['intent'] == "meaning_of_life":
            speak(
                "The meaning of life is a philosophical question that has puzzled humanity for centuries. Some say it's to seek happiness, others say it's to find purpose boss")

        elif intent_data['intent'] == "robot":
            speak(
                "I'm an AI-powered virtual assistant boss. While I don't have a physical body like a robot, I'm here to assist you!")

        elif intent_data['intent'] == "pets":
            speak("I don't have any pets, but I'm here to assist you boss!")

        elif intent_data['intent'] == "apology":
            speak("No need to apologize boss")

        elif intent_data['intent'] == "good_day":
            speak("Have a good day too boss!")

        # Greet
        elif intent_data['intent'] == "Greet":
            greet(intent_data)

        # Exit the program
        elif intent_data['intent'] == "exit":
            speak("Exiting Boss")
            eel.close_window()
            exit()

        # Date and Time
        elif intent_data['intent'] == "date_time":
            tell_time_and_date(query)

        # Temperature
        elif intent_data['intent'] == "temperature":
            temperature(query)

        # Weather
        elif intent_data['intent'] == "weather":
            weather(query)

        # Check if the user wants to turn on internet
        elif intent_data['intent'] == "internet_on" and check_internet():
            speak("Boss the internet is already on")

        # Check if the user wants to turn off internet
        elif intent_data['intent'] == "internet_off" and check_internet():
            # Display warning message
            speak(
                "I'm sorry boss but I must warn you. You can't turn off the internet. My functions rely on an active internet connection to assist you effectively")

        # Open settings
        elif intent_data['intent'] == "open_settings":
            open_settings(query)

        # Keyboard keys
        elif intent_data['intent'] == "keyboard_keys":
            keyboard_keys(query)

        # Shortcuts
        elif intent_data['intent'] == "shortcuts":
            shortcut_functions(query)

        # Open application
        elif intent_data['intent'] == "open_application":
            open_application(query)

        # Close current application
        elif intent_data['intent'] == "close_current_window":
            close_window()

        # Close application
        elif intent_data['intent'] == "close_application":
            close_application(query)

        # Search on Wikipedia
        elif intent_data['intent'] == "wikipedia":
            wikipedia_functions(query)

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
                speak("Boss please specify the brightness level.")
            except ValueError:
                speak("Boss please provide a valid brightness level.")

        # Action Center
        # To show or hide action center
        elif intent_data['intent'] == "show_hide_action_center":
            show_or_hide_action_center(query)

        # On action center toggle wi-fi
        elif intent_data['intent'] == "toggle_wifi_action_center":
            toggle_wifi(query)

        # On action center show Bluetooth devices
        elif intent_data['intent'] == "show_wifi_networks_action_center":
            action_center_show_wifi_networks()

        # On action center toggle Bluetooth
        elif intent_data['intent'] == "toggle_bluetooth_action_center":
            toggle_bluetooth(query)

        # On action center show Bluetooth devices
        elif intent_data['intent'] == "show_bluetooth_devices_action_center":
            action_center_show_bluetooth_devices()

        # On action center toggle airplane mode
        elif intent_data['intent'] == "toggle_airplane_mode_action_center":
            toggle_airplane_mode(query)

        # On action center toggle battery saver
        elif intent_data['intent'] == "toggle_battery_saver":
            toggle_battery_saver(query)

        # On action center toggle night light mode
        elif intent_data['intent'] == "toggle_night_light_action_center":
            toggle_night_light(query)

        # On action center toggle nearby sharing
        elif intent_data['intent'] == "toggle_nearby_sharing_action_center":
            toggle_nearby_sharing(query)

        # Settings
        # Enable or disable Bluetooth in settings
        elif intent_data['intent'] == "enable_disable_bluetooth_settings":
            enable_or_disable_bluetooth(query)

        # On settings show Bluetooth devices
        elif intent_data['intent'] == "show_bluetooth_devices_settings":
            settings_show_bluetooth_devices()

        # Enable or disable Airplane Mode in settings
        elif intent_data['intent'] == "enable_disable_airplane_mode_settings":
            enable_or_disable_airplane_mode(query)

        # Enable or disable Night Light in settings
        elif intent_data['intent'] == "enable_disable_night_light_settings":
            enable_or_disable_night_light(query)

        # Enable or disable Do Not Disturb in settings
        elif intent_data['intent'] == "enable_disable_do_not_disturb":
            enable_or_disable_do_not_disturb(query)

        # Enable or disable Nearby Share in settings
        elif intent_data['intent'] == "enable_disable_nearby_share_settings":
            enable_or_disable_nearby_share(query)

        # Enable or disable Wi-Fi in settings
        elif intent_data['intent'] == "enable_disable_wifi_settings":
            enable_or_disable_wifi(query)

        # Show available Wi-Fi networks in settings
        elif intent_data['intent'] == "show_wifi_networks_settings":
            settings_show_wifi_networks()

        # Enable or disable Hotspot in settings
        elif intent_data['intent'] == "enable_disable_hotspot":
            enable_or_disable_hotspot(query)

        # Enable or disable Light or Dark Mode in settings
        elif intent_data['intent'] == "enable_disable_light_dark_mode":
            enable_or_disable_light_or_dark_mode(query)

        # Turn on or off Bluetooth
        elif intent_data['intent'] == "turn_on_off_bluetooth":
            turn_on_or_off_bluetooth(query)

        # Show Bluetooth devices
        elif intent_data['intent'] == "show_bluetooth_devices":
            show_bluetooth_devices()

        # Turn on or off airplane mode
        elif intent_data['intent'] == "turn_on_off_airplane_mode":
            turn_on_or_off_airplane_mode(query)

        # Turn on or off night light mode
        elif intent_data['intent'] == "turn_on_off_night_light":
            turn_on_or_off_night_light(query)

        # Turn on or off nearby sharing
        elif intent_data['intent'] == "turn_on_off_nearby_sharing":
            turn_on_or_off_nearby_sharing(query)

        # Turn on or off Wi-Fi
        elif intent_data['intent'] == "turn_on_off_wifi":
            enable_or_disable_wifi(query)

        # Show available Wi-Fi networks
        elif intent_data['intent'] == "show_wifi_networks":
            show_wifi_networks()

        # Camera
        # Take a photo
        elif intent_data['intent'] == "camera_take_photo":
            take_photo(query)

        # Start a video
        elif intent_data['intent'] == "camera_start_video":
            start_video()

        # Scan barcode
        elif intent_data['intent'] == "scan_barcode":
            scan_barcode()

        # Screenshot
        elif intent_data['intent'] == "take_screenshot":
            screenshot(query)

        # Screenrecord
        elif intent_data['intent'] == "screen_record":
            screenrecord(query)

        # Record audio
        elif intent_data['intent'] == "record_audio":
            record_audio()

        # Create a file
        elif intent_data['intent'] == "create_file":
            create_file(query)

        # Search in Windows
        elif intent_data['intent'] == "search_windows":
            search_in_windows(query)

        # Search
        elif intent_data['intent'] == "search":
            search(query)

        # Play music or video
        elif intent_data['intent'] == "play_media":
            play_functions(query)

        else:
            speak(
                "Sorry, I didn't quite catch that. As much as I'd like to, I have some limitations. How can I assist you within my capabilities?")
