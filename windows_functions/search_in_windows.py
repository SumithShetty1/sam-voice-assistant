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
        pyautogui.write(search_query)
        # Press Enter to perform the search
        pyautogui.press('enter')

        # Display assistant's message
        print(f"Sam: Searching for '{search_query}', sir")
        speak(f"Searching for '{search_query}' sir")
    except IndexError:
        print("Sam: Please specify the search query, sir")
        speak("Please specify the search query sir")
    except Exception as e:
        print(f"Sam: Error performing search: {e}")
        print("Sam: Sorry, I couldn't perform search, sir")
        speak("Sorry, I couldn't perform search sir")
