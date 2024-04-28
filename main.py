import webbrowser
import wikipedia
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
from windows_functions.search import search_in_windows
from windows_functions.open_settings import open_settings
from windows_functions.take_photo import take_photo
from windows_functions.start_video import start_video
from windows_functions.scan_barcode import scan_barcode
from windows_functions.screenshot import screenshot
from windows_functions.screenrecord import screenrecord
from windows_functions.shortcut_functions import shortcut_functions
from windows_functions.system_control import system_control


# Function to interact with the user and perform actions based on their commands
def take_query():
    # Initial greeting
    print("Sam: Hello sir, How may I help you?")
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
                print(
                    "Sam: Sir, it seems there is no internet connection. Please connect to the internet and try again")
                speak("Sir, it seems there is no internet connection. Please connect to the internet and try again")
                internet_connection_message_displayed = True  # Set the flag to True to indicate that the message has been displayed
            continue
        else:
            # Reset the flag when internet connection is available
            internet_connection_message_displayed = False

        if not sleeping:
            # Listen for user command
            query = listen()
            # query = "off battery saver in action centre"

            # Check if the user wants to wake up the assistant
            if "hey sam" in query:
                print("Sam: Yes sir, I'm awake")
                speak("Yes sir, I'm awake")
                continue

            # Check if the user wants the assistant to sleep
            elif "sleep" in query or "stop" in query:
                print("Sam: Going to sleep, sir")
                speak("Going to sleep sir")
                sleeping = True
                continue

        else:
            # Listen for wake-up phrase
            print("Say, hey Sam or wake up")
            wake_up_phrase = listen()
            if "hey sam" in wake_up_phrase or "wake up" in wake_up_phrase:
                print("Sam: Yes sir, I'm awake")
                speak("Yes sir, I'm awake")
                sleeping = False
                continue

        # Respond to specific queries
        # Tell the user the assistant's name
        if "tell me your name" in query:
            print("Sam: I am Sam. Your desktop Assistant")
            speak("I am Sam. Your desktop Assistant")

        # Exit the program
        elif "exit" in query:
            print("Sam: Exiting sir")
            speak("Exiting sir")
            exit()

        # Check if the user wants to turn on internet
        elif "on internet" in query and check_internet():
            print("Sam: Sir, the internet is already on.")
            speak("Sir the internet is already on")
            continue

        # Check if the user wants to turn off internet
        elif "off internet" in query and check_internet():
            # Display warning message
            print(
                "Sam: I'm sorry, sir, but I must warn you. You can't turn off the internet. My functions rely on an active internet connection to assist you effectively.")
            speak(
                "I'm sorry sir but I must warn you. You can't turn off the internet. My functions rely on an active internet connection to assist you effectively")
            continue

        # System controls
        elif "lock" in query or "sleep" in query or "sign out" in query or "restart" in query or "shutdown" in query:
            system_control(query)

        # Open settings
        elif "open settings" in query or "open setting" in query:
            open_settings(query)

        # Shortcuts
        elif any(shortcut in query for shortcut in
                 ["copy", "cut", "paste", "undo", "redo", "select all", "find", "save", "print", "new", "task view",
                  "switch apps", "minimize all", "show desktop", "snap window left", "snap window right",
                  "maximize window", "minimize window", "bold", "italic", "underline", "align left", "align center",
                  "align right", "open start menu", "open run dialog", "open power user menu",
                  "open system properties"]):
            shortcut_functions(query)

        # Open application
        elif "open" in query:
            open_application(query)

        # Close current application
        elif "close current window" in query:
            close_window()

        # Close application
        elif "close" in query:
            close_application(query)

        # Search the web
        elif "google search" in query:
            try:
                search_query = query.split("search ")[1]
                search_url = f"https://www.google.com/search?q={search_query}"
                speak(f"Searching the web for {search_query} sir")
                webbrowser.open(search_url)
            except IndexError:
                print("Sam: Please specify the search query, sir")
                speak("Please specify the search query sir")

        # Search on Wikipedia
        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            result = wikipedia.summary(query, sentences=4)
            print("Sam: According to wikipedia " + result)
            speak("According to wikipedia")
            speak(result)

        # Increase system volume
        elif "increase volume" in query:
            volume_up(1)

        # Decrease system volume
        elif "decrease volume" in query:
            volume_down(1)

        # UnMute
        elif "disable mute" in query:
            unmute_volume()

        # Mute
        elif "mute" in query:
            mute_volume()

        # Increase screen brightness
        elif "increase brightness" in query:
            increase_brightness(10)

        # Decrease screen brightness
        elif "decrease brightness" in query:
            decrease_brightness(10)

        # Check if the query mentions setting brightness to a specific level
        elif "set brightness" in query:
            # Extract the brightness level from the query
            try:
                brightness_str = next(word for word in query.split() if word.isdigit() or "%" in word)
                # Remove the "%" sign if present and convert to integer
                brightness_level = int(brightness_str.rstrip("%"))
                # Set the brightness to the extracted level
                set_brightness(brightness_level)
            except StopIteration:
                print("Sam: Sir, please specify the brightness level.")
                speak("Sir please specify the brightness level.")
            except ValueError:
                print("Sam: Sir, please provide a valid brightness level.")
                speak("Sir please provide a valid brightness level.")

        # Action Center
        # To show or hide action center
        elif "show action centre" in query or "hide action centre" in query:
            show_or_hide_action_center(query)

        # On action center toggle wi-fi
        elif "on wi-fi in action centre" in query or "off wi-fi in action centre" in query:
            toggle_wifi(query)

        # On action center show Bluetooth devices
        elif "show wifi networks in action centre" in query:
            action_center_show_wifi_networks()

        # On action center toggle Bluetooth
        elif "on bluetooth in action centre" in query or "off bluetooth in action centre" in query:
            toggle_bluetooth(query)

        # On action center show Bluetooth devices
        elif "show bluetooth devices in action centre" in query:
            action_center_show_bluetooth_devices()

        # On action center toggle airplane mode
        elif "on airplane mode in action centre" in query or "off airplane mode in action centre" in query:
            toggle_airplane_mode(query)

        # On action center toggle battery saver
        elif "on battery saver" in query or "off battery saver" in query:
            toggle_battery_saver(query)

        # On action center toggle night light mode
        elif "on night light in action centre" in query or "off night light in action centre" in query:
            toggle_night_light(query)

        # On action center toggle nearby sharing
        elif "on nearby sharing in action centre" in query or "on nearby share in action centre" in query:
            toggle_nearby_sharing(query)

        # Settings
        # Enable or disable Bluetooth in settings
        elif "on bluetooth in settings" in query or "off bluetooth in settings" in query:
            enable_or_disable_bluetooth(query)

        # On settings show Bluetooth devices
        elif "show bluetooth devices in settings" in query:
            settings_show_bluetooth_devices()

        # Enable or disable Airplane Mode in settings
        elif "on airplane mode in settings" in query or "off airplane mode in settings" in query:
            enable_or_disable_airplane_mode(query)

        # Enable or disable Night Light in settings
        elif "on night light in settings" in query or "off night light in settings" in query:
            enable_or_disable_night_light(query)

        # Enable or disable Do Not Disturb in settings
        elif "on do not disturb" in query or "off do not disturb" in query:
            enable_or_disable_do_not_disturb(query)

        # Enable or disable Nearby Share in settings
        elif "on nearby share in settings" in query or "off nearby share in settings" in query:
            enable_or_disable_nearby_share(query)

        # Enable or disable Wi-Fi in settings
        elif "on wi-fi in settings" in query or "off wi-fi in settings" in query:
            enable_or_disable_wifi(query)

        # Show available Wi-Fi networks in settings
        elif "show available wi-fi networks in settings" in query:
            settings_show_wifi_networks()

        # Enable or disable Hotspot in settings
        elif "on hotspot" in query or "off hotspot" in query:
            enable_or_disable_hotspot(query)

        # Enable or disable Light or Dark Mode in settings
        elif "on light mode" in query or "off light mode" in query or "on dark mode" in query or "off dark mode" in query:
            enable_or_disable_light_or_dark_mode(query)

        # Turn on or off Bluetooth
        elif "on bluetooth" in query or "off bluetooth" in query:
            turn_on_or_off_bluetooth(query)

        # Show Bluetooth devices
        elif "show bluetooth devices" in query:
            show_bluetooth_devices()

        # Turn on or off airplane mode
        elif "on airplane mode" in query or "off airplane mode" in query:
            turn_on_or_off_airplane_mode(query)

        # Turn on or off night light mode
        elif "on night light" in query or "off night light" in query:
            turn_on_or_off_night_light(query)

        # Turn on or off nearby sharing
        elif "on nearby sharing" in query or "on nearby share" in query:
            turn_on_or_off_nearby_sharing(query)

        # Turn on or off Wi-Fi
        elif "on wi-fi" in query or "off wi-fi" in query:
            enable_or_disable_wifi(query)

        # Show available Wi-Fi networks
        elif "show available wi-fi networks" in query:
            show_wifi_networks()

        # Camera
        # Take a photo
        elif "take a photo" in query:
            take_photo(query)

        # Start a video
        elif "start a video" in query:
            start_video()

        # Scan barcode
        elif "scan the barcode" in query:
            scan_barcode()

        # Screenshot
        elif "take a screenshot" in query:
            screenshot(query)

        # Screenrecord
        elif "record the screen" in query:
            screenrecord(query)

        # Screenrecord
        elif "record the screen" in query:
            screenrecord(query)

        # Search in Windows
        elif "windows search" in query:
            search_in_windows(query)


# Main function to initiate the assistant
if __name__ == '__main__':
    try:
        take_query()
    except Exception as e:
        print(e)
        print("Exiting")
