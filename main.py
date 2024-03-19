import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import wikipedia
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Function to capture user's voice command
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        # r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Me: {query}")
        except Exception as e:
            return "None"

        return query

# Function to convert text to speech
def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(audio)
    engine.runAndWait()

# Function to increase volume
def volume_up(step):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(current_volume + step, None)

# Function to decrease volume
def volume_down(step):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(current_volume - step, None)

# Function to interact with the user and perform actions based on their commands
def take_query():
    print("Sam: Hello sir. How may I help you")
    speak("Hello sir. How may I help you")

    sleeping = False
    while True:
        if not sleeping:
            query = takeCommand()

            if "hey sam" in query:
                speak("Yes sir, I'm awake.")
                continue

            elif "sleep" in query or "stop" in query:
                speak("Going to sleep.")
                sleeping = True
                continue

        else:
            wake_up_phrase = takeCommand()
            if "hey sam" or "sam" in wake_up_phrase:
                speak("Yes sir, I'm awake.")
                sleeping = False
                continue

        if "tell me your name" in query:
            speak("Sam: I am Sam. Your desktop Assistant")

        # This will exit and terminate the program
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

        # Searching the web
        elif "search" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://www.google.com/search?q={search_query}"
            speak(f"Searching the web for {search_query}")
            webbrowser.open(search_url)

        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            result = wikipedia.summary(query, sentences=4)
            print("Sam: According to wikipedia " + result)
            speak("According to wikipedia")
            speak(result)

        # Adjusting system volume
        elif "increase volume" in query:
            volume_up(1)
            speak("Volume increased")

        elif "decrease volume" in query:
            volume_down(1)
            speak("Volume decreased")

# Main function to initiate the assistant
if __name__ == '__main__':
    take_query()