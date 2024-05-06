from sam_functions.speak import speak
from windows_functions.search_in_windows import search_in_windows
import webbrowser
import pyautogui
from search_bar import search_bar


def search(query):
    try:
        if "google" in query or "chrome" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://www.google.com/search?q={search_query}"
            print(f"Searching the web for {search_query}, sir.")
            speak(f"Searching the web for {search_query} sir")
            webbrowser.open(search_url)

        elif "youtube" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://www.youtube.com/results?search_query={search_query}"
            print(f"Searching YouTube for {search_query}, sir.")
            speak(f"Searching YouTube for {search_query} sir")
            webbrowser.open(search_url)

        elif "spotify" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://open.spotify.com/search/{search_query}"
            print(f"Searching Spotify for {search_query}, sir.")
            speak(f"Searching Spotify for {search_query} sir")
            webbrowser.open(search_url)

        elif "linkedin" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://www.linkedin.com/search/results/all/?keywords={search_query}"
            print(f"Searching LinkedIn for {search_query}, sir.")
            speak(f"Searching LinkedIn for {search_query} sir")
            webbrowser.open(search_url)

        elif "amazon" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://www.amazon.in/s?k={search_query}"
            print(f"Searching Amazon for {search_query}, sir.")
            speak(f"Searching Amazon for {search_query} sir")
            webbrowser.open(search_url)

        elif "twitter" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://twitter.com/search?q={search_query}"
            print(f"Searching Twitter for {search_query}, sir.")
            speak(f"Searching Twitter for {search_query} sir")
            webbrowser.open(search_url)

        elif "github" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://github.com/search?q={search_query}"
            print(f"Searching GitHub for {search_query}, sir.")
            speak(f"Searching GitHub for {search_query} sir")
            webbrowser.open(search_url)

        elif "wikipedia" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://en.wikipedia.org/wiki/{search_query}"
            print(f"Searching Wikipedia for {search_query}, sir.")
            speak(f"Searching Wikipedia for {search_query} sir")
            webbrowser.open(search_url)

        elif "facebook" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://www.facebook.com/search/top/?q={search_query}"
            print(f"Searching Facebook for {search_query}, sir.")
            speak(f"Searching Facebook for {search_query} sir")
            webbrowser.open(search_url)

        elif "instagram" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://www.instagram.com/explore/tags/{search_query}"
            print(f"Searching Instagram for {search_query}, sir.")
            speak(f"Searching Instagram for {search_query} sir")
            webbrowser.open(search_url)

        elif "netflix" in query:
            search_query = query.split("search ")[1]
            search_url = f"https://www.netflix.com/search?q={search_query}"
            print(f"Searching Netflix for {search_query}, sir.")
            speak(f"Searching Netflix for {search_query} sir")
            webbrowser.open(search_url)

        elif "bing" in query or "edge" in query:
            pyautogui.press("win")
            # Type "edge" to search for Microsoft Edge
            pyautogui.write("edge")
            # Press Enter to open Microsoft Edge
            pyautogui.press("enter")
            # Wait for Edge to open
            pyautogui.sleep(2)

            # Type the Bing search URL in the address bar
            search_query = query.split("search ")[1]
            search_url = f"https://www.bing.com/search?q={search_query}"
            pyautogui.write(search_url)
            pyautogui.press("enter")

            # Display assistant's message
            print(f"Sam: Searching Bing for {search_query}, sir")
            speak(f"Searching Bing for {search_query} sir")

        elif "windows" in query:
            search_in_windows(query)

        else:
            search_bar(query)

    except IndexError:
        print("Sam: Please specify the search query, sir")
        speak("Please specify the search query sir")
    except Exception as e:
        print(f"Sam: Error performing search: {e}")
        print("Sam: Sorry, I couldn't perform the search, sir")
        speak("Sorry I couldn't perform the search sir")
