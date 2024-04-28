import time
import pyautogui
from sam_functions.speak import speak


def system_control(query):
    try:
        if 'lock' in query:
            print("Sam: Locking the system, sir.")
            speak("Locking the system sir")
            pyautogui.hotkey('win', 'l')
            exit()

        if 'sleep' in query:
            print("Sam: Putting the system to sleep, sir.")
            speak("Putting the system to sleep sir")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('left')
            time.sleep(0.2)
            pyautogui.press('enter')
            exit()

        if 'sign out' in query:
            print("Sam: Signing out, sir.")
            speak("Signing out sir")
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
            print("Sam: Restarting the system, sir.")
            speak("Restarting the system sir")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('right')
            time.sleep(0.2)
            pyautogui.press('enter')
            exit()

        if 'shutdown' in query:
            print("Sam: Shutting down the system, sir.")
            speak("Shutting down the system sir")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('enter')
            exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Oops! Something went wrong while performing the system control command, sir.")
        speak("Oops! Something went wrong while performing the system control command sir")
