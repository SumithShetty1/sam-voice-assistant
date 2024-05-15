import wikipedia
from sam_functions.speak import speak
import eel


def wikipedia_functions(query):
    speak("Checking Wikipedia...")

    # Remove the specific phrases and clean up the query
    if "what is" in query:
        updated_query = query.replace("what is", "").strip()
    elif "explain" in query:
        updated_query = query.replace("explain", "").strip()
    elif "from wikipedia" in query:
        updated_query = query.replace("wikipedia", "").strip()

    try:
        if "what is" in query:
            result = wikipedia.summary(updated_query, sentences=2)
            speak("According to Wikipedia")
            speak(result)
        elif "explain" in query:
            result = wikipedia.summary(updated_query, sentences=6)
            speak("Please check the chat box boss")
            eel.receiverText(result)

    except wikipedia.exceptions.DisambiguationError as e:
        pass
        speak("The query is ambiguous, please be more specific.")
    except wikipedia.exceptions.PageError:
        pass
        speak("The page does not exist on Wikipedia.")
    except Exception as e:
        pass
        speak("An error occurred while retrieving information from Wikipedia.")
