import pyautogui
from sam_functions.speak import speak


# Function perform various keyboard shortcuts and actions based on the provided query
def shortcut_functions(query, intent_data):
    try:
        # Detect the entity in the query
        detected_entities = [entity for entity in intent_data.get('entities', []) if entity in query.lower()]

        # Combined actions
        if detected_entities == ['select all', 'copy']:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            speak("All selected and copied sir.")
            return
        if detected_entities == ['select all', 'cut']:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'x')
            speak("All selected and cut sir.")
            return

        # Keyboard shortcuts
        if detected_entities == ['copy']:
            pyautogui.hotkey('ctrl', 'c')
            speak("Copied sir.")
            return

        if detected_entities == ['cut']:
            pyautogui.hotkey('ctrl', 'x')
            speak("Cut sir.")
            return

        if detected_entities == ['paste']:
            pyautogui.hotkey('ctrl', 'v')
            speak("Pasted sir.")
            return

        if detected_entities == ['undo']:
            pyautogui.hotkey('ctrl', 'z')
            speak("Undone sir.")
            return

        if detected_entities == ['redo']:
            pyautogui.hotkey('ctrl', 'y')
            speak("Redone sir.")
            return

        if detected_entities == ['select all']:
            pyautogui.hotkey('ctrl', 'a')
            speak("All selected sir.")
            return

            # Other shortcuts
        if detected_entities == ['find']:
            pyautogui.hotkey('ctrl', 'f')
            speak("Find activated sir.")
            return
        if detected_entities == ['save']:
            pyautogui.hotkey('ctrl', 's')
            speak("Saved sir.")
            return
        if detected_entities == ['print']:
            pyautogui.hotkey('ctrl', 'p')
            speak("Printed sir.")
            return

        if detected_entities == ['new tab']:
            pyautogui.hotkey('ctrl', 't')
            speak("New tab opened sir.")
            return

        if detected_entities == ['new']:
            pyautogui.hotkey('ctrl', 'n')
            speak("New document opened sir.")
            return

        # Window management shortcuts
        if detected_entities == ['task view']:
            pyautogui.hotkey('win', 'tab')
            speak("Task View activated sir.")
            return

        if detected_entities == ['switch apps']:
            pyautogui.hotkey('alt', 'tab')
            speak("Switched apps sir.")
            return

        if detected_entities == ['minimize all']:
            pyautogui.hotkey('win', 'm')
            speak("Minimized all windows sir.")
            return

        if detected_entities == ['show desktop']:
            pyautogui.hotkey('win', 'd')
            speak("Showed desktop sir.")
            return

        if detected_entities == ['snap window left']:
            pyautogui.hotkey('win', 'left')
            speak("Snapped window to the left sir.")
            return

        if detected_entities == ['snap window right']:
            pyautogui.hotkey('win', 'right')
            speak("Snapped window to the right sir.")
            return

        if detected_entities == ['maximize window']:
            pyautogui.hotkey('win', 'up')
            speak("Maximized window sir.")
            return

        if detected_entities == ['minimize window']:
            pyautogui.hotkey('win', 'down')
            speak("Minimized window sir.")
            return

        # Formatting shortcuts
        if detected_entities == ['bold']:
            pyautogui.hotkey('ctrl', 'b')
            speak("Applied bold formatting sir.")
            return

        if detected_entities == ['italic']:
            pyautogui.hotkey('ctrl', 'i')
            speak("Applied italic formatting sir.")
            return

        if detected_entities == ['underline']:
            pyautogui.hotkey('ctrl', 'u')
            speak("Applied underline formatting sir.")
            return

        if detected_entities == ['align left']:
            pyautogui.hotkey('ctrl', 'l')
            speak("Aligned text left sir.")
            return

        if detected_entities == ['align center']:
            pyautogui.hotkey('ctrl', 'e')
            speak("Aligned text center sir.")
            return

        if detected_entities == ['align right']:
            pyautogui.hotkey('ctrl', 'r')
            speak("Aligned text right sir.")
            return

        # Other system shortcuts
        if detected_entities == ['open start menu']:
            pyautogui.press('win')
            speak("Opened Start menu sir.")
            return

        if detected_entities == ['open run dialog']:
            pyautogui.hotkey('win', 'r')
            speak("Opened Run dialog sir.")
            return

        if detected_entities == ['open power user menu']:
            pyautogui.hotkey('win', 'x')
            speak("Opened Power User menu sir.")
            return

        if detected_entities == ['open system properties']:
            pyautogui.hotkey('win', 'pause')
            speak("Opened System Properties sir.")
            return

    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while performing the shortcut command sir.")
