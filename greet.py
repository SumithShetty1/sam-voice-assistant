from datetime import datetime
from sam_functions.speak import speak


def greet(intent_data):
    try:
        # Check if the determined greeting matches any entity
        detected_entity = None

        if intent_data["detected_entities"] != []:
            detected_entity = intent_data["detected_entities"]

        # Get the current hour
        current_hour = datetime.now().hour

        # Determine the appropriate greeting based on the time of day
        if 0 <= current_hour < 12:
            greeting = "Good morning"
        elif 12 <= current_hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        # Respond based on the detected entity and the current time of day
        if detected_entity == "morning" and greeting == "Good morning":
            speak(f"{greeting} boss.")
        elif detected_entity == "afternoon" and greeting == "Good afternoon":
            speak(f"{greeting} boss.")
        elif detected_entity == "night" and greeting == "Good evening":
            speak(f"Good night boss.")
        elif detected_entity == "evening" and greeting == "Good evening":
            speak(f"{greeting} boss.")
        if detected_entity == "morning" and greeting != "Good morning":
            speak(f"It's not morning anymore, but {greeting} boss.")
        elif detected_entity == "afternoon" and greeting != "Good afternoon":
            speak(f"It's not afternoon anymore, but {greeting} boss.")
        elif detected_entity == "night" and greeting != "Good evening":
            speak(f"It's not night yet, but Good night boss.")
        elif detected_entity == "evening" and greeting != "Good evening":
            speak(f"It's not evening anymore, but {greeting} boss.")
        else:
            # Use a random response from the JSON data
            from random import choice
            response = choice(intent_data["responses"])
            speak(response)

    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to greet you boss.")
