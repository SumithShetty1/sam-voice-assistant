import speech_recognition as sr
import pyttsx3


# Function to capture user's voice command
def takeCommand():
    # Creating a Recognizer instance
    r = sr.Recognizer()

    # Using the microphone as the audio source
    with sr.Microphone() as source:
        print('Listening...')
        # Set energy threshold for ambient noise levels
        r.energy_threshold = 4000
        # Set the pause threshold to determine the end of a phrase
        # r.pause_threshold = 0.7

        try:
            # Listening for audio input from the user
            audio = r.listen(source)
            print("Recognizing...")
            # Recognize speech using Google Speech Recognition
            query = r.recognize_google(audio, language='en-in')
            print(f"Me: {query}")
            query = query.lower()  # Convert the text to lowercase
            return query
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
        except Exception:
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
