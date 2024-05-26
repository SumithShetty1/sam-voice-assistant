import time
import pyautogui
from sam_functions.speak import speak
from sam_functions.listen import listen
from random import choice
import eel
from intent_detect.load_model import recognize_intent


def system_control(intent_data):
    try:
        # Use a random response from the JSON data
        response = choice(intent_data["responses"])

        if intent_data['intent'] == "system_control_lock":
            speak("Warning! Locking the system will interrupt any ongoing tasks. Do you want to continue sir?")
            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("System lock cancelled sir.")
                    return
                elif confirm['intent'] == "yes":
                    break
                elif confirm['intent'] == "exit":
                    speak(confirm["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

            speak(response + " sir.")
            pyautogui.hotkey('win', 'l')
            eel.close_window()
            exit()

        elif intent_data['intent'] == "system_control_sleep":
            speak("Warning! Putting the system to sleep will interrupt any ongoing tasks. Do you want to continue sir?")
            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("System sleep cancelled sir.")
                    return
                elif confirm['intent'] == "yes":
                    break
                elif confirm['intent'] == "exit":
                    speak(intent_data["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

            speak(response + " sir.")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('left')
            time.sleep(0.2)
            pyautogui.press('enter')
            eel.close_window()
            exit()

        elif intent_data['intent'] == "system_control_sign_out":
            speak("Are you sure you want to sign out sir?")
            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Sign out cancelled sir.")
                    return
                elif confirm['intent'] == "yes":
                    break
                elif confirm['intent'] == "exit":
                    speak(intent_data["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

            speak(response + " sir.")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('left')
            time.sleep(0.2)
            pyautogui.press('left')
            time.sleep(0.2)
            pyautogui.press('enter')
            eel.close_window()
            exit()

        elif intent_data['intent'] == "system_control_restart":
            speak("Are you sure you want to restart the system sir?")
            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Restart cancelled sir.")
                    return
                elif confirm['intent'] == "yes":
                    break
                elif confirm['intent'] == "exit":
                    speak(intent_data["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

            speak(response + " sir.")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('right')
            time.sleep(0.2)
            pyautogui.press('enter')
            eel.close_window()
            exit()

        elif intent_data['intent'] == "system_control_shutdown":
            speak("Are you sure you want to shut down the system sir?")
            while True:
                query = listen()

                if query == "":
                    continue

                confirm = recognize_intent(query)
                if confirm['intent'] == "no" or confirm['intent'] == "assistant_sleep":
                    speak("Shutdown cancelled sir.")
                    return
                elif confirm['intent'] == "yes":
                    break
                elif confirm['intent'] == "exit":
                    speak(intent_data["responses"])
                    eel.close_window()
                    exit()
                else:
                    speak("Sorry sir, I didn't quite catch that.")
                    continue

            speak(response + " sir.")
            pyautogui.hotkey('win', 'd')  # Show desktop
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press('enter')
            eel.close_window()
            exit()

    except Exception as e:
        speak(f"An error occurred")
        speak("Oops! Something went wrong while performing the system control command sir.")
