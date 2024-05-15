import time
import pyautogui
from sam_functions.speak import speak


def search_in_windows(query):
    try:
        search_query = query.split("search ")[1]
        # Press Windows key + S to open the search box
        pyautogui.hotkey('win', 's')
        time.sleep(1)  # Add a short delay to ensure the search box opens

        # Type the search query
        pyautogui.write(search_query, interval=0.1)  # Adjust interval as needed for typing speed
        # Press Enter to perform the search
        pyautogui.press('enter')

        # Display assistant's message
        speak(f"Searching for '{query}', boss")
    except IndexError:
        speak("Please specify the search query, boss")
    except Exception as e:
        speak("Error performing search")
        speak("Sorry, I couldn't perform search, boss")
