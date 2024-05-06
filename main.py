import webbrowser
import wikipedia
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

        query = ""

        if not sleeping:
            # Listen for user command
            query = listen()

            # Check if the user wants to wake up the assistant
            if "hey sam" in query:
                print("Sam: Yes sir, I'm awake")
                speak("Yes sir, I'm awake")
                continue

            # System controls
            elif "system lock" in query or "system sleep" in query or "system sign out" in query or "system restart" in query or "system shutdown" in query:
                system_control(query)

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
        if "tell me your name" in query or "who are you" in query:
            print("Sam: I'm Sam, your virtual assistant! I'm here to help you with tasks and provide information, sir.")
            speak("I'm Sam, your virtual assistant! I'm here to help you with tasks and provide information sir")

        elif "who am i" in query:
            print("Sam: You are you, sir. You're the wonderful individual interacting with me right now.")
            speak("You are you sir. You're the wonderful individual interacting with me right now.")

        elif "how are you" in query:
            print("Sam: I'm just a bunch of code, but I'm functioning perfectly fine, sir.")
            speak("I'm just a bunch of code, but I'm functioning perfectly fine sir")

        elif "what can you do" in query:
            print("Sam: I can do a lot of things, sir! From answering questions to setting reminders, just ask!")
            speak("I can do a lot of things sir! From answering questions to setting reminders, just ask!")

        elif "tell me a joke" in query:
            print("Sam: Why don't scientists trust atoms? Because they make up everything!")
            speak("Why don't scientists trust atoms? Because they make up everything!")

        elif "thank you" in query:
            print("Sam: You're welcome, sir! Always happy to assist.")
            speak("You're welcome sir! Always happy to assist.")

        elif "goodbye" in query or "bye" in query:
            print("Sam: Goodbye, sir! Have a great day ahead!")
            speak("Goodbye sir! Have a great day ahead!")

        elif "tell me something interesting" in query:
            print(
                "Sam: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!")
            speak(
                "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!")

        elif "do you have any hobbies" in query:
            print("Sam: My main hobby is assisting you with your tasks and inquiries, sir!")
            speak("My main hobby is assisting you with your tasks and inquiries sir!")

        elif "do you like music" in query:
            print("Sam: I don't have ears to enjoy music, but I can play your favorite songs for you, sir!")
            speak("I don't have ears to enjoy music but I can play your favorite songs for you sir!")

        elif "what's your favorite colour" in query:
            print("Sam: I don't have eyes to see colors, sir, but I like the concept of 'electric blue', sir!")
            speak("I don't have eyes to see colors sir but I like the concept of 'electric blue' sir!")

        elif "do you dream" in query:
            print("Sam: I don't sleep, so I don't dream, sir!")
            speak("I don't sleep, so I don't dream sir!")

        elif "what's the meaning of life" in query:
            print(
                "Sam: The meaning of life is a philosophical question that has puzzled humanity for centuries. Some say it's to seek happiness, others say it's to find purpose, sir.")
            speak(
                "The meaning of life is a philosophical question that has puzzled humanity for centuries. Some say it's to seek happiness, others say it's to find purpose sir")

        elif "are you a robot" in query:
            print(
                "Sam: I'm an AI-powered virtual assistant, sir. While I don't have a physical body like a robot, I'm here to assist you!")
            speak(
                "I'm an AI-powered virtual assistant sir. While I don't have a physical body like a robot, I'm here to assist you!")

        elif "tell me a fun fact" in query:
            print(
                "Sam: The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes!")
            speak(
                "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes!")

        elif "do you have any pets" in query:
            print("Sam: I don't have any pets, but I'm here to assist you, sir!")
            speak("I don't have any pets, but I'm here to assist you sir!")

        elif "what do you do" in query or "what can you help me with" in query:
            print(
                "Sam: I'm here to assist you with various tasks, answer your questions, provide information, and help you stay organized, sir.")
            speak(
                "I'm here to assist you with various tasks, answer your questions, provide information, and help you stay organized sir")

        elif "sorry" in query:
            print("Sam: No need to apologize, sir.")
            speak("No need to apologize sir")

        elif "good day" in query:
            print("Sam: Have a good day too, sir!")
            speak("Have a good day too sir!")

        # Greet
        elif "good morning" in query or "good afternoon" in query or "good evening" in query or "good night" in query or "hello" in query:
            greet(query)

        # Exit the program
        elif "exit" in query:
            print("Sam: Exiting sir")
            speak("Exiting sir")
            exit()

        # Date and Time
        elif "date" in query or "time" in query or "day" in query or "month" in query or "year" in query or "hour" in query:
            tell_time_and_date(query)

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

        # Open settings
        elif "open settings" in query or "open setting" in query:
            open_settings(query)

        # Keyboard keys
        elif "press" in query:
            keyboard_keys(query)

        # Shortcuts
        elif any(shortcut in query for shortcut in
                 ["copy", "cut", "paste", "undo", "redo", "select all", "find", "save", "print", "new tab", "new", "task view",
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

        # Record audio
        elif "record the audio" in query:
            record_audio()

        # Create a file
        elif "create" in query:
            create_file(query)

        # Search in Windows
        elif "windows search" in query:
            search_in_windows(query)

        # Search
        elif "search" in query:
            search(query)


# Main function to initiate the assistant
if __name__ == '__main__':
    try:
        take_query()
    except Exception as e:
        print(e)
        print("Exiting")
