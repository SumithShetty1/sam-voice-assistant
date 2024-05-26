import wikipedia
from sam_functions.speak import speak
import eel


def wikipedia_functions(query, intent_data):
    speak("Checking Wikipedia...")

    # Remove the specific phrases and clean up the query
    search_query = None

    for prep in intent_data['text']:
        if prep in query:
            # Extract search query from the query based on the preposition
            parts = query.split(prep)
            if len(parts) > 1:
                search_query = parts[1].strip()
            break

    # Check if 'search_query' is extracted and perform necessary replacements
    if search_query:
        # Remove specific phrases like "explain", "from wikipedia"
        search_query = search_query.replace("explain", "").replace("from wikipedia", "").strip()

    # If the search query is empty after processing, handle accordingly
    if not search_query:
        speak("Please specify what you would like to search on Wikipedia.")
        return

    try:
        if "explain" in query or "describe" in query or "clarify" in query:
            result = wikipedia.summary(search_query, sentences=6)
            speak("Please check the chat box sir")
            eel.receiverText(result)
        else:
            result = wikipedia.summary(search_query, sentences=2)
            speak("According to Wikipedia")
            speak(result)

    except wikipedia.exceptions.DisambiguationError as e:
        pass
        speak("The query is ambiguous, please be more specific.")
    except wikipedia.exceptions.PageError:
        pass
        speak("The page does not exist on Wikipedia.")
    except Exception as e:
        pass
        speak("An error occurred while retrieving information from Wikipedia.")
