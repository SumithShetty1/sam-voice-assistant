import pyautogui
import time
from sam_functions.speak import speak
from check_functions import check_dark_mode


# Bluetooth
# Function to check if bluetooth is already on
def is_file_explorer_open():
    try:
        # Check if the Bluetooth icon is present in the screenshot
        if not check_dark_mode():
            pyautogui.locateOnScreen("images/light_mode/file_explorer/search_icon.png", confidence=0.9)
        else:
            pyautogui.locateOnScreen("images/dark_mode/file_explorer/search_icon.png", confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        print("Sam: An error occurred:", e)


def search_bar(query):
    try:
        search_query = query.split("search ")[1]

        if is_file_explorer_open():
            # Press Ctrl + F to focus on the search
            pyautogui.hotkey("ctrl", "f")
            time.sleep(1)  # Add a short delay to ensure the search box opens

            # Type the search query
            pyautogui.write(search_query)

            # Display assistant's message
            print(f"Sam: Searching for '{search_query}', sir")
            speak(f"Searching for '{search_query}' sir")
            return

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
            # Press Windows key + S to open the search box
            pyautogui.hotkey('win', 's')
            time.sleep(1)  # Add a short delay to ensure the search box opens

            # Type the search query
            pyautogui.write(search_query)

            # Display assistant's message
            print(f"Sam: Searching for '{search_query}', sir")
            speak(f"Searching for '{search_query}' sir")

    except IndexError:
        print("Sam: Please specify the search query, sir")
        speak("Please specify the search query sir")

    except Exception as e:
        print(f"Sam: Error performing search: {e}")
        print("Sam: Sorry, I couldn't perform the search, sir")
        speak("Sorry I couldn't perform the search sir")
