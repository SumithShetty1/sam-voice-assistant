import pyautogui
import time
import webbrowser
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_youtube_opening


def play_video_on_youtube(query):
    try:
        video_name = query.split("play ")[1]

        search_url = f"https://www.youtube.com/"
        webbrowser.open(search_url)
        time.sleep(3)

        # Check for YouTube continuously for 10 seconds
        if check_youtube_opening():
            # YouTube found, proceed with the operation
            pass
        else:
            # YouTube not found within 10 seconds, ask the user whether to continue waiting or exit
            print(
                "Sam: YouTube is taking longer than usual to open. Do you want to continue waiting, sir?")
            speak(
                "YouTube is taking longer than usual to open. Do you want to continue waiting sir?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_youtube_opening():
                        # Handle the case if YouTube still not found
                        print(f"Sam: YouTube is still taking time to open. Please manually play {video_name}")
                        speak(f"YouTube is still taking time to open. Please manually play {video_name}")
                        return
                else:
                    print("Sam: Closing YouTube, sir")
                    speak("Closing YouTube sir")
                    pyautogui.hotkey('alt', 'f4')
                    return

        # Search for the video
        pyautogui.press('/')
        time.sleep(1)

        pyautogui.write(video_name)
        pyautogui.press('enter')
        time.sleep(3)

        # Speak confirmation message
        print(f"Sam: Playing {video_name} on YouTube, sir.")
        speak(f"Playing {video_name} on YouTube sir")

    except Exception as e:
        # Handle errors
        print("Sam: Sorry, I couldn't play the video on YouTube, sir.")
        speak("Sorry, I couldn't play the video on YouTube sir")


play_video_on_youtube("play Shape of You")
