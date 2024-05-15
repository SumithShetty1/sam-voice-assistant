import pyautogui
from sam_functions.speak import speak


# Function perform various keyboard shortcuts and actions based on the provided query
def shortcut_functions(query):
    try:
        # Combined actions
        if 'select all' in query and 'copy' in query:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            speak("All selected and copied, boss.")
            return
        if 'select all' in query and 'cut' in query:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'x')
            speak("All selected and cut, boss.")
            return

        # Keyboard shortcuts
        if 'copy' in query:
            pyautogui.hotkey('ctrl', 'c')
            speak("Copied, boss.")
            return
        if 'cut' in query:
            pyautogui.hotkey('ctrl', 'x')
            speak("Cut, boss.")
            return
        if 'paste' in query:
            pyautogui.hotkey('ctrl', 'v')
            speak("Pasted, boss.")
            return
        if 'undo' in query:
            pyautogui.hotkey('ctrl', 'z')
            speak("Undone, boss.")
            return
        if 'redo' in query:
            pyautogui.hotkey('ctrl', 'y')
            speak("Redone, boss.")
            return

        if 'select all' in query:
            pyautogui.hotkey('ctrl', 'a')
            speak("All selected, boss.")
            return

            # Other shortcuts
        if 'find' in query:
            pyautogui.hotkey('ctrl', 'f')
            speak("Find activated, boss.")
            return
        if 'save' in query:
            pyautogui.hotkey('ctrl', 's')
            speak("Saved, boss.")
            return
        if 'print' in query:
            pyautogui.hotkey('ctrl', 'p')
            speak("Printed, boss.")
            return

        if 'new tab' in query:
            pyautogui.hotkey('ctrl', 't')
            speak("New tab opened, boss.")
            return

        if 'new' in query:
            pyautogui.hotkey('ctrl', 'n')
            speak("New document opened, boss.")
            return

        # Window management shortcuts
        if 'task view' in query:
            pyautogui.hotkey('win', 'tab')
            speak("Task View activated, boss.")
            return
        if 'switch apps' in query:
            pyautogui.hotkey('alt', 'tab')
            speak("Switched apps, boss.")
            return
        if 'minimize all' in query:
            pyautogui.hotkey('win', 'm')
            speak("Minimized all windows, boss.")
            return
        if 'show desktop' in query:
            pyautogui.hotkey('win', 'd')
            speak("Showed desktop, boss.")
            return
        if 'snap window left' in query:
            pyautogui.hotkey('win', 'left')
            speak("Snapped window to the left, boss.")
            return
        if 'snap window right' in query:
            pyautogui.hotkey('win', 'right')
            speak("Snapped window to the right, boss.")
            return
        if 'maximize window' in query:
            pyautogui.hotkey('win', 'up')
            speak("Maximized window, boss.")
            return
        if 'minimize window' in query:
            pyautogui.hotkey('win', 'down')
            speak("Minimized window, boss.")
            return

        # Formatting shortcuts
        if 'bold' in query:
            pyautogui.hotkey('ctrl', 'b')
            speak("Applied bold formatting, boss.")
            return
        if 'italic' in query:
            pyautogui.hotkey('ctrl', 'i')
            speak("Applied italic formatting, boss.")
            return
        if 'underline' in query:
            pyautogui.hotkey('ctrl', 'u')
            speak("Applied underline formatting, boss.")
            return
        if 'align left' in query:
            pyautogui.hotkey('ctrl', 'l')
            speak("Aligned text left, boss.")
            return
        if 'align center' in query:
            pyautogui.hotkey('ctrl', 'e')
            speak("Aligned text center, boss.")
            return
        if 'align right' in query:
            pyautogui.hotkey('ctrl', 'r')
            speak("Aligned text right, boss.")
            return

        # Other system shortcuts
        if 'open start menu' in query:
            pyautogui.press('win')
            speak("Opened Start menu, boss.")
            return
        if 'open run dialog' in query:
            pyautogui.hotkey('win', 'r')
            speak("Opened Run dialog, boss.")
            return
        if 'open power user menu' in query:
            pyautogui.hotkey('win', 'x')
            speak("Opened Power User menu, boss.")
            return
        if 'open system properties' in query:
            pyautogui.hotkey('win', 'pause')
            speak("Opened System Properties, boss.")
            return
    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while performing the shortcut command, boss.")
