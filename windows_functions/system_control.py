import time
import pyautogui
from sam_functions.speak import speak


def system_control(query):
    try:
        if 'lock' in query:
            speak("Locking the system, boss.")
            pyautogui.hotkey('win', 'l')
            exit()

        if 'sleep' in query:
            speak("Putting the system to sleep, boss.")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('left')
            time.sleep(0.2)
            pyautogui.press('enter')
            exit()

        if 'sign out' in query:
            speak("Signing out, boss.")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('left')
            time.sleep(0.2)
            pyautogui.press('left')
            time.sleep(0.2)
            pyautogui.press('enter')
            exit()

        if 'restart' in query:
            speak("Restarting the system, boss.")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('right')
            time.sleep(0.2)
            pyautogui.press('enter')
            exit()

        if 'shutdown' in query:
            speak("Shutting down the system, boss.")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('enter')
            exit()
    except Exception as e:
        speak(f"An error occurred")
        speak("Oops! Something went wrong while performing the system control command, boss.")
