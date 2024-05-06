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
            print(f"Sam: It's not morning anymore, but {greeting}, sir.")
            speak(f"It's not morning anymore but {greeting} sir")
        elif "good afternoon" in query and greeting != "Good afternoon":
            print(f"Sam: It's not afternoon anymore, but {greeting}, sir.")
            speak(f"It's not afternoon anymore but {greeting} sir")
        elif "good night" in query and greeting != "Good night":
            print(f"Sam: It's not night yet, but {greeting}, sir.")
            print(f"It's not night yet but {greeting} sir")
        elif "hello" in query:
            print(f"Sam: Hello, sir.")
            speak(f"Hello sir")
        else:
            print(f"Sam: {greeting}, sir.")
            speak(f"{greeting} sir")

    except Exception as e:
        print(f"Sam: An error occurred: {e}")
        print("Sam: Oops! Something went wrong while trying to greet you, sir.")
        speak("Oops! Something went wrong while trying to greet you sir")
