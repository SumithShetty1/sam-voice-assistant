import requests
import webbrowser
import wikipedia
from sam_functions import takeCommand, speak
from app_functions import open_application, close_application, close_window
from volume_functions import volume_up, volume_down, mute_volume, unmute_volume
from brightness_functions import increase_brightness, decrease_brightness
from actioncenter_functions import show_or_hide_action_center, turn_on_or_off_bluetooth, show_bluetooth_devices, \
    turn_on_or_off_airplane_mode, turn_on_or_off_battery_saver, turn_on_or_off_night_light, \
    turn_on_or_off_nearby_sharing
from windows_search_functions import search_in_windows

# Function to check internet connectivity
def check_internet():
    try:
        requests.get('http://www.google.com', timeout=3)  # Attempt to make a request to Google
        return True
    except requests.ConnectionError:
        return False


# Function to turn off Wi-Fi
def turn_off_internet():
    # Display warning message
    print("Sam: Warning! You cannot turn off Internet or Wi-Fi. This assistant requires an internet connection to function properly, sir")
    speak("Warning! You cannot turn off Internet or Wi-Fi. This assistant requires an internet connection to function properly sir")


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
                print("Sam: Sir, it seems there is no internet connection. Please connect to the internet and try again")
                speak("Sir, it seems there is no internet connection. Please connect to the internet and try again")
                internet_connection_message_displayed = True  # Set the flag to True to indicate that the message has been displayed
            continue
        else:
            # Reset the flag when internet connection is available
            internet_connection_message_displayed = False

        if not sleeping:
            # Listen for user command
            # query = takeCommand()
            query = "on bluetooth quickly"

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

        # Quickly toggle Bluetooth
        elif "on bluetooth quickly" in query or "off bluetooth quickly" in query:
            turn_on_or_off_bluetooth(query)

        # Quickly show Bluetooth devices
        elif "show bluetooth devices quickly" in query:
            show_bluetooth_devices()

        # Quickly toggle airplane mode
        elif "on airplane mode quickly" in query or "off airplane mode quickly" in query:
            turn_on_or_off_airplane_mode(query)

        # Quickly toggle battery saver
        elif "on battery saver quickly" in query or "off battery saver quickly" in query:
            turn_on_or_off_battery_saver()

        # Quickly toggle night light mode
        elif "on night light quickly" in query or "off night light quickly" in query:
            turn_on_or_off_night_light()

        # Quickly toggle nearby sharing
        elif "on nearby share quickly" in query or "on nearby share quickly" in query:
            turn_on_or_off_nearby_sharing()

    # Search in Windows
        elif "windows search" in query:
            search_in_windows(query)


# Main function to initiate the assistant
if __name__ == '__main__':
    take_query()
