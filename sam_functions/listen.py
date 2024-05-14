import speech_recognition as sr
import eel


# Function to capture user's voice command
def listen():
    # Creating a Recognizer instance
    r = sr.Recognizer()

    # Using the microphone as the audio source
    with sr.Microphone() as source:
        eel.DisplayMessage('Listening...')

        r.adjust_for_ambient_noise(source)

        try:
            # Listening for audio input from the user
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            eel.DisplayMessage('Recognizing...')

            # Recognize speech using Google Speech Recognition
            query = r.recognize_google(audio, language='en-in')

            eel.DisplayMessage(query)
            eel.senderText(query)
            query = query.lower()  # Convert the text to lowercase
            return query
        except KeyboardInterrupt:
            eel.close_window()
            exit()
        except Exception:
            return ""
