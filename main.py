import webbrowser
import wikipedia
from check_functions import check_internet
from sam_functions import takeCommand, speak
from app_functions import open_application, close_application, close_window
from volume_functions import volume_up, volume_down, mute_volume, unmute_volume
from brightness_functions import increase_brightness, decrease_brightness
from actioncenter_functions import show_or_hide_action_center, toggle_bluetooth, action_center_show_bluetooth_devices, \
    toggle_airplane_mode, toggle_battery_saver, toggle_night_light, toggle_nearby_sharing
from windows_search_functions import search_in_windows


# Function to turn off Wi-Fi
def turn_off_internet():
    # Display warning message
    print(
        "Sam: Warning! You cannot turn off Internet or Wi-Fi. This assistant requires an internet connection to function properly, sir")
    speak(
        "Warning! You cannot turn off Internet or Wi-Fi. This assistant requires an internet connection to function properly sir")


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
            query = takeCommand()
            # query = "off battery saver in action center"

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
            wake_up_phrase = takeCommand()
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

        # Check if the user wants to turn off Wi-Fi
        elif "turn off internet" in query or "turn off wi-fi" in query:
            turn_off_internet()
            continue

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
        elif "from google search" in query:
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

        # To show or hide action center
        elif "show action centre" in query or "hide action centre" in query:
            show_or_hide_action_center(query)

        # On action center toggle Bluetooth
        elif "on bluetooth in action center" in query or "off bluetooth in action center" in query:
            toggle_bluetooth(query)

        # On action center show Bluetooth devices
        elif "show bluetooth devices in action center" in query:
            action_center_show_bluetooth_devices()

        # On action center toggle airplane mode
        elif "on airplane mode in action center" in query or "off airplane mode in action center" in query:
            toggle_airplane_mode(query)

        # On action center toggle battery saver
        elif "on battery saver in action center" in query or "off battery saver in action center" in query:
            toggle_battery_saver(query)

        # On action center toggle night light mode
        elif "on night light in action center" in query or "off night light in action center" in query:
            toggle_night_light(query)

        # On action center toggle nearby sharing
        elif "on nearby sharing in action center" in query or "on nearby share in action center" in query:
            toggle_nearby_sharing(query)

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
