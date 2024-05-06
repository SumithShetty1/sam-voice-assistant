import pyautogui
from sam_functions.speak import speak


# Function perform various keyboard shortcuts and actions based on the provided query
def shortcut_functions(query):
    try:
        # Combined actions
        if 'select all' in query and 'copy' in query:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            print("Sam: All selected and copied, sir.")
            speak("All selected and copied sir")
            return
        if 'select all' in query and 'cut' in query:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'x')
            print("Sam: All selected and cut, sir.")
            speak("All selected and cut sir")
            return

        # Keyboard shortcuts
        if 'copy' in query:
            pyautogui.hotkey('ctrl', 'c')
            print("Sam: Copied, sir.")
            speak("Copied sir")
            return
        if 'cut' in query:
            pyautogui.hotkey('ctrl', 'x')
            print("Sam: Cut, sir.")
            speak("Cut sir")
            return
        if 'paste' in query:
            pyautogui.hotkey('ctrl', 'v')
            print("Sam: Pasted, sir.")
            speak("Pasted sir")
            return
        if 'undo' in query:
            pyautogui.hotkey('ctrl', 'z')
            print("Sam: Undone, sir.")
            speak("Undone sir")
            return
        if 'redo' in query:
            pyautogui.hotkey('ctrl', 'y')
            print("Sam: Redone, sir.")
            speak("Redone sir")
            return

        if 'select all' in query:
            pyautogui.hotkey('ctrl', 'a')
            print("Sam: All selected, sir.")
            speak("All selected sir")
            return

            # Other shortcuts
        if 'find' in query:
            pyautogui.hotkey('ctrl', 'f')
            print("Sam: Find activated, sir.")
            speak("Find activated sir")
            return
        if 'save' in query:
            pyautogui.hotkey('ctrl', 's')
            print("Sam: Saved, sir.")
            speak("Saved sir")
            return
        if 'print' in query:
            pyautogui.hotkey('ctrl', 'p')
            print("Sam: Printed, sir.")
            speak("Printed sir")
            return

        if 'new tab' in query:
            pyautogui.hotkey('ctrl', 't')
            print("Sam: New tab opened, sir.")
            speak("New tab opened sir")
            return

        if 'new' in query:
            pyautogui.hotkey('ctrl', 'n')
            print("Sam: New document opened, sir.")
            speak("New document opened sir")
            return

        # Window management shortcuts
        if 'task view' in query:
            pyautogui.hotkey('win', 'tab')
            print("Sam: Task View activated, sir.")
            speak("Task View activated sir")
            return
        if 'switch apps' in query:
            pyautogui.hotkey('alt', 'tab')
            print("Sam: Switched apps, sir.")
            speak("Switched apps sir")
            return
        if 'minimize all' in query:
            pyautogui.hotkey('win', 'm')
            print("Sam: Minimized all windows, sir.")
            speak("Minimized all windows sir")
            return
        if 'show desktop' in query:
            pyautogui.hotkey('win', 'd')
            print("Sam: Showed desktop, sir.")
            speak("Showed desktop sir")
            return
        if 'snap window left' in query:
            pyautogui.hotkey('win', 'left')
            print("Sam: Snapped window to the left, sir.")
            speak("Snapped window to the left sir")
            return
        if 'snap window right' in query:
            pyautogui.hotkey('win', 'right')
            print("Sam: Snapped window to the right, sir.")
            speak("Snapped window to the right sir")
            return
        if 'maximize window' in query:
            pyautogui.hotkey('win', 'up')
            print("Sam: Maximized window, sir.")
            speak("Maximized window sir")
            return
        if 'minimize window' in query:
            pyautogui.hotkey('win', 'down')
            print("Sam: Minimized window, sir.")
            speak("Minimized window sir")
            return

        # Formatting shortcuts
        if 'bold' in query:
            pyautogui.hotkey('ctrl', 'b')
            print("Sam: Applied bold formatting, sir.")
            speak("Applied bold formatting sir")
            return
        if 'italic' in query:
            pyautogui.hotkey('ctrl', 'i')
            print("Sam: Applied italic formatting, sir.")
            speak("Applied italic formatting sir")
            return
        if 'underline' in query:
            pyautogui.hotkey('ctrl', 'u')
            print("Sam: Applied underline formatting, sir.")
            speak("Applied underline formatting sir")
            return
        if 'align left' in query:
            pyautogui.hotkey('ctrl', 'l')
            print("Sam: Aligned text left, sir.")
            speak("Aligned text left sir")
            return
        if 'align center' in query:
            pyautogui.hotkey('ctrl', 'e')
            print("Sam: Aligned text center, sir.")
            speak("Aligned text center sir")
            return
        if 'align right' in query:
            pyautogui.hotkey('ctrl', 'r')
            print("Sam: Aligned text right, sir.")
            speak("Aligned text right sir")
            return

        # Other system shortcuts
        if 'open start menu' in query:
            pyautogui.press('win')
            print("Sam: Opened Start menu, sir.")
            speak("Opened Start menu sir")
            return
        if 'open run dialog' in query:
            pyautogui.hotkey('win', 'r')
            print("Sam: Opened Run dialog, sir.")
            speak("Opened Run dialog sir")
            return
        if 'open power user menu' in query:
            pyautogui.hotkey('win', 'x')
            print("Sam: Opened Power User menu, sir.")
            speak("Opened Power User menu sir")
            return
        if 'open system properties' in query:
            pyautogui.hotkey('win', 'pause')
            print("Sam: Opened System Properties, sir.")
            speak("Opened System Properties sir")
            return
    except Exception as e:
        print(f"Sam: An error occurred: {e}")
        print("Oops! Something went wrong while performing the shortcut command, sir.")
        speak("Oops! Something went wrong while performing the shortcut command sir")
