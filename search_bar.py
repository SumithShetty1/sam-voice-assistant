import pyautogui
import time
from sam_functions.speak import speak


def search_bar(query):
    try:
        search_query = query.split("search ")[1]

        # Take a screenshot before pressing Ctrl+L
        before_screenshot = pyautogui.screenshot()

        # Press Ctrl + L to focus on the address bar in Chrome
        pyautogui.hotkey("ctrl", "l")
        time.sleep(1)  # Add a short delay to ensure the search box opens

        # Take a screenshot after pressing Ctrl+L
        after_screenshot = pyautogui.screenshot()

        # Check if there is any change in the screen after pressing Ctrl+L
        if before_screenshot != after_screenshot:
            # Type the search query
            pyautogui.write(search_query)
            # Press Enter to perform the search
            pyautogui.press('enter')

            # Display assistant's message
            print(f"Sam: Searching for '{search_query}', sir")
            speak(f"Searching for '{search_query}' sir")
        else:
            print("Sam: Unable to access the search bar, sir")
            speak("Unable to access the search bar sir")

    except IndexError:
        print("Sam: Please specify the search query, sir")
        speak("Please specify the search query sir")

    except Exception as e:
        print(f"Sam: Error performing search: {e}")
        print("Sam: Sorry, I couldn't perform the search, sir")
        speak("Sorry I couldn't perform the search sir")
