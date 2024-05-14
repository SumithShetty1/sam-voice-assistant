import pyttsx3
import eel


# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    eel.DisplayMessage(text)

    # Speak the provided audio
    engine.say(text)

    eel.receiverText(text)

    # Blocks while processing all the currently queued commands
    engine.runAndWait()
