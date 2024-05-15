import time
import pyautogui
from sam_functions.speak import speak


# Function to start audio recording
def record_audio():
    try:
        # Open Sound Recorder using Windows search
        pyautogui.hotkey('win')
        time.sleep(0.5)
        pyautogui.typewrite('Sound Recorder')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(2)  # Wait for Sound Recorder to open

        # Say "Recording audio in 3 seconds"
        speak("Audio recording will start in 3 seconds, boss.")
        time.sleep(3)

        # Press Ctrl+R to start recording
        pyautogui.hotkey('ctrl', 'r')

    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to record audio.")
