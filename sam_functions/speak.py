import pyttsx3


# Function to convert text to speech
def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Speak the provided audio
    engine.say(audio)
    # Blocks while processing all the currently queued commands
    engine.runAndWait()