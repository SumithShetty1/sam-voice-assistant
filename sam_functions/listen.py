import speech_recognition as sr


# Function to capture user's voice command
def listen():
    # Creating a Recognizer instance
    r = sr.Recognizer()
    # Set energy threshold for ambient noise levels
    r.energy_threshold = 4000

    # Using the microphone as the audio source
    with sr.Microphone() as source:
        print('Listening...')
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
            return ""
