import requests  # Import requests module for checking internet connectivity
import speech_recognition as sr
import webbrowser
import wikipedia
from sam_functions import speak, open_application, close_application, volume_up, volume_down, mute_volume, \
    unmute_volume, increase_brightness, decrease_brightness


# Function to capture user's voice command
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        # Set energy threshold for ambient noise levels
        r.energy_threshold = 4000
        # Set the pause threshold to determine the end of a phrase
        # r.pause_threshold = 0.7

        try:
            audio = r.listen(source)
            print("Recognizing...")
            # Recognize speech using Google Speech Recognition
            query = r.recognize_google(audio, language='en-in')
            print(f"Me: {query}")
            return query
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
        except Exception:
            return "None"


# Function to check internet connectivity
def check_internet():
    try:
        requests.get('http://www.google.com', timeout=3)  # Attempt to make a request to Google
        return True
    except requests.ConnectionError:
        return False


# Function to interact with the user and perform actions based on their commands
def take_query():
    # Initial greeting
    print("Sam: Hello sir, How may I help you?")
    speak("Hello sir, How may I help you?")

    # Initialize the sleeping state
    sleeping = False

    # Loop to continuously listen for user commands
    while True:
        # Check internet connectivity
        if not check_internet():
            print("Sam: Sir, it seems there is no internet connection. Please connect to the internet and try again.")
            continue

        if not sleeping:
            # Listen for user command
            query = takeCommand()

            # Check if the user wants to wake up the assistant
            if "hey sam" in query:
                print("Sam: Yes sir, I'm awake.")
                speak("Yes sir, I'm awake.")
                continue

            # Check if the user wants the assistant to sleep
            elif "sleep" in query or "stop" in query:
                print("Sam: Going to sleep.")
                speak("Going to sleep.")
                sleeping = True
                continue

        else:
            # Listen for wake-up phrase
            print("Say, hey Sam or wake up")
            wake_up_phrase = takeCommand()
            if "hey sam" in wake_up_phrase or "wake up" in wake_up_phrase:
                print("Sam: Yes sir, I'm awake.")
                speak("Yes sir, I'm awake.")
                sleeping = False
                continue

        # Respond to specific queries
        # Tell the user the assistant's name
        if "tell me your name" in query:
            print("Sam: I am Sam. Your desktop Assistant")
            speak("I am Sam. Your desktop Assistant")

        # Exit the program
        elif "exit" in query:
            speak("Exiting sir")
            print("Sam: Exiting sir")
            exit()

        # Launching the application
        elif "open" in query:
            try:
                app = query.split("open ")[1]
                open_application(app)
            except IndexError:
                print("Sam: Please specify the application to open sir.")
                speak("Please specify the application to open sir.")

        # Close current application
        elif "close" in query:
            try:
                app_to_close = query.split("close ")[1]
                close_application(app_to_close)
            except IndexError:
                print("Sam: Please specify the application to close sir.")
                speak("Please specify the application to close sir.")

        # Search the web
        elif "search" in query:
            try:
                search_query = query.split("search ")[1]
                search_url = f"https://www.google.com/search?q={search_query}"
                speak(f"Searching the web for {search_query}")
                webbrowser.open(search_url)
            except IndexError:
                print("Sam: Please specify the search query sir.")
                speak("Please specify the search query sir.")

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


# Main function to initiate the assistant
if __name__ == '__main__':
    take_query()
