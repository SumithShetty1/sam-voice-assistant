import pyautogui
import time
import webbrowser
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_youtube_opening, check_spotify_opening, check_dark_mode
from AppOpener import open


def play_track_in_spotify(track_name):
    try:
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
                speak(
                    "Spotify is taking longer than usual to open. Do you want to continue waiting boss?")

                while True:
                    confirm = listen()
                    if confirm == "":
                        continue
                    if "yes" in confirm:
                        if not check_spotify_opening():
                            # Handle the case if Spotify still not found
                            speak(f"Spotify is still taking time to open. Please manually play {track_name}")
                            return
                    else:
                        speak("Closing Spotify boss")
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
                speak(
                    "Spotify is taking longer than usual to open. Do you want to continue waiting boss?")

                while True:
                    confirm = listen()
                    if confirm == "":
                        continue
                    if "yes" in confirm:
                        if not check_spotify_opening():
                            # Handle the case if Spotify still not found
                            speak(f"Spotify is still taking time to open. Please manually play {track_name}")
                            return
                    else:
                        speak("Closing Spotify boss")
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
        pyautogui.press('enter')
        time.sleep(1)
        # Speak confirmation message
        speak(f"Playing {track_name} on Spotify boss.")
        time.sleep(0.6)
        pyautogui.press('enter')

    except Exception as e:
        # Handle errors
        speak("Sorry, I couldn't play the track on Spotify boss.")


def play_video_on_youtube(video_name):
    try:
        search_url = f"https://www.youtube.com/"
        webbrowser.open(search_url)
        time.sleep(3.5)

        # Check for YouTube continuously for 10 seconds
        if check_youtube_opening():
            # YouTube found, proceed with the operation
            pass
        else:
            # YouTube not found within 10 seconds, ask the user whether to continue waiting or exit
            speak(
                "YouTube is taking longer than usual to open. Do you want to continue waiting boss?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_youtube_opening():
                        # Handle the case if YouTube still not found
                        speak(f"YouTube is still taking time to open. Please manually play {video_name}")
                        return
                else:
                    speak("Closing YouTube boss")
                    pyautogui.hotkey('alt', 'f4')
                    return

        # Search for the video
        pyautogui.press('/')
        time.sleep(1)

        pyautogui.write(video_name)
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(3)

        # Click on the first video link
        first_video_position = None

        try:
            if not check_dark_mode():
                first_video_position = pyautogui.locateCenterOnScreen(
                    "images/light_mode/youtube/views.png", confidence=0.9)
            else:
                first_video_position = pyautogui.locateCenterOnScreen(
                    "images/dark_mode/youtube/views.png", confidence=0.9)
        except pyautogui.ImageNotFoundException:
            pass
        except Exception as e:
            pass

        if first_video_position:
            pyautogui.click(first_video_position)
            # Speak confirmation message
            speak(f"Playing {video_name} on YouTube boss.")
        else:
            speak("Please pick a video from the list of videos manually boss.")

    except Exception as e:
        # Handle errors
        speak("Sorry, I couldn't play the video on YouTube boss.")


# Function to play music or video
def play_functions(query):
    try:
        if "spotify" in query:
            track_name = query.split("play ")[1]
            play_track_in_spotify(track_name)
        else:
            video_name = query.split("play ")[1]
            play_video_on_youtube(video_name)

    except Exception as e:
        # Handle errors
        speak("Please specify what to play boss")