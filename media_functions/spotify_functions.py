import pyautogui
import time
import webbrowser
from AppOpener import open
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_spotify_opening


def play_track_in_spotify(query):
    try:
        track_name = query.split("play ")[1]
        try:
            # Attempting to open the spotify application
            open("spotify", throw_error=True, match_closest=True)
            time.sleep(3)

            # Check for Spotify continuously for 10 seconds
            if check_spotify_opening():
                # Spotify found, proceed with the operation
                pass
            else:
                # Spotify not found within 10 seconds, ask the user whether to continue waiting or exit
                print(
                    "Sam: Spotify is taking longer than usual to open. Do you want to continue waiting, sir?")
                speak(
                    "Spotify is taking longer than usual to open. Do you want to continue waiting sir?")

                while True:
                    confirm = listen()
                    if confirm == "":
                        continue
                    if "yes" in confirm:
                        if not check_spotify_opening():
                            # Handle the case if Spotify still not found
                            print(f"Sam: Spotify is still taking time to open. Please manually play {track_name}")
                            speak(f"Spotify is still taking time to open. Please manually play {track_name}")
                            return
                    else:
                        print("Sam: Closing Spotify settings, sir")
                        speak("Closing Spotify settings sir")
                        pyautogui.hotkey('alt', 'f4')
                        return

            # Search for the track
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(1)

            pyautogui.write(track_name)
            pyautogui.press('enter')
            time.sleep(3)

        except Exception as e:
            search_url = f"https://open.spotify.com/"
            webbrowser.open(search_url)
            time.sleep(3)

            # Check for Spotify continuously for 10 seconds
            if check_spotify_opening():
                # Spotify found, proceed with the operation
                pass
            else:
                # Spotify not found within 10 seconds, ask the user whether to continue waiting or exit
                print(
                    "Sam: Spotify is taking longer than usual to open. Do you want to continue waiting, sir?")
                speak(
                    "Spotify is taking longer than usual to open. Do you want to continue waiting sir?")

                while True:
                    confirm = listen()
                    if confirm == "":
                        continue
                    if "yes" in confirm:
                        if not check_spotify_opening():
                            # Handle the case if Spotify still not found
                            print(f"Sam: Spotify is still taking time to open. Please manually play {track_name}")
                            speak(f"Spotify is still taking time to open. Please manually play {track_name}")
                            return
                    else:
                        print("Sam: Closing Spotify settings, sir")
                        speak("Closing Spotify settings sir")
                        pyautogui.hotkey('alt', 'f4')
                        return

            # Search for the track
            pyautogui.hotkey('ctrl', 'shift', 'l')
            time.sleep(1)

            pyautogui.write(track_name)
            pyautogui.press('enter')
            time.sleep(3)

        # Play the track
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)

        # Speak confirmation message
        print(f"Sam: Playing {track_name} on Spotify, sir.")
        speak(f"Playing {track_name} on Spotify sir")

        pyautogui.press('enter')

    except Exception as e:
        # Handle errors
        print("Sam: Sorry, I couldn't play the track on Spotify, sir.")
        speak("Sorry, I couldn't play the track on Spotify sir")


play_track_in_spotify("Shape of You")
