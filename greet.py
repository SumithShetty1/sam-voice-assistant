from datetime import datetime
from sam_functions.speak import speak


def greet(query, intent_data):
    try:
        # Detect the entity in the query
        detected_entity = next((entity for entity in intent_data.get('entities', []) if entity in query.lower()), None)

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
            speak(f"{greeting} sir.")
        elif detected_entity == "afternoon" and greeting == "Good afternoon":
            speak(f"{greeting} sir.")
        elif detected_entity == "night" and greeting == "Good evening":
            speak(f"Good night sir.")
        elif detected_entity == "evening" and greeting == "Good evening":
            speak(f"{greeting} sir.")
        elif detected_entity == "morning" and greeting != "Good morning":
            speak(f"It's not morning anymore, but {greeting} sir.")
        elif detected_entity == "afternoon" and greeting != "Good afternoon":
            speak(f"It's not afternoon anymore, but {greeting} sir.")
        elif detected_entity == "night" and greeting != "Good evening":
            speak(f"It's not night yet, but Good night sir.")
        elif detected_entity == "evening" and greeting != "Good evening" and greeting == "Good afternoon":
            speak(f"It's not evening yet, but {greeting} sir.")
        elif detected_entity == "evening" and greeting != "Good evening":
            speak(f"It's not evening anymore, but {greeting} sir.")
        else:
            # Use a random response from the JSON data
            from random import choice
            response = choice(intent_data["responses"])
            speak(response)

    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to greet you sir.")
