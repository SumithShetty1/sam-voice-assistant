import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import wikipedia
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

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
        except Exception as e:
            return "None"

# Function to convert text to speech
def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Speak the provided audio
    engine.say(audio)
    # Blocks while processing all the currently queued commands
    engine.runAndWait()

# Function to increase volume
def volume_up(step):
    devices = AudioUtilities.GetSpeakers()  # Get the speakers' devices
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Activate the interface for the audio endpoint volume
    volume = cast(interface, POINTER(IAudioEndpointVolume))  # Cast the interface to an audio endpoint volume pointer
    current_volume = volume.GetMasterVolumeLevel()  # Get the current master volume level
    max_volume = 0
    new_volume = min(current_volume + step, max_volume)
    # Check if the new volume is equal to the current volume
    if new_volume == current_volume:
        # Speak and print a message indicating that the volume is already at its maximum
        speak("Volume is already at its maximum.")
        print("Volume is already at its maximum.")
    else:
        # Set the master volume level to the new volume
        volume.SetMasterVolumeLevel(new_volume, None)
        speak("Volume increased.")
        print("Volume increased.")

# Function to decrease volume
def volume_down(step):
    devices = AudioUtilities.GetSpeakers()   # Get the speakers' devices
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Activate the interface for the audio endpoint volume
    volume = cast(interface, POINTER(IAudioEndpointVolume))  # Cast the interface to an audio endpoint volume pointer
    current_volume = volume.GetMasterVolumeLevel()
    min_volume = -65.25
    new_volume = max(current_volume - step, min_volume)
    # Check if the absolute difference between the new volume and the current volume is very small
    if abs(new_volume - current_volume) < 0.01:  # Using a tolerance threshold for comparison
        print('Volume is already at its minimum.')
    else:
        # Set the master volume level to the new volume
        volume.SetMasterVolumeLevel(new_volume, None)
        print("Volume decreased.")
        speak("Volume decreased.")

# Function to mute volume
def mute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get the current mute status
    is_muted = volume.GetMute()
    # Check if volume is not already muted
    if not is_muted:
        # Mute volume
        volume.SetMute(1, None)
        print("Volume muted.")
        speak("Volume muted.")
    else:
        print("Volume is already muted.")
        speak("Volume is already muted.")

# Function to unmute volume
def unmute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get the current mute status
    is_muted = volume.GetMute()
    # Check if volume is currently muted
    if is_muted:
        # Unmute volume
        volume.SetMute(0, None)
        print("Volume unmuted.")
        speak("Volume unmuted.")
    else:
        print("Volume is already unmuted.")
        speak("Volume is already unmuted.")

# Function to increase brightness
def increase_brightness(step):
    # Get the current brightness level
    current_brightness = sbc.get_brightness()[0]  # Access the first brightness level
    max_brightness = 100  # Maximum brightness level
    new_brightness = min(current_brightness + step, max_brightness)
    # Check if the brightness is already at its maximum
    if new_brightness == current_brightness:
        print("Brightness is already at its maximum.")
        speak("Brightness is already at its maximum.")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        print("Brightness increased.")
        speak("Brightness increased.")

# Function to decrease brightness
def decrease_brightness(step):
    # Get the current brightness level
    current_brightness = sbc.get_brightness()[0]  # Access the first brightness level
    min_brightness = 0  # Minimum brightness level
    new_brightness = max(current_brightness - step, min_brightness)
    # Check if the brightness is already at its minimum
    if new_brightness == current_brightness:
        print("Brightness is already at its minimum.")
        speak("Brightness is already at its minimum.")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        print("Brightness decreased.")
        speak("Brightness decreased.")

# Function to interact with the user and perform actions based on their commands
def take_query():
    # Initial greeting
    print("Sam: Hello sir, How may I help you?")
    speak("Hello sir, How may I help you?")

    # Initialize the sleeping state
    sleeping = False

    # Loop to continuously listen for user commands
    while True:
        if not sleeping:
            # Listen for user command
            query = takeCommand()

            # Check if the user wants to wake up the assistant
            if "hey sam" in query:
                speak("Yes sir, I'm awake.")
                continue

            # Check if the user wants the assistant to sleep
            elif "sleep" in query or "stop" in query:
                speak("Going to sleep.")
                sleeping = True
                continue

        else:
            # Listen for wake-up phrase
            wake_up_phrase = takeCommand()
            if "hey sam" or "sam" in wake_up_phrase:
                speak("Yes sir, I'm awake.")
                sleeping = False
                continue

        # Respond to specific queries
        # Tell the user the assistant's name
        if "tell me your name" in query:
            speak("Sam: I am Sam. Your desktop Assistant")

        # Exit the program
        elif "exit" in query:
            speak("Exiting sir")
            exit()

        # Launching the application
        elif "open" in query:
            app = query.split("open ")[1]
            try:
                os.system(f'start {app}.exe')
                speak(f"Opening {app} sir")
            except Exception as e:
                print(e)
                speak(f"Sorry, I couldn't open {app} sir")

        # Search the web
        elif "search" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://www.google.com/search?q={search_query}"
            speak(f"Searching the web for {search_query}")
            webbrowser.open(search_url)

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