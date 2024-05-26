import time
import pyautogui
from sam_functions.speak import speak


def search_in_windows(query, intent_data):
    try:
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
            # Remove specific phrases
            search_query = search_query.replace("search", "").replace("windows", "").strip()

        # Press Windows key + S to open the search box
        pyautogui.hotkey('win', 's')
        time.sleep(1)  # Add a short delay to ensure the search box opens

        # Type the search query
        pyautogui.write(search_query)
        # Press Enter to perform the search
        pyautogui.press('enter')

        # Display assistant's message
        speak(f"Searching for '{search_query}' sir")
    except IndexError:
        speak("Please specify the search query sir")
    except Exception as e:
        speak("Error performing search")
        speak("Sorry, I couldn't perform search sir")
