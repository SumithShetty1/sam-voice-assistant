from datetime import datetime
from sam_functions.speak import speak


def greet(query):
    try:
        # Get the current hour
        current_hour = datetime.now().hour

        # Determine the appropriate greeting based on the time of day
        if 5 <= current_hour < 12:
            greeting = "Good morning"
        elif 12 <= current_hour < 18:
            greeting = "Good afternoon"
        elif 18 <= current_hour < 22:
            greeting = "Good evening"
        else:
            greeting = "Good night"

        # Check if the query matches the greeting
        if "good morning" in query and greeting != "Good morning":
            speak(f"It's not morning anymore, but {greeting}, boss.")
        elif "good afternoon" in query and greeting != "Good afternoon":
            speak(f"It's not afternoon anymore, but {greeting}, boss.")
        elif "good night" in query and greeting != "Good night":
            speak(f"It's not night yet, but {greeting}, boss.")
        elif "hello" in query:
            speak(f"Hello, boss.")
        else:
            speak(f"{greeting}, boss.")

    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to greet you, boss.")
